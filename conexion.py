import mysql.connector

def obtener_conexion():
    return mysql.connector.connect(
        host="crossover.proxy.rlwy.net",
        port=27645,
        user="root",
        password="QZfJLpAfqssdkkNaRuvyvIEWQKwkdsrn",
        database="railway"
    )