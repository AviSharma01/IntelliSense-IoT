import smtplib
from email.mime.text import MIMEText

def send_alert(sender_email, sender_password, recipient_email, subject, message):
    # Create a MIME message object
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = recipient_email

    # Connect to the email server and login
    smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
    smtp_server.starttls()
    smtp_server.login(sender_email, sender_password)

    # Send the email
    smtp_server.sendmail(sender_email, recipient_email, msg.as_string())
    smtp_server.quit()

def check_sensor_readings(sensor_readings):
    # Check if temperature is too high
    if sensor_readings['temperature'] > 30:
        send_alert(sender_email='myemail@gmail.com',
                   sender_password='mypassword',
                   recipient_email='alerts@example.com',
                   subject='High Temperature Alert',
                   message='Temperature is too high: {}'.format(sensor_readings['temperature']))
    
    # Check if humidity is too low
    if sensor_readings['humidity'] < 40:
        send_alert(sender_email='myemail@gmail.com',
                   sender_password='mypassword',
                   recipient_email='alerts@example.com',
                   subject='Low Humidity Alert',
                   message='Humidity is too low: {}'.format(sensor_readings['humidity']))
