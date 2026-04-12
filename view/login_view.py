#from tkinter import *
import customtkinter as ctk
from PIL import Image
import CTkMessagebox as box
from presenter.login_presenter import  LoginPresenter

class loginframe(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.presenter = LoginPresenter(self)

        # Настройки окна
        self.geometry('450x300')
        self.title('Окно авторизации')
        self.configure(fg_color="#ffffff")
        ctk.set_default_color_theme("blue")
        ctk.set_appearance_mode("light")

        # Текст
        self.labeltitle = ctk.CTkLabel(self,text="АВТОРИЗАЦИЯ",text_color="black", font=("Segoe UI",32,"bold"))
        self.labeltitle.pack(pady=25)

        # Поле для логина
        self.frame = ctk.CTkFrame(self,height=38,width=400, fg_color="#ebebeb",border_width=0,corner_radius=15)
        self.frame.pack(pady=15)
        self.userimg = ctk.CTkImage(Image.open("images/user.png"),size=(32,32))
        self.userlabel = ctk.CTkLabel(self.frame, image=self.userimg,text="",fg_color="transparent")
        self.userlabel.place(y=4,x=10)
        self.login_entry = ctk.CTkEntry(self.frame,width=340,placeholder_text="Введите логин",fg_color="transparent",border_width=0,font=("Segoe UI",18))
        self.login_entry.place(y=4,x=42)

        # Поле для пароля
        self.frame2 = ctk.CTkFrame(self,height=38,width=400, fg_color="#ebebeb",border_width=0,corner_radius=15)
        self.frame2.pack()
        self.lockimg = ctk.CTkImage(Image.open("images/lock.png"),size=(32,32))
        self.locklabel = ctk.CTkLabel(self.frame2, image=self.lockimg,text="",fg_color="transparent")
        self.locklabel.place(y=4,x=10)
        self.pass_entry = ctk.CTkEntry(self.frame2,width=340,placeholder_text="Введите пароль",fg_color="transparent",border_width=0,font=("Segoe UI",18),show="*")
        self.pass_entry.place(y=4,x=42)


        # Кнопка входа
        self.login_btn = ctk.CTkButton(self, text="ВХОД",font=("Segoe UI",18,"bold"),command=self.auth)
        self.login_btn.pack(pady=35)

    def auth(self):
        login1 = self.login_entry.get()
        login2 = login1.replace(" ", "")
        password = self.pass_entry.get()
        self.presenter.loginfunc(login2,password)

        # Функции вывода сообщений
    def show_err(self):
        box.CTkMessagebox(title="Ошибка", message="Неверные данные!", icon="cancel", font=("Arial", 14),
                              fade_in_duration=85, topmost=True,
                              button_color="#f7f7f7", button_hover_color="#bfbfbf",
                              button_text_color="#000000")

    def welcome_msg(self, role):
        box.CTkMessagebox(title="Добро пожаловать", message=f"Добро пожаловать! Ваша роль - {role}", icon="check",
                              font=("Arial", 14), fade_in_duration=85, topmost=True,
                              button_color="#f7f7f7", button_hover_color="#bfbfbf",
                              button_text_color="#000000")











