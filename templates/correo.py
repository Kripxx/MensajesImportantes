import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def enviar_correo(destinatario, asunto, mensaje):
    remitente = "tucorreo@gmail.com"
    password = "tu_contraseña"  # ⚠️ Usa .env en producción

    msg = MIMEMultipart()
    msg['From'] = remitente
    msg['To'] = destinatario
    msg['Subject'] = asunto
    msg.attach(MIMEText(mensaje, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(remitente, password)
        server.sendmail(remitente, destinatario, msg.as_string())
        server.quit()
        print("✅ Correo enviado con éxito.")
    except Exception as e:
        print(f"❌ Error al enviar el correo: {e}")
