import sqlite3

class AdminCRUD:
    def __init__(self, db_path="model/customreestr.db"):
        self.db_path = db_path

    def get_users(self):
        connection=sqlite3.connect(self.db_path)
        cursor=connection.cursor()
        cursor.execute("SELECT * FROM Users")
        result=cursor.fetchall()
        connection.close()
        return result

    def get_roles(self):
        connection=sqlite3.connect(self.db_path)
        cursor=connection.cursor()
        cursor.execute("SELECT * FROM Roles")
        result=cursor.fetchall()
        connection.close()
        return result

    def get_logs(self):
        connection=sqlite3.connect(self.db_path)
        cursor=connection.cursor()
        cursor.execute("SELECT * FROM Logs")
        result=cursor.fetchall()
        connection.close()
        return result

    def get_catalog(self):
        connection=sqlite3.connect(self.db_path)
        cursor=connection.cursor()
        cursor.execute("SELECT * FROM Price_catalog")
        result=cursor.fetchall()
        connection.close()
        return result

    def get_dropdown(self):
        connection=sqlite3.connect(self.db_path)
        cursor=connection.cursor()
        cursor.execute("SELECT * FROM Dropdown_values")
        result=cursor.fetchall()
        connection.close()
        return result

    def get_reestr(self):
        connection=sqlite3.connect(self.db_path)
        cursor=connection.cursor()
        cursor.execute("SELECT * FROM Procurement")
        result=cursor.fetchall()
        connection.close()
        return result

    def get_stat(self):
        connection=sqlite3.connect(self.db_path)
        cursor=connection.cursor()
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

    def update_cell(self,table,entry_id,column,new_value):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        cursor.execute(f"UPDATE {table} SET {column} = ? WHERE id = ?",(new_value,entry_id))
        connection.commit()
        connection.close()