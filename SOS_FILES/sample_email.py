import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import ssl


email_sender = 'jahaganapathi1@gmail.com'
email_password = 'bkggefxqikzpbmke'  


email_receivers = ['arunaananthagiri04@gmail.com', 'mathavramalingam1608@gmail.com', 'sreepriyanth2005@gmail.com','bavyadharshinir.22cse@kongu.edu']


url = 'https://66c62f95a65a5b61a9d3136b--coruscating-marigold-a0ceb0.netlify.app/'


filename = 'Recorded.wav'


context = ssl.create_default_context()
try:
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        
        for email_receiver in email_receivers:
            
            msg = MIMEMultipart()
            msg['From'] = email_sender
            msg['To'] = email_receiver
            msg['Subject'] = "SOS ALERT"
            
            
            body = f"SOS ALERT DETECTED. Please visit the following link for more details: {url}"
            msg.attach(MIMEText(body, 'plain'))
            
            
            try:
                with open(filename, 'rb') as f:
                    attachment = MIMEApplication(f.read(), _subtype='wav')
                    attachment.add_header('Content-Disposition', 'attachment', filename=filename)
                    msg.attach(attachment)
            except FileNotFoundError:
                print(f"Error: The file '{filename}' was not found.")
                continue  
            
            
            smtp.sendmail(email_sender, email_receiver, msg.as_string())
        
    print("Emails successfully sent.")
except smtplib.SMTPAuthenticationError:
    print("Failed to authenticate. Check your email and password.")
except smtplib.SMTPConnectError:
    print("Failed to connect to the SMTP server.")
except Exception as e:
    print(f"Failed to send email. Error: {str(e)}")
