from flask import Flask, request
from flask_restful import Api, Resource
from datetime import datetime
import json
import logging
import os
from dotenv import load_dotenv
from security.authentication import verify_password
from security.authorization import require_permission
from database.queries import insert_sensor_data, get_sensor_data
from monitoring.sensor_monitor import SensorMonitor

app = Flask(__name__)
api = Api(app)

load_dotenv()

# Setup logging
logging.basicConfig(filename='logs.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

# Initialize sensor monitor
sensor_monitor = SensorMonitor()

# Authentication and authorization
def authenticate(username, password):
    return verify_password(username, password)

def identity(payload):
    user_id = payload['identity']
    return {'user_id': user_id}

# Routes
class SensorData(Resource):
    @require_permission('read')
    def get(self):
        data = get_sensor_data()
        return json.loads(data)

    @require_permission('write')
    def post(self):
        data = request.json
        data['timestamp'] = datetime.now().isoformat()
        insert_sensor_data(data)
        return {'message': 'Data saved'}

api.add_resource(SensorData, '/api/sensor_data')

if __name__ == '__main__':
    app.run(debug=True, host=os.getenv('FLASK_APP_HOST'), port=os.getenv('FLASK_APP_PORT'))
