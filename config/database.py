import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()


class Database:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            port=os.getenv('DB_PORT'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME')
        )
        self.cursor = self.connection.cursor(dictionary=True)

    def execute(self, query, params=None):
        self.cursor.execute(query, params or ())
        self.connection.commit()
        return self.cursor

    def fetch_all(self, query, params=None):
        self.cursor.execute(query, params or ())
        return self.cursor.fetchall()

    def fetch_one(self, query, params=None):
        self.cursor.execute(query, params or ())
        return self.cursor.fetchone()

    def __del__(self):
        self.connection.close()