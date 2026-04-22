
from model.user_CRUD import UserCRUD


class LoginPresenter:
    def __init__(self, view):
        self.view = view
        self.usercrud = UserCRUD()
        self.id = None

    def loginfunc(self, usern, password):
        user = self.usercrud.get_user(usern)
        if user:
            self.id = user[0]
            dbpassword = user[2]
            dbrole = user[3]
            if password==dbpassword:
                self.open_dashboard(dbrole,user)

            else:
                self.view.show_err()
        else:
            self.view.show_err()


    def open_dashboard(self, role, user):
        if role == 1:
            self.view.withdraw()
            from view.admin_view import adminframe
            app = adminframe(user)
            app.mainloop()
        else:
            self.view.withdraw()
            from view.user_view import userframe
            app = userframe(user)
            app.mainloop()


