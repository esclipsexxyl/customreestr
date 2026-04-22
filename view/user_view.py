from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import simpledialog
import customtkinter as ctk
from PIL import Image
import CTkMessagebox as box
from customtkinter import CTkImage
from datetime import datetime

from presenter.user_presenter import UserPresenter


class userframe(ctk.CTkToplevel):
    def __init__(self, user):
        super().__init__()
        self.presenter = UserPresenter(self)
        self.userssum = 0
        self.rolessum = 0
        self.catalogsum = 0
        self.reestrsum = 0
        self.login = user[1]
        self.name1 = user[4]
        self.name2 = user[5]
        self.name3 = user[6]
        self.now = datetime.now()

        # Настройки окна
        self.title('Реестр закупки оборудования')
        self.configure(fg_color="#f8fafc")
        ctk.set_default_color_theme("blue")
        ctk.set_appearance_mode("light")

        # Установка минимального размера и геометрии
        self.minsize(1600, 1000)
        self.geometry('1600x1000')
        # self.attributes('-fullscreen', True)

        # Навигация
        self.nav_frame = ctk.CTkFrame(self, fg_color="white", width=280, corner_radius=0, border_width=1,
                                      border_color="#e2e8f0")
        self.nav_frame.pack(side='left', fill='y')
        self.nav_frame.pack_propagate(False)

        # Логотип и заголовок в навигации
        self.nav_header = ctk.CTkFrame(self.nav_frame, fg_color="#3b82f6", height=80, corner_radius=0)
        self.nav_header.pack(fill='x')
        self.nav_header.pack_propagate(False)

        try:
            self.nav_logo = ctk.CTkImage(Image.open("images/vektorlogo.png"), size=(32, 32))
            self.nav_logo_label = ctk.CTkLabel(self.nav_header, image=self.nav_logo, text="", fg_color="transparent")
            self.nav_logo_label.place(y=24, x=20)
        except:
            pass

        self.nav_title = ctk.CTkLabel(self.nav_header, text="Рабочее пространство", font=("Segoe UI", 18, "bold"),
                                      text_color="white")
        self.nav_title.place(y=28, x=60)

        # Вкладки
        self.menu_btn = ctk.CTkButton(
            self.nav_frame,
            text='📊 Главное меню',
            border_width=0,
            fg_color="#3b82f6",
            text_color="white",
            hover_color="#2563eb",
            anchor="w",
            font=("Segoe UI", 14, "bold"),
            height=45,
            corner_radius=8,
            command=lambda: self.change_nav("menu")
        )
        self.menu_btn.pack(pady=(20, 5), padx=15, fill='x')

        self.addreestr_btn = ctk.CTkButton(
            self.nav_frame,
            text='➕ Добавить новую запись',
            border_width=0,
            fg_color="transparent",
            text_color="#64748b",
            hover_color="#f1f5f9",
            anchor="w",
            font=("Segoe UI", 14),
            height=40,
            corner_radius=8,
            command=lambda: self.change_nav("menu")
        )
        self.addreestr_btn.pack(pady=2, padx=15, fill='x')

        self.reestr_btn = ctk.CTkButton(
            self.nav_frame,
            text='📝 Реестр',
            border_width=0,
            fg_color="transparent",
            text_color="#64748b",
            hover_color="#f1f5f9",
            anchor="w",
            font=("Segoe UI", 14),
            height=40,
            corner_radius=8,
            command=lambda: self.change_nav("menu")
        )
        self.reestr_btn.pack(pady=2, padx=15, fill='x')


        self.catalog_btn = ctk.CTkButton(
            self.nav_frame,
            text='📋 Справочник',
            border_width=0,
            fg_color="transparent",
            text_color="#64748b",
            hover_color="#f1f5f9",
            anchor="w",
            font=("Segoe UI", 14),
            height=40,
            corner_radius=8,
            command=lambda: self.change_nav("menu")
        )
        self.catalog_btn.pack(pady=2, padx=15, fill='x')

        self.dropdown_btn = ctk.CTkButton(
            self.nav_frame,
            text="📄 Выпадающие списки",
            border_width=0,
            fg_color="transparent",
            text_color="#64748b",
            hover_color="#f1f5f9",
            anchor="w",
            font=("Segoe UI", 14),
            height=40,
            corner_radius=8,
            command=lambda: self.change_nav("menu")
        )
        self.dropdown_btn.pack(pady=2, padx=15, fill="x")
        # Информация о пользователе
        self.infoframe = ctk.CTkFrame(
            self.nav_frame,
            height=60,
            fg_color="#f8fafc",
            border_width=1,
            border_color="#e2e8f0",
            corner_radius=12
        )
        self.infoframe.place(x=15, y=920, relwidth=0.9)
        self.infoimg = ctk.CTkImage(Image.open("images/user.png"), size=(24, 24))
        self.infolabel = ctk.CTkLabel(self.infoframe, image=self.infoimg, text="", fg_color="transparent")
        self.infolabel.place(y=18, x=12)
        self.infolabel2 = ctk.CTkLabel(
            self.infoframe,
            fg_color="transparent",
            text_color="#475569",
            text=f"{self.login}",
            font=("Segoe UI", 12, "bold")
        )
        self.infolabel2.place(y=12, x=45)
        self.role_label = ctk.CTkLabel(
            self.infoframe,
            fg_color="transparent",
            text_color="#64748b",
            text="Пользователь",
            font=("Segoe UI", 10)
        )
        self.role_label.place(y=30, x=45)

        # Основной фрейм
        self.main_frame = ctk.CTkFrame(self, fg_color="#f8fafc")
        self.main_frame.pack(side='right', expand=True, fill='both')

        # Фрейм заголовок
        self.title_frame = ctk.CTkFrame(
            self.main_frame,
            fg_color="white",
            height=70,
            corner_radius=0,
            border_width=1,
            border_color="#e2e8f0"
        )
        self.title_frame.pack(side='top', fill='x')
        self.title_frame.pack_propagate(False)

        # Заголовок и логотип
        self.header_container = ctk.CTkFrame(self.title_frame, fg_color="transparent")
        self.header_container.place(relx=0.5, rely=0.5, anchor="center")

        try:
            self.vektorlogo = ctk.CTkImage(Image.open("images/vektorlogo.png"), size=(32, 32))
            self.vektorlabel = ctk.CTkLabel(self.header_container, image=self.vektorlogo, text="",
                                            fg_color="transparent")
            self.vektorlabel.pack(side="left", padx=(0, 10))
        except:
            pass

        self.title_label = ctk.CTkLabel(
            self.header_container,
            text="Реестр закупки оборудования",
            font=("Segoe UI", 24, "bold"),
            text_color="#1e293b"
        )
        self.title_label.pack(side="left")

        # Время
        self.timelabel = ctk.CTkLabel(
            self.title_frame,
            text=f"{self.now.strftime("%d.%m.%Y %H:%M")}",
            fg_color="transparent",
            text_color="#64748b",
            font=("Segoe UI", 14)
        )
        self.timelabel.place(relx=0.98, rely=0.5, anchor="e")


        self.update_time()

        # Центрирование окна после создания всех элементов
        self.center_window()

        self.show_menu()

    def update_time(self):
        self.now = datetime.now()
        self.timelabel.configure(text=f"{self.now.strftime('%H:%M')} | {self.now.strftime('%d.%m.%Y')}")
        self.after(1000, self.update_time)

    def center_window(self):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width // 2) - 800  # 1600/2
        y = (screen_height // 2) - 500  # 1000/2
        self.geometry(f'1600x1000+{x}+{y}')

    def change_nav(self, name):
        buttons = {
            "menu": self.menu_btn,
            "add_reestr": self.addreestr_btn,
            "catalog": self.catalog_btn,
            "reestr": self.reestr_btn,
            "dropdown": self.dropdown_btn
        }

        # Сбрасываем все кнопки
        for btn_name, btn in buttons.items():
            btn.configure(
                fg_color="transparent",
                hover_color="#f1f5f9",
                font=("Segoe UI", 14),
                text_color="#64748b"
            )

        # Подсвечиваем активную кнопку
        if name in buttons:
            buttons[name].configure(
                fg_color="#3b82f6",
                hover_color="#2563eb",
                font=("Segoe UI", 14, "bold"),
                text_color="white"
            )


        match name:
            case "catalog":
                self.show_catalog()
            case "reestr":
                self.show_reestr()
            case "dropdown":
                self.show_dropdown()
            case "menu":
                self.show_menu()
            case "add_reestr":
                self.show_addreestr()

    def clear_main_frame(self):
        for widget in self.main_frame.winfo_children():
                if widget != self.title_frame:
                    widget.destroy()
            # widget.destroy()

    def show_menu(self):
        self.clear_main_frame()

        # Get user info and statistics
        try:
            print(self.name1)
            if self.name1!="None":
                full_name = f"{self.name1} {self.name2} {self.name3}"
            else: full_name = self.login
            #full_name = f"{user[4]} {user_info[5]} {user_info[6]}" if user_info else self.login
        except:
            full_name = self.login
        
        stats = self.presenter.get_statistics()

        # Greeting
        greeting_frame = ctk.CTkFrame(self.main_frame, fg_color="white", corner_radius=12, height=80)
        greeting_frame.pack(fill="x", padx=20, pady=(20, 10))
        greeting_frame.pack_propagate(False)

        greeting_label = ctk.CTkLabel(
            greeting_frame,
            text=f"Добро пожаловать, {full_name}!",
            font=("Segoe UI", 24, "bold"),
            text_color="#1e293b",
            fg_color="transparent"
        )
        greeting_label.place(relx=0.5, rely=0.5, anchor="center")

        # Заголовок
        menu_title = ctk.CTkLabel(
            self.main_frame,
            text="📊 Статистика системы",
            font=("Segoe UI", 20, "bold"),
            text_color="#1e293b"
        )
        menu_title.pack(pady=(10, 20))

        # Контейнер для карточек
        cards_container = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        cards_container.pack(expand=True, fill="both", padx=40, pady=20)

        # Карточки статистики - только справочник и реестр
        self.stat_frame1 = ctk.CTkFrame(
            cards_container,
            height=200,
            width=280,
            corner_radius=16,
            fg_color="white",
            border_width=2,
            border_color="#f59e0b"
        )
        self.stat_frame1.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        self.stat_frame2 = ctk.CTkFrame(
            cards_container,
            height=200,
            width=280,
            corner_radius=16,
            fg_color="white",
            border_width=2,
            border_color="#ef4444"
        )
        self.stat_frame2.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

        # Настройка весов для сетки
        cards_container.grid_columnconfigure(0, weight=1)
        cards_container.grid_columnconfigure(1, weight=1)
        cards_container.grid_rowconfigure(0, weight=1)

        # Иконки и значения для карточек с реальными данными - только справочник и реестр
        self.create_stat_card(self.stat_frame1, "📋", "Справочник", str(stats['catalog']), "#f59e0b")
        self.create_stat_card(self.stat_frame2, "📝", "Реестр", str(stats['reestr']), "#ef4444")

    def create_stat_card(self, parent, icon, title, value, color):
        # Иконка
        icon_label = ctk.CTkLabel(
            parent,
            text=icon,
            font=("Segoe UI", 36),
            text_color=color,
            fg_color="transparent"
        )
        icon_label.place(relx=0.5, rely=0.25, anchor="center")

        # Значение
        value_label = ctk.CTkLabel(
            parent,
            text=value,
            font=("Segoe UI", 32, "bold"),
            text_color="#1e293b",
            fg_color="transparent"
        )
        value_label.place(relx=0.5, rely=0.5, anchor="center")

        # Заголовок
        title_label = ctk.CTkLabel(
            parent,
            text=title,
            font=("Segoe UI", 14),
            text_color="#64748b",
            fg_color="transparent"
        )
        title_label.place(relx=0.5, rely=0.75, anchor="center")

