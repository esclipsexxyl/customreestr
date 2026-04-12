import sqlite3

class UserCRUD:
    def __init__(self, db_path="model/customreestr.db"):
        self.db_path = db_path

    def get_user(self, username):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        user = cursor.execute("SELECT * FROM Users WHERE login = ?",(username,)).fetchone()
        connection.close()
        return user

