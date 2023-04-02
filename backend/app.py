from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config.from_pyfile('settings.py')

db = SQLAlchemy(app)
jwt = JWTManager(app)

@app.route('/')
def hello():
    return 'Hello, World!'

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
