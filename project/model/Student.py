from database.config import db
import mysql.connector as con


class Student:
    def __init__(self):
        self._db = db().con()

    def GetALL(self):
        cursor = self._db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM students")
        students = cursor.fetchall()
        return students

    def GetAll(self, limit, offset):
        cursor = self._db.cursor(dictionary=True)
        query = "SELECT * FROM students LIMIT %s OFFSET %s"
        cursor.execute(query, (limit, offset))
        students = cursor.fetchall()
        return students
    
    def CountAll(self):
        cursor = self._db.cursor()
        cursor.execute("SELECT COUNT(*) FROM students")
        total = cursor.fetchone()[0]
        return total
    
    def Create(self, firstname, lastname, email, gender):
        try:
            cursor = self._db.cursor()
            cursor.execute(
                'INSERT INTO students(firstname, lastname, email, gender) VALUES(%s,%s,%s,%s)',(firstname, lastname, email, gender)
            )
            self._db.commit()
            return True
        except Exception as e:
            print(e)
            return False
        
    def Remove(self,id):
        try:
            cursor = self._db.cursor()
            cursor.execute('DELETE FROM students WHERE id_student = %s',(id,))
            self._db.commit()
            if cursor.rowcount > 0:
                return True
            return False
        except Exception as e:
            print(e)
            return False
        
    def Update(self, id, firstname, lastname, email, gender):
        try:
            cursor = self._db.cursor()
            cursor.execute('UPDATE students SET firstname = %s,lastname = %s,email = %s,gender = %s WHERE id_student = %s',
                (firstname, lastname, email, gender, id)
            )
            self._db.commit()
            if cursor.rowcount > 0:
                return True
            return False
        except Exception as e:
            print(e)
            return False
        
    def Finds(self, content):
        try:
            cursor = self._db.cursor(dictionary=True)
            query = 'SELECT * FROM students WHERE firstname LIKE %s OR lastname LIKE %s OR email LIKE %s OR gender LIKE %s'
            value = f"%{content}%"
            cursor.execute(query, (value, value, value, value))
            students = cursor.fetchall()
            return students
        except Exception as e:
            print(e)
            return False
    
    def Find(self, id):
        try:
            cursor = self._db.cursor(dictionary=True)
            cursor.execute('SELECT * FROM students WHERE id_student = %s',(id,))
            student = cursor.fetchone()
            return student
        except Exception as e:
            print(e)
            return False