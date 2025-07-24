from flask import Flask, render_template, request, redirect, url_for, flash
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from conexion import obtener_conexion

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta_segura'

# -------------------------------
# Función para enviar correo
# -------------------------------
def enviar_correo(asunto, contenido_html, destinatarios):
    remitente = "cossasutilesso@gmail.com"
    password = "hdomufccuykobyra"  # sin espacios

    msg = MIMEMultipart()
    msg['From'] = remitente
    msg['To'] = ", ".join(destinatarios) if isinstance(destinatarios, list) else destinatarios
    msg['Subject'] = asunto

    # Contenido en HTML
    msg.attach(MIMEText(contenido_html, 'html'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(remitente, password)
        server.sendmail(remitente, destinatarios, msg.as_string())
        server.quit()
        print("✅ Correo enviado correctamente.")
    except Exception as e:
        print("❌ Error enviando correo:", e)

# -------------------------------
# Rutas Flask
# -------------------------------
@app.route('/')
def formulario():
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)

    cursor.execute("SELECT area_id, nombre FROM areas")
    areas = cursor.fetchall()

    cursor.execute("SELECT motivo_id, nombre FROM motivos")
    motivos = cursor.fetchall()

    cursor.close()
    conexion.close()

    return render_template('index.html', areas=areas, motivos=motivos)

@app.route('/guardar', methods=['POST'])
def guardar():
    area_id = request.form['area_id']
    motivo_id = request.form['motivo_id']
    asunto = request.form['asunto']
    contenido = request.form['contenido']
    estado = request.form['estado']
    destinatario = request.form['correo_destino']

    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)

    # 🔍 Obtener nombre del área
    cursor.execute("SELECT nombre FROM areas WHERE area_id = %s", (area_id,))
    area = cursor.fetchone()
    nombre_area = area['nombre'] if area else "No especificado"

    # 🔍 Obtener nombre del motivo
    cursor.execute("SELECT nombre FROM motivos WHERE motivo_id = %s", (motivo_id,))
    motivo = cursor.fetchone()
    nombre_motivo = motivo['nombre'] if motivo else "No especificado"

    # 💾 Guardar en base de datos
    sql = '''
        INSERT INTO citaciones (area_id, motivo_id, asunto, contenido, estado)
        VALUES (%s, %s, %s, %s, %s)
    '''
    cursor.execute(sql, (area_id, motivo_id, asunto, contenido, estado))
    conexion.commit()
    cursor.close()
    conexion.close()

    # 📨 Armar contenido en HTML para el correo
    contenido_correo_html = f"""
    <html>
        <body>
            <p><strong>Área:</strong> {nombre_area}</p>
            <p><strong>Motivo:</strong> {nombre_motivo}</p>
            <hr>
            <p><strong>Mensaje:</strong></p>
            <p>{contenido.replace('\n', '<br>')}</p>
        </body>
    </html>
    """

    enviar_correo(asunto, contenido_correo_html, destinatario)

    flash('Citación registrada y correo enviado correctamente.')
    return redirect(url_for('formulario'))

if __name__ == '__main__':
    app.run(debug=True)
