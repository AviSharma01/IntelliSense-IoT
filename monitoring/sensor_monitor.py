import random
import time
from monitoring.alerting import send_alert

def read_sensor_data():
    """
    Simulate reading sensor data.
    """
    # Generate random values for temperature and humidity
    temperature = random.uniform(20.0, 30.0)
    humidity = random.uniform(30.0, 50.0)
    
    return temperature, humidity

def monitor_sensors():
    """
    Monitor sensors for abnormal readings and send alerts if necessary.
    """
    while True:
        # Read sensor data
        temperature, humidity = read_sensor_data()
        
        # Check if temperature or humidity is outside of normal range
        if temperature < 22.0 or temperature > 28.0:
            send_alert(f"Temperature reading out of range: {temperature}")
        if humidity < 35.0 or humidity > 45.0:
            send_alert(f"Humidity reading out of range: {humidity}")
        
        # Wait for a minute before reading data again
        time.sleep(60)
