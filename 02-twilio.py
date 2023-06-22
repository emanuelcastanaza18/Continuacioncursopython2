import os
import twilio.rest import Client

sid = os.environ.get['TWILIO_ACCOUNT_SID']
token = os.environ.get['TWILIO_TOKEN']
numero = os.environ.get['TWILIO_N']

cliente = Client(sid, token)
mensaje = cliente.messages.create(
    body="Hola mundo!",
    from_=numero,
    to="+15558675310"
)