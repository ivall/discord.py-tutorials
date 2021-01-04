import mysql.connector
from config import *


class Database:
    def __init__(self):
        self._conn = mysql.connector.connect(user=user, password=password, host=host, database=database)
        self._cursor = self._conn.cursor(buffered=True)

    @property
    def connection(self):
        return self._conn

    @property
    def cursor(self):
        return self._cursor

    def execute(self, sql, params=None):
        self._cursor.execute(sql, params)
        self._conn.commit()
        return self._cursor.fetchone()
