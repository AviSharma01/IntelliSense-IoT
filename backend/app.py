import boto3
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

# Initialize Flask app
app = Flask(__name__)
app.config.from_pyfile('settings.py')

# Initialize SQLAlchemy database object
db = SQLAlchemy(app)

# Initialize JWT manager object
jwt = JWTManager(app)

# Initialize AWS IoT client object
iot = boto3.client('iot')

shadow = boto3.client('iot-data')

# Define function to handle incoming data
def iot_data_handler(payload):
    # Extract the desired data from the payload
    data = json.loads(payload)
    temperature = data['temperature']
    humidity = data['humidity']

    # Insert data into the database
    new_data = TemperatureData(temperature=temperature, humidity=humidity)
    db.session.add(new_data)
    db.session.commit()

    # Update the shadow
    shadow.update_thing_shadow(
        thingName='my_thing',
        payload=json.dumps({
            'state': {
                'reported': {
                    'temperature': temperature,
                    'humidity': humidity
                }
            }
        })
    )


# Subscribe to the IoT topic
iot.subscribe(
    topic='my_topic',
    qos=1,
    callback=iot_data_handler
)

@app.route('/api/temperature')
def get_temperature():
    # Get temperature data from database
    temperature_data = Temperature.query.all()

    # Convert database objects to dictionary format
    temperature_list = []
    for temperature in temperature_data:
        temperature_dict = {
            'timestamp': temperature.timestamp,
            'temperature': temperature.temperature
        }
        temperature_list.append(temperature_dict)

    # Return temperature data as JSON
    return jsonify(temperature_list)


if __name__ == '__main__':
    app.run()

