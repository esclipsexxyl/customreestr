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
        self.title('Реестр закупки оборудования - Авторизация')
        self.configure(fg_color="#f8fafc")
        ctk.set_default_color_theme("blue")
        ctk.set_appearance_mode("light")
        
        # Установка минимального размера и геометрии
        self.minsize(500, 600)
        self.geometry('500x600')
        self.resizable(False, False)
        
        # Основной контейнер
        self.main_container = ctk.CTkFrame(self, fg_color="white", corner_radius=20, border_width=1, border_color="#e2e8f0")
        self.main_container.pack(pady=40, padx=40, fill="both", expand=True)
        
        # Логотип и заголовок
        self.header_frame = ctk.CTkFrame(self.main_container, fg_color="transparent")
        self.header_frame.pack(pady=(30, 20))
        
        try:
            self.logo_img = ctk.CTkImage(Image.open("images/vektorlogo.png"), size=(48, 48))
            self.logo_label = ctk.CTkLabel(self.header_frame, image=self.logo_img, text="", fg_color="transparent")
            self.logo_label.pack()
        except:
            pass
            
        self.labeltitle = ctk.CTkLabel(self.header_frame, text="АВТОРИЗАЦИЯ", text_color="#1e293b", font=("Segoe UI", 28, "bold"))
        self.labeltitle.pack(pady=(15, 5))
        
        self.subtitle = ctk.CTkLabel(self.header_frame, text="Введите ваши учетные данные для входа", text_color="#64748b", font=("Segoe UI", 14))
        self.subtitle.pack()

        # Контейнер для полей ввода
        self.form_container = ctk.CTkFrame(self.main_container, fg_color="transparent")
        self.form_container.pack(pady=20, padx=40, fill="x")
        
        # Поле для логина
        self.login_label = ctk.CTkLabel(self.form_container, text="Логин", text_color="#475569", font=("Segoe UI", 12, "bold"), anchor="w")
        self.login_label.pack(fill="x", pady=(0, 5))
        
        self.login_frame = ctk.CTkFrame(self.form_container, height=45, fg_color="#f1f5f9", border_width=1, border_color="#cbd5e1", corner_radius=10)
        self.login_frame.pack(fill="x", pady=(0, 15))
        self.userimg = ctk.CTkImage(Image.open("images/user.png"), size=(20, 20))
        self.userlabel = ctk.CTkLabel(self.login_frame, image=self.userimg, text="", fg_color="transparent")
        self.userlabel.place(y=12, x=15)
        self.login_entry = ctk.CTkEntry(self.login_frame, placeholder_text="Введите ваш логин", fg_color="transparent", border_width=0, font=("Segoe UI", 14), text_color="#1e293b")
        self.login_entry.place(y=11, x=45, relwidth=0.85)

        # Поле для пароля
        self.password_label = ctk.CTkLabel(self.form_container, text="Пароль", text_color="#475569", font=("Segoe UI", 12, "bold"), anchor="w")
        self.password_label.pack(fill="x", pady=(0, 5))
        
        self.password_frame = ctk.CTkFrame(self.form_container, height=45, fg_color="#f1f5f9", border_width=1, border_color="#cbd5e1", corner_radius=10)
        self.password_frame.pack(fill="x", pady=(0, 25))
        self.lockimg = ctk.CTkImage(Image.open("images/lock.png"), size=(20, 20))
        self.locklabel = ctk.CTkLabel(self.password_frame, image=self.lockimg, text="", fg_color="transparent")
        self.locklabel.place(y=12, x=15)
        self.pass_entry = ctk.CTkEntry(self.password_frame, placeholder_text="Введите ваш пароль", fg_color="transparent", border_width=0, font=("Segoe UI", 14), text_color="#1e293b", show="*")
        self.pass_entry.place(y=11, x=45, relwidth=0.85)


        # Кнопка входа
        self.login_btn = ctk.CTkButton(
            self.main_container, 
            text="Войти в систему", 
            font=("Segoe UI", 16, "bold"), 
            command=self.auth,
            height=45,
            corner_radius=10,
            fg_color="#3b82f6",
            hover_color="#2563eb",
            text_color="white"
        )
        self.login_btn.pack(pady=(10, 20), padx=40, fill="x")
        
        # Привязка событий
        self.pass_entry.bind("<Return>", lambda event: self.auth())
        self.login_entry.bind("<Return>", lambda event: self.pass_entry.focus())
        
        # Центрирование окна после создания всех элементов
        self.center_window()
        
    def center_window(self):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width // 2) - 250  # 500/2
        y = (screen_height // 2) - 200  # 400/2
        self.geometry(f'500x400+{x}+{y}')

    def auth(self):
        login1 = self.login_entry.get()
        login2 = login1.replace(" ", "")
        password = self.pass_entry.get()
        self.presenter.loginfunc(login2,password)

        # Функции вывода сообщений
    def show_err(self):
        box.CTkMessagebox(
            title="Ошибка авторизации", 
            message="Неверный логин или пароль. Попробуйте еще раз.", 
            icon="cancel", 
            font=("Segoe UI", 14),
            fade_in_duration=100, 
            topmost=True,
            button_color="#ef4444", 
            button_hover_color="#dc2626",
            button_text_color="white",
            fg_color="#fef2f2",
            text_color="#991b1b"
        )

    def welcome_msg(self, role):
        box.CTkMessagebox(
            title="Успешный вход", 
            message=f"Добро пожаловать в систему! Ваша роль: {role}", 
            icon="check",
            font=("Segoe UI", 14), 
            fade_in_duration=100, 
            topmost=True,
            button_color="#10b981", 
            button_hover_color="#059669",
            button_text_color="white",
            fg_color="#f0fdf4",
            text_color="#065f46"
        )











