from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
import smtplib
import ssl
from email.message import EmailMessage
from twilio.rest import Client
import speech_recognition as sr
import pyttsx3

class SOSApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        # Button to start voice recognition
        self.sos_button = Button(text="Press to Activate SOS", font_size=24)
        self.sos_button.bind(on_press=self.recognize_voice)
        layout.add_widget(self.sos_button)

        return layout

    def recognize_voice(self, instance):
        # Voice recognition logic
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

            try:
                print("Recognizing...")
                query = recognizer.recognize_google(audio, language='en-in').lower()
                if "sos" in query:
                    self.send_sos_alert()
                else:
                    print("No SOS detected")
            except sr.UnknownValueError:
                print("Could not understand audio")

    def send_sos_alert(self):
        self.sos_button.text = "SOS Alert Sent!"
        self.email_sos()
        self.sms_alert()
        self.call_sos()

    def email_sos(self):
        # Email sending logic (same as your script)
        email_sender = 'jahaganapathi1@gmail.com'
        email_password = 'bkggefxqikzpbmke'
        email_receiver = 'sreepriyanth2005@gmail.com'
        subject = 'SOS ALERT!'
        body = 'This is an SOS alert. Help needed immediately!'
        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = email_receiver
        em['Subject'] = subject
        em.set_content(body)
        context = ssl.create_default_context()
        try:
            with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
                smtp.starttls(context=context)
                smtp.login(email_sender, email_password)
                smtp.sendmail(email_sender, email_receiver, em.as_string())
            print("Email sent successfully.")
        except Exception as e:
            print(f"Failed to send email. Error: {str(e)}")

    def sms_alert(self):
        # SMS sending logic (same as your script)
        account_sid = "ACcd0d88307fcfd80e81de7e8885fe2d3f"
        auth_token = "fcac17f33fa681e4289c6871c800b005"
        client = Client(account_sid, auth_token)
        phone_numbers = ["+911234567890", "+919876543210"]
        for number in phone_numbers:
            client.messages.create(body="SOS Alert! Help needed!", from_="+12562239694", to=number)
        print("SMS sent successfully.")

    def call_sos(self):
        # Call alert logic (same as your script)
        account_sid = "ACcd0d88307fcfd80e81de7e8885fe2d3f"
        auth_token = "fcac17f33fa681e4289c6871c800b005"
        client = Client(account_sid, auth_token)
        client.calls.create(url='http://demo.twilio.com/docs/voice.xml', to="+911234567890", from_="+12562239694")
        print("Call made successfully.")

if __name__ == '__main__':
    SOSApp().run()
