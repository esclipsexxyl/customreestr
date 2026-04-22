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

    def get_stat(self):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM v_menu_stat")
        row = cursor.fetchone()
        if row:
            users_count, roles_count, catalog_count, reestr_count = row
            return {
                'users': users_count,
                'roles': roles_count,
                'catalog': catalog_count,
                'reestr': reestr_count
            }
        return None

