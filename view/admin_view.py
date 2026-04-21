from tkinter import *
import tkinter.ttk as ttk
from tkinter import simpledialog
import customtkinter as ctk
from PIL import Image
import CTkMessagebox as box
from customtkinter import CTkImage
from datetime import datetime


from presenter.admin_presenter import  AdminPresenter

class adminframe(ctk.CTkToplevel):
    def __init__(self,user):
        super().__init__()
        self.presenter = AdminPresenter(self)
        self.userssum=0
        self.rolessum=0
        self.catalogsum=0
        self.reestrsum=0
        self.login=user[1]
        self.now = datetime.now()

        # Настройки окна
        self.title('Реестр закупки оборудования - Панель администратора')
        self.configure(fg_color="#f8fafc")
        ctk.set_default_color_theme("blue")
        ctk.set_appearance_mode("light")
        
        # Установка минимального размера и геометрии
        self.minsize(1600, 1000)
        self.geometry('1600x1000')
        #self.attributes('-fullscreen', True)
        
        # Навигация
        self.nav_frame=ctk.CTkFrame(self, fg_color="white", width=280, corner_radius=0, border_width=1, border_color="#e2e8f0")
        self.nav_frame.pack(side='left',fill='y')
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
            
        self.nav_title = ctk.CTkLabel(self.nav_header, text="Админ панель", font=("Segoe UI", 18, "bold"), text_color="white")
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
            command=lambda:self.change_nav("menu")
        )
        self.menu_btn.pack(pady=(20, 5), padx=15, fill='x')
        
        self.users_btn = ctk.CTkButton(
            self.nav_frame,
            text='👥 Пользователи', 
            border_width=0,
            fg_color="transparent",
            text_color="#64748b",
            hover_color="#f1f5f9",
            anchor="w",
            font=("Segoe UI", 14),
            height=40,
            corner_radius=8,
            command=lambda:self.change_nav("users")
        )
        self.users_btn.pack(pady=2, padx=15, fill='x')
        
        self.roles_btn = ctk.CTkButton(
            self.nav_frame,
            text='👤 Роли', 
            border_width=0,
            fg_color="transparent",
            text_color="#64748b",
            hover_color="#f1f5f9",
            anchor="w",
            font=("Segoe UI", 14),
            height=40,
            corner_radius=8,
            command=lambda:self.change_nav("roles")
        )
        self.roles_btn.pack(pady=2, padx=15, fill='x')
        
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
            command=lambda:self.change_nav("catalog")
        )
        self.catalog_btn.pack(pady=2, padx=15, fill='x')
        
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
            command=lambda:self.change_nav("reestr")
        )
        self.reestr_btn.pack(pady=2, padx=15, fill='x')
        
        self.logs_btn = ctk.CTkButton(
            self.nav_frame,
            text='📄 Логи', 
            border_width=0,
            fg_color="transparent",
            text_color="#64748b",
            hover_color="#f1f5f9",
            anchor="w",
            font=("Segoe UI", 14),
            height=40,
            corner_radius=8,
            command=lambda:self.change_nav("logs")
        )
        self.logs_btn.pack(pady=2, padx=15, fill='x')
        self.dropdown_btn = ctk.CTkButton(
            self.nav_frame,
            text="📄 Выпадающие списки",
            border_width = 0,
            fg_color ="transparent",
            text_color ="#64748b",
            hover_color ="#f1f5f9",
            anchor ="w",
            font = ("Segoe UI", 14),
                height=40,
                corner_radius=8,
                command= lambda:self.change_nav("dropdown")
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
            text="Администратор",
            font=("Segoe UI", 10)
        )
        self.role_label.place(y=30, x=45)

        # Основной фрейм
        self.main_frame = ctk.CTkFrame(self, fg_color="#f8fafc")
        self.main_frame.pack(side='right',expand=True,fill='both')

        # Фрейм заголовок
        self.title_frame = ctk.CTkFrame(
            self.main_frame,
            fg_color="white",
            height=70,
            corner_radius=0,
            border_width=1,
            border_color="#e2e8f0"
        )
        self.title_frame.pack(side='top',fill='x')
        self.title_frame.pack_propagate(False)
        
        # Заголовок и логотип
        self.header_container = ctk.CTkFrame(self.title_frame, fg_color="transparent")
        self.header_container.place(relx=0.5, rely=0.5, anchor="center")
        
        try:
            self.vektorlogo = ctk.CTkImage(Image.open("images/vektorlogo.png"), size=(32, 32))
            self.vektorlabel = ctk.CTkLabel(self.header_container, image=self.vektorlogo, text="", fg_color="transparent")
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

        # Фрейм кнопок действий
        self.action_frame=ctk.CTkFrame(
            self.main_frame,
            fg_color="white",
            height=60,
            corner_radius=12,
            border_width=1,
            border_color="#e2e8f0"
        )
        self.action_frame.pack(side="bottom",fill="x", padx=20, pady=10)
        self.action_frame.pack_propagate(False)
        
        self.add_btn = ctk.CTkButton(
            self.action_frame,
            text="➕ Добавить",
            font=("Segoe UI", 12, "bold"),
            fg_color="#10b981",
            hover_color="#059669",
            text_color="white",
            height=40,
            corner_radius=8,
            width=120
        )
        self.add_btn.pack(side="left", padx=15, pady=10)
        
        self.delete_btn = ctk.CTkButton(
            self.action_frame,
            text="🗑️ Удалить",
            font=("Segoe UI", 12, "bold"),
            fg_color="#ef4444",
            hover_color="#dc2626",
            text_color="white",
            height=40,
            corner_radius=8,
            width=120
        )
        self.delete_btn.pack(side="left", padx=5, pady=10)
        
        self.update_btn = ctk.CTkButton(
            self.action_frame,
            text="🔄 Обновить",
            font=("Segoe UI", 12, "bold"),
            fg_color="#3b82f6",
            hover_color="#2563eb",
            text_color="white",
            height=40,
            corner_radius=8,
            width=120,
            command=self.update_current_table
        )
        self.update_btn.pack(side="left", padx=5, pady=10)

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
    
    def change_nav(self,name):
        buttons = {
            "menu": self.menu_btn,
            "users": self.users_btn,
            "roles": self.roles_btn,
            "catalog": self.catalog_btn,
            "reestr": self.reestr_btn,
            "logs": self.logs_btn,
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
            case "users":
                self.show_users()
            case "roles":
                self.show_roles()
            case "catalog":
                self.show_catalog()
            case "reestr":
                self.show_reestr()
            case "logs":
                self.show_logs()
            case "dropdown":
                self.show_dropdown()
            case "menu":
                self.show_menu()
            case "dropdown":
                self.show_dropdown()

    def clear_main_frame(self):
        for widget in self.main_frame.winfo_children():
            if widget != self.action_frame:
                if widget != self.title_frame:
                    widget.destroy()
               #widget.destroy()

    def show_menu(self):
        self.clear_main_frame()
        
        # Получаем реальные данные из базы через presenter
        stats = self.presenter.get_statistics()
        
        # Заголовок
        menu_title = ctk.CTkLabel(
            self.main_frame,
            text="📊 Статистика системы",
            font=("Segoe UI", 20, "bold"),
            text_color="#1e293b"
        )
        menu_title.pack(pady=(30, 20))
        
        # Контейнер для карточек
        cards_container = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        cards_container.pack(expand=True, fill="both", padx=40, pady=20)
        
        # Карточки статистики
        self.stat_frame1 = ctk.CTkFrame(
            cards_container, 
            height=200,
            width=280,
            corner_radius=16,
            fg_color="white",
            border_width=2,
            border_color="#3b82f6"
        )
        self.stat_frame1.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        
        self.stat_frame2 = ctk.CTkFrame(
            cards_container, 
            height=200,
            width=280,
            corner_radius=16,
            fg_color="white",
            border_width=2,
            border_color="#10b981"
        )
        self.stat_frame2.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
        
        self.stat_frame3 = ctk.CTkFrame(
            cards_container, 
            height=200,
            width=280,
            corner_radius=16,
            fg_color="white",
            border_width=2,
            border_color="#f59e0b"
        )
        self.stat_frame3.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")
        
        self.stat_frame4 = ctk.CTkFrame(
            cards_container, 
            height=200,
            width=280,
            corner_radius=16,
            fg_color="white",
            border_width=2,
            border_color="#ef4444"
        )
        self.stat_frame4.grid(row=1, column=1, padx=20, pady=20, sticky="nsew")
        
        # Настройка весов для сетки
        cards_container.grid_columnconfigure(0, weight=1)
        cards_container.grid_columnconfigure(1, weight=1)
        cards_container.grid_rowconfigure(0, weight=1)
        cards_container.grid_rowconfigure(1, weight=1)
        
        # Иконки и значения для карточек с реальными данными
        self.create_stat_card(self.stat_frame1, "👥", "Пользователи", str(stats['users']), "#3b82f6")
        self.create_stat_card(self.stat_frame2, "👤", "Роли", str(stats['roles']), "#10b981")
        self.create_stat_card(self.stat_frame3, "📋", "Справочник", str(stats['catalog']), "#f59e0b")
        self.create_stat_card(self.stat_frame4, "📝", "Реестр", str(stats['reestr']), "#ef4444")
        
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


    def show_users (self):
        """Вызывает загрузку пользователей и оторбражает их"""
        self.current_table = 'users'
        self.clear_main_frame()
        
        # Заголовок таблицы
        table_header = ctk.CTkFrame(self.main_frame, fg_color="white", corner_radius=12, height=60)
        table_header.pack(fill="x", padx=20, pady=(20, 10))
        table_header.pack_propagate(False)
        
        header_label = ctk.CTkLabel(
            table_header,
            text="👥 Список пользователей",
            font=("Segoe UI", 18, "bold"),
            text_color="#1e293b",
            fg_color="transparent"
        )
        header_label.place(relx=0.5, rely=0.5, anchor="center")
        
        # Контейнер для таблицы
        table_container = ctk.CTkFrame(self.main_frame, fg_color="white", corner_radius=12)
        table_container.pack(fill="both", expand=True, padx=20, pady=(0, 10))
        
        # Стилизованная таблица
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview", 
                       background="white",
                       foreground="#1e293b",
                       fieldbackground="white",
                       borderwidth=0,
                       font=("Segoe UI", 11))
        style.configure("Treeview.Heading", 
                       background="#f8fafc",
                       foreground="#475569",
                       font=("Segoe UI", 12, "bold"),
                       relief="flat")
        style.map("Treeview", 
                 background=[('selected', '#dbeafe')],
                 foreground=[('selected', '#1e40af')])
        
        self.tree = ttk.Treeview(
            table_container,
            columns=("ID","Логин","Пароль","Роль","Имя","Фамилия","Отчество","Дата регистрации"),
            show="headings",
            height=15
        )
        self.tree.heading("ID",text="ID",anchor="c")
        self.tree.column("ID",width=60,anchor="c")

        self.tree.heading("Логин",text="Логин",anchor="c")
        self.tree.column("Логин",width=150,anchor="c")

        self.tree.heading("Пароль", text="Пароль", anchor="c")
        self.tree.column("Пароль", width=120, anchor="c")

        self.tree.heading("Роль", text="Роль", anchor="c")
        self.tree.column("Роль", width=100, anchor="c")

        self.tree.heading("Имя", text="Имя", anchor="c")
        self.tree.column("Имя", width=100, anchor="c")

        self.tree.heading("Фамилия", text="Фамилия", anchor="c")
        self.tree.column("Фамилия", width=120, anchor="c")

        self.tree.heading("Отчество", text="Отчество", anchor="c")
        self.tree.column("Отчество", width=120, anchor="c")

        self.tree.heading("Дата регистрации", text="Дата регистрации", anchor="c")
        self.tree.column("Дата регистрации", width=150, anchor="c")

        self.column_mapping = {
            'ID': 'id',
            'Логин': 'login',
            'Пароль': 'password',
            'Роль': 'role',
            'Имя':'name',
            'Фамилия': 'second_name',
            'Отчество': 'last_name',
            'Дата регистрации': 'created_at'
        }

        self.tree.pack(expand=True,fill="both", padx=10, pady=10)
        self.tree.bind("<Double-1>", self.on_cell_double_click)


        #Получаем данные из презентера
        users=self.presenter.get_users()
        #Отображаем данные
        self.show_users_data(users)

    def show_users_data(self,users):
        """"Отобржает список пользователей в таблице"""""
        self.tree.delete(*self.tree.get_children()) #Удалить все элементы таблицу
        print(users)
        for row in users: #Пройти по всем пользователям
            self.tree.insert("","end",values=row) #в корневую таблицу добавить запись в конец

    def show_roles(self):
        """Shows roles table"""
        self.current_table = 'roles'
        self.clear_main_frame()

        # Table header
        table_header = ctk.CTkFrame(self.main_frame, fg_color="white", corner_radius=12, height=60)
        table_header.pack(fill="x", padx=20, pady=(20, 10))
        table_header.pack_propagate(False)

        header_label = ctk.CTkLabel(
            table_header,
            text="Роли пользователей",
            font=("Segoe UI", 18, "bold"),
            text_color="#1e293b",
            fg_color="transparent"
        )
        header_label.place(relx=0.5, rely=0.5, anchor="center")

        # Table container
        table_container = ctk.CTkFrame(self.main_frame, fg_color="white", corner_radius=12)
        table_container.pack(fill="both", expand=True, padx=20, pady=(0, 10))

        # Styled table
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview",
                        background="white",
                        foreground="#1e293b",
                        fieldbackground="white",
                        borderwidth=0,
                        font=("Segoe UI", 11))
        style.configure("Treeview.Heading",
                        background="#f8fafc",
                        foreground="#475569",
                        font=("Segoe UI", 12, "bold"),
                        relief="flat")
        style.map("Treeview",
                  background=[('selected', '#dbeafe')],
                  foreground=[('selected', '#1e40af')])

        # Treeview with Roles table columns (ID and Name only)
        self.tree = ttk.Treeview(
            table_container,
            columns=("ID", "Name"),
            show="headings",
            height=15
        )

        self.tree.heading("ID", text="ID", anchor="c")
        self.tree.column("ID", width=80, anchor="c")
        self.tree.heading("Name", text="Название роли", anchor="w")
        self.tree.column("Name", width=250, anchor="w")

        self.column_mapping = {
            'ID': 'id',
            'Name': 'name'
        }

        self.tree.pack(expand=True, fill="both", padx=10, pady=10)
        self.tree.bind("<Double-1>", self.on_cell_double_click)

        # Get data from presenter
        roles = self.presenter.get_roles()
        self.show_roles_data(roles)

    def show_roles_data(self, roles):
        """Displays roles data in table"""
        self.tree.delete(*self.tree.get_children())
        for row in roles:
            self.tree.insert("", "end", values=row)
    def show_reestr(self):
        """Shows procurement (реестр) table"""
        self.current_table = 'reestr'
        self.clear_main_frame()

        # Table header
        table_header = ctk.CTkFrame(self.main_frame, fg_color="white", corner_radius=12, height=60)
        table_header.pack(fill="x", padx=20, pady=(20, 10))
        table_header.pack_propagate(False)

        header_label = ctk.CTkLabel(
            table_header,
            text="Реестр закупок",
            font=("Segoe UI", 18, "bold"),
            text_color="#1e293b",
            fg_color="transparent"
        )
        header_label.place(relx=0.5, rely=0.5, anchor="center")

        # Table container
        table_container = ctk.CTkFrame(self.main_frame, fg_color="white", corner_radius=12)
        table_container.pack(fill="both", expand=True, padx=20, pady=(0, 10))

        # Styled table
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview",
                        background="white",
                        foreground="#1e293b",
                        fieldbackground="white",
                        borderwidth=0,
                        font=("Segoe UI", 11))
        style.configure("Treeview.Heading",
                        background="#f8fafc",
                        foreground="#475569",
                        font=("Segoe UI", 12, "bold"),
                        relief="flat")
        style.map("Treeview",
                  background=[('selected', '#dbeafe')],
                  foreground=[('selected', '#1e40af')])

        # Simplified treeview with only ID column (заглушка)
        self.tree = ttk.Treeview(
            table_container,
            columns=("ID",),
            show="headings",
            height=15
        )

        self.tree.heading("ID", text="ID", anchor="c")
        self.tree.column("ID", width=100, anchor="c")

        self.column_mapping = {
            'ID': 'id'
        }

        self.tree.pack(expand=True, fill="both", padx=10, pady=10)
        self.tree.bind("<Double-1>", self.on_cell_double_click)

        # Get data from presenter
        reestr = self.presenter.get_reestr()
        self.show_reestr_data(reestr)

    def show_reestr_data(self, reestr):
        """Displays procurement data in table"""
        self.tree.delete(*self.tree.get_children())
        for row in reestr:
            # Если row - это кортеж или список, берем первый элемент (ID)
            if isinstance(row, (tuple, list)):
                self.tree.insert("", "end", values=(row[0],))
            else:
                self.tree.insert("", "end", values=(row,))
    def show_catalog(self):
        """Shows price catalog table"""
        self.current_table = 'catalog'
        self.clear_main_frame()

        # Table header
        table_header = ctk.CTkFrame(self.main_frame, fg_color="white", corner_radius=12, height=60)
        table_header.pack(fill="x", padx=20, pady=(20, 10))
        table_header.pack_propagate(False)

        header_label = ctk.CTkLabel(
            table_header,
            text="Прайс-каталог",
            font=("Segoe UI", 18, "bold"),
            text_color="#1e293b",
            fg_color="transparent"
        )
        header_label.place(relx=0.5, rely=0.5, anchor="center")

        # Table container
        table_container = ctk.CTkFrame(self.main_frame, fg_color="white", corner_radius=12)
        table_container.pack(fill="both", expand=True, padx=20, pady=(0, 10))

        # Styled table
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview",
                        background="white",
                        foreground="#1e293b",
                        fieldbackground="white",
                        borderwidth=0,
                        font=("Segoe UI", 11))
        style.configure("Treeview.Heading",
                        background="#f8fafc",
                        foreground="#475569",
                        font=("Segoe UI", 12, "bold"),
                        relief="flat")
        style.map("Treeview",
                  background=[('selected', '#dbeafe')],
                  foreground=[('selected', '#1e40af')])

        # Treeview with all Price_catalog columns
        self.tree = ttk.Treeview(
            table_container,
            columns=("ID", "Name", "Unit Price", "Description", "Category", "Last Updated"),
            show="headings",
            height=15
        )

        self.tree.heading("ID", text="ID", anchor="c")
        self.tree.column("ID", width=60, anchor="c")

        self.tree.heading("Name", text="Наименование", anchor="w")
        self.tree.column("Name", width=200, anchor="w")

        self.tree.heading("Unit Price", text="Цена за ед.", anchor="e")
        self.tree.column("Unit Price", width=120, anchor="e")

        self.tree.heading("Description", text="Описание", anchor="w")
        self.tree.column("Description", width=300, anchor="w")

        self.tree.heading("Category", text="Категория", anchor="w")
        self.tree.column("Category", width=150, anchor="w")

        self.tree.heading("Last Updated", text="Последнее обновление", anchor="c")
        self.tree.column("Last Updated", width=150, anchor="c")

        self.column_mapping = {
            'ID': 'id',
            'Name': 'name',
            'Unit Price': 'unit_price',
            'Description': 'description',
            'Category': 'category',
            'Last Updated': 'last_updated'
        }

        self.tree.pack(expand=True, fill="both", padx=10, pady=10)
        self.tree.bind("<Double-1>", self.on_cell_double_click)

        # Get data from presenter
        catalog = self.presenter.get_catalog()
        self.show_catalog_data(catalog)

    def show_catalog_data(self, catalog):
        """Displays price catalog data in table"""
        self.tree.delete(*self.tree.get_children())
        for row in catalog:
            self.tree.insert("", "end", values=row)
    def show_logs(self):
        """Shows logs table"""
        self.current_table = 'logs'
        self.clear_main_frame()

        # Table header
        table_header = ctk.CTkFrame(self.main_frame, fg_color="white", corner_radius=12, height=60)
        table_header.pack(fill="x", padx=20, pady=(20, 10))
        table_header.pack_propagate(False)

        header_label = ctk.CTkLabel(
            table_header,
            text="Журнал событий",
            font=("Segoe UI", 18, "bold"),
            text_color="#1e293b",
            fg_color="transparent"
        )
        header_label.place(relx=0.5, rely=0.5, anchor="center")

        # Table container
        table_container = ctk.CTkFrame(self.main_frame, fg_color="white", corner_radius=12)
        table_container.pack(fill="both", expand=True, padx=20, pady=(0, 10))

        # Styled table
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview",
                        background="white",
                        foreground="#1e293b",
                        fieldbackground="white",
                        borderwidth=0,
                        font=("Segoe UI", 11))
        style.configure("Treeview.Heading",
                        background="#f8fafc",
                        foreground="#475569",
                        font=("Segoe UI", 12, "bold"),
                        relief="flat")
        style.map("Treeview",
                  background=[('selected', '#dbeafe')],
                  foreground=[('selected', '#1e40af')])

        self.tree = ttk.Treeview(
            table_container,
            columns=("ID", "User", "Action", "Date"),
            show="headings",
            height=15
        )

        self.tree.heading("ID", text="ID", anchor="c")
        self.tree.column("ID", width=60, anchor="c")
        self.tree.heading("User", text="Пользователь", anchor="c")
        self.tree.column("User", width=150, anchor="c")
        self.tree.heading("Action", text="Действие", anchor="c")
        self.tree.column("Action", width=150, anchor="c")
        self.tree.heading("Date", text="Дата", anchor="c")
        self.tree.column("Date", width=150, anchor="c")

        self.column_mapping = {
            'ID': 'id',
            'User': 'user',
            'Action': 'action',
            'Date': 'date'
        }

        self.tree.pack(expand=True, fill="both", padx=10, pady=10)
        self.tree.bind("<Double-1>", self.on_cell_double_click)

        # Get data from presenter
        logs = self.presenter.get_logs()
        self.show_logs_data(logs)

    def show_logs_data(self, logs):
        """Displays logs data in table"""
        self.tree.delete(*self.tree.get_children())
        for row in logs:
            self.tree.insert("", "end", values=row)
    def show_dropdown(self):
        """Shows dropdown values table"""
        self.current_table = 'dropdown'
        self.clear_main_frame()

        # Table header
        table_header = ctk.CTkFrame(self.main_frame, fg_color="white", corner_radius=12, height=60)
        table_header.pack(fill="x", padx=20, pady=(20, 10))
        table_header.pack_propagate(False)

        header_label = ctk.CTkLabel(
            table_header,
            text="Выпадающие списки",
            font=("Segoe UI", 18, "bold"),
            text_color="#1e293b",
            fg_color="transparent"
        )
        header_label.place(relx=0.5, rely=0.5, anchor="center")

        # Table container
        table_container = ctk.CTkFrame(self.main_frame, fg_color="white", corner_radius=12)
        table_container.pack(fill="both", expand=True, padx=20, pady=(0, 10))

        # Styled table
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview",
                        background="white",
                        foreground="#1e293b",
                        fieldbackground="white",
                        borderwidth=0,
                        font=("Segoe UI", 11))
        style.configure("Treeview.Heading",
                        background="#f8fafc",
                        foreground="#475569",
                        font=("Segoe UI", 12, "bold"),
                        relief="flat")
        style.map("Treeview",
                  background=[('selected', '#dbeafe')],
                  foreground=[('selected', '#1e40af')])

        self.tree = ttk.Treeview(
            table_container,
            columns=("ID", "Field", "Value", "Description"),
            show="headings",
            height=15
        )

        self.tree.heading("ID", text="ID", anchor="c")
        self.tree.column("ID", width=60, anchor="c")
        self.tree.heading("Field", text="Поле", anchor="c")
        self.tree.column("Field", width=150, anchor="c")
        self.tree.heading("Value", text="Значение", anchor="c")
        self.tree.column("Value", width=150, anchor="c")
        self.tree.heading("Description", text="Описание", anchor="c")
        self.tree.column("Description", width=300, anchor="c")

        self.column_mapping = {
            'ID': 'id',
            'Field': 'field',
            'Value': 'value',
            'Description': 'description'
        }

        self.tree.pack(expand=True, fill="both", padx=10, pady=10)
        self.tree.bind("<Double-1>", self.on_cell_double_click)

        # Get data from presenter
        dropdown = self.presenter.get_dropdown()
        self.show_dropdown_data(dropdown)

    def show_dropdown_data(self, dropdown):
        """Displays dropdown data in table"""
        self.tree.delete(*self.tree.get_children())
        for row in dropdown:
            self.tree.insert("", "end", values=row)
    def update_current_table(self):
        """Обновляет данные в текущей таблице"""
        if hasattr(self, 'current_table'):
            if self.current_table == 'users':
                self.show_users()
            elif self.current_table == 'menu':
                self.show_menu()
            # Можно добавить другие таблицы по мере необходимости
    
    def on_cell_double_click(self, event):
        selected_item = self.tree.selection()
        if not selected_item:
            return
        column_id = self.tree.identify_column(event.x) #Определяем колонку
        column_index = int(column_id[1:]) - 1
        #Полуаем данные (Tkinter считает с 1)
        column_header = self.tree["columns"][column_index] #название колонки
        item = self.tree.item(selected_item) #Получаем данные строки
        entry_id = item["values"][0] #ID записи
        old_value = item["values"][column_index] #Текущее значение ячейки
        column_name = self.column_mapping.get(column_header)
        #Запрашиваем новое значение
        new_value = simpledialog.askstring("Редактирование",f"Новое значение для {column_name}:",initialvalue = old_value)

        if new_value and new_value != old_value:
            self.presenter.update_cell(self.current_table,entry_id,column_name,new_value)


