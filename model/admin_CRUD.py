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

    def update_cell(self,table,entry_id,column,new_value):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        cursor.execute(f"UPDATE {table} SET {column} = ? WHERE id = ?",(new_value,entry_id))
        connection.commit()
        connection.close()