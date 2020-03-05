import connexion
from connexion import NoContent

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from base import Base
from request import Request
from report import Report
import datetime
from datetime import datetime
import yaml
from threading import Thread
import json
from pykafka import KafkaClient

with open('app_conf.yaml', 'r') as f:
    app_config = yaml.safe_load(f.read())


DB_ENGINE = create_engine('mysql+pymysql://{}:{}@{}:{}/{}'.format(
    app_config['datastore']['user'],app_config['datastore']['password'],
    app_config['datastore']['hostname'],app_config['datastore']['port'],
    app_config['datastore']['db']))
Base.metadata.bind = DB_ENGINE
DB_SESSION = sessionmaker(bind=DB_ENGINE)

print("{}:{}".format(app_config['kafka']['server'], app_config['kafka']['port']))
print(app_config['kafka']['topic'])
client = KafkaClient(hosts="{}:{}".format(app_config['kafka']['server'], app_config['kafka']['port']))
topic = client.topics[app_config['kafka']['topic']]
consumer = topic.get_simple_consumer(auto_commit_enable=True, auto_commit_interval_ms=1000)


# def add_ride_request(requestInfo):
# #     """ Receives a ride request """
# #
# #     session = DB_SESSION()
# #
# #     rq = Request(requestInfo['name'],
# #                  requestInfo['location'],
# #                  requestInfo['destination'],
# #                  requestInfo['time'],
# #                  requestInfo['notes'])
# #
# #     session.add(rq)
# #
# #     session.commit()
# #     session.close()
# #
# #     return NoContent, 201

def get_ride_request(startDate, endDate):
    """ Get a ride request submission from the data store """

    results_list = []

    session = DB_SESSION()

    results = []

    results = session.query(Request).filter(Request.date_created >= datetime.fromisoformat(startDate), Request.date_created <= datetime.fromisoformat(endDate))

    for result in results:
        results_list.append(result.to_dict())
        print(result.to_dict())

    session.close()

    return results_list, 200


# def add_ride_report(reportInfo):
#     """ Add a ride report from the data store """
#     session = DB_SESSION()
#
#     rp = Report(reportInfo['name'],
#                 reportInfo['customer'],
#                 reportInfo['pickup'],
#                 reportInfo['dropoff'],
#                 reportInfo['pickuptime'],
#                 reportInfo['dropofftime'],
#                 reportInfo['rating'],
#                 reportInfo['notes'])
#     session.add(rp)
#
#     session.commit()
#     session.close()
#
#     return NoContent, 201


def get_ride_report(startDate, endDate):
    """ Ger a ride report from the data store """

    results_list = []

    session = DB_SESSION()

    results = []

    results = session.query(Report).filter(Report.date_created>=startDate, Report.date_created<=endDate)

    for result in results:
        results_list.append(result.to_dict())
        print(result.to_dict())

    session.close()

    return results_list, 200

def process_messages():

    print("Process message")
    for msg in consumer:
        print(msg)
        msg_str = msg.value.decode('utf-8')
        msg = json.loads(msg_str)

        if msg['type'] == 'request':
            session = DB_SESSION()
            rq = Request(msg['name'],
                         msg['location'],
                         msg['destination'],
                         msg['time'],
                         msg['notes'])

            session.add(rq)

            session.commit()
            session.close()

        elif msg['type'] == 'report':
            session = DB_SESSION()
            rp = Report(msg['name'],
                        msg['customer'],
                        msg['pickup'],
                        msg['dropoff'],
                        msg['pickuptime'],
                        msg['dropofftime'],
                        msg['rating'],
                        msg['notes'])

            session.add(rp)

            session.commit()
            session.close()


app = connexion.FlaskApp(__name__, specification_dir='')
app.add_api("openapi.yaml")

if __name__ == "__main__":
    t1 = Thread(target=process_messages)
    t1.setDaemon(True)
    t1.start()
    app.run(port=8090)

