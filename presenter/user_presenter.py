from model.user_CRUD import UserCRUD

class UserPresenter:
    def __init__(self, view):
        self.view = view
        self.user_crud = UserCRUD()

    def get_statistics(self):
        return self.user_crud.get_stat()

