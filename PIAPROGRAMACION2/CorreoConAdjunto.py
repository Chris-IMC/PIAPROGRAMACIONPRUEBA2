import email, smtplib, ssl
import logging
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

logging.basicConfig(level=logging.INFO, filemode="Tareas_de_ciberseguridad.log", format="%(asctime)s - %(levelname)s - %(message)s")

class CorreoConAdjunto:

    def Correo(self):

        print("Adjunta los datos necesarios para el envio de correo")

        while True:
            subject = input("Escriba el asunto y presione enter: ")
            body = input("Escriba el cuerpo y presione enter: ")
            if not subject or body:
                print("Porfavor ingrese bien los datos requeridos")
            else:
                break

        while True:
            sender_email = input("Escriba la direccion desde la que se enviara el correo y presione enter: ")
            receiver_email = input("Escriba la direccion de destino y presione enter: ")
            if not sender_email or receiver_email:
                print("Porfavor ingrese bien los datos requeridos")
            else:
                break

        while True:
            password = input("Escriba la contraseña del correo y presione enter: ")
            if not password:
                print("Porfavor ingrese bien el dato requerido")
            else:
                break

        try:

            message = MIMEMultipart()
            message["From"] = sender_email
            message["To"] = receiver_email
            message["Subject"] = subject
            message["Bcc"] = receiver_email

            message.attach(MIMEText(body, "plain"))

            filename = "meme.jpeg"

            with open(filename, "rb") as attachment:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())

            encoders.encode_base64(part)

            part.add_header(
                "Content-Disposition",
                f"attachment; filename= {filename}",
            )

            message.attach(part)
            text = message.as_string()

            context = ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, text)





        except Exception as error:
            logging.error(error, exc_info=True)
            print("Hay un problema")





