from model.admin_CRUD import AdminCRUD

class AdminPresenter:
    def __init__(self, view):
        self.view = view
        self.admin_crud = AdminCRUD()

    def get_users(self):
        return self.admin_crud.get_users()

    def get_logs(self):
        return self.admin_crud.get_logs()

    def get_catalog(self):
        return self.admin_crud.get_catalog()

    def get_dropdown(self):
        return self.admin_crud.get_dropdown()

    def get_reestr(self):
        return self.admin_crud.get_reestr()

    def get_roles(self):
        return self.admin_crud.get_roles()

    def close_window(self):
        self.view.withdraw()

    def update_cell(self,table,entry_id,column,new_value):
        self.admin_crud.update_cell(table,entry_id,column,new_value)
        self.view.update_current_table()

    def get_statistics(self):
        return self.admin_crud.get_stat()

    def users_id(self):
        result = self.admin_crud.get_users()
        result = [str(item[0]) for item in result]
        return result

    def delete_record(self, table, record_id):
        self.admin_crud.delete_record(table, record_id)
        self.view.update_current_table()

    def add_user(self, login, password, role, name, second_name, last_name,date, phone):
        self.admin_crud.add_user(login, password, role, name, second_name, last_name,date, phone)