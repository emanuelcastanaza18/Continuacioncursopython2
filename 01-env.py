#Variables de entorno
# SENDGRID_API_KEY= ""

import os
from sendgrid.helpers.mail import mail
from sendgrid import SendGridAPIClient

email = os.environ.get('SENDGRID_EMAIL')

menaje = mail.Mail(
    from_email=email,
    to_emails=email,
    subject='Prueba de envio de email',
    html_content='Curso de <b>Ultimate Python</b>'
)

try:
    apikey = os.environ.get('SENDGRID_API_KEY')
    sg = SendGridAPIClient(apikey)
    respuesta = sg.send(menaje)
    print(
        respuesta.status_code, #El estado de la respuesta
        respuesta.body, #Para saber el mensaje
        respuesta.headers, #Cabeceras 
    )
except Exception as e:
    print(e)