from model.admin_CRUD import AdminCRUD

class AdminPresenter:
    def __init__(self, view):
        self.view = view
        self.admin_crud = AdminCRUD()

    def get_users(self):
        return self.admin_crud.get_users()

    def close_window(self):
        self.view.withdraw()

    def users_id(self):
        result = self.admin_crud.get_users()
        result = [str(item[0]) for item in result]
        return result