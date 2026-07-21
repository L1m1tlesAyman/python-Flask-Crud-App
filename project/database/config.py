import mysql.connector

class db:
    @staticmethod
    def con():
        Con = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'studentsdb'
        )
        return Con