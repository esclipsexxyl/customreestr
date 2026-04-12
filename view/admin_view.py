from tkinter import *
import tkinter.ttk as ttk
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
        self.geometry('1440x900')
        self.title('Реестр закупки оборудования - панель администратора')
        self.configure(fg_color="#ffffff")
        ctk.set_default_color_theme("blue")
        ctk.set_appearance_mode("light")
        #self.attributes('-fullscreen', True)

        # Навигация
        self.nav_frame=ctk.CTkFrame(self,fg_color="#ffffff")
        self.nav_frame.pack(side='left',fill='y')

        # Вкладки
        self.menu_btn = ctk.CTkButton(self.nav_frame,text='📎Главное меню', border_width=0,fg_color="#2596be",text_color="white",hover_color="#227fa1",anchor="w",font=("Arial",18),command=lambda:self.change_nav("menu"))
        self.menu_btn.pack(pady=10,padx=10)
        self.users_btn = ctk.CTkButton(self.nav_frame,text='👥Пользователи', border_width=0,fg_color="transparent",text_color="black",hover_color="white",anchor="w",font=("Arial",14),command=lambda:self.change_nav("users"))
        self.users_btn.pack(pady=10,padx=10)
        self.roles_btn = ctk.CTkButton(self.nav_frame,text='👤Роли', border_width=0,fg_color="transparent",text_color="black",hover_color="white",anchor="w",font=("Arial",14),command=lambda:self.change_nav("roles"))
        self.roles_btn.pack(pady=10,padx=10)
        self.catalog_btn = ctk.CTkButton(self.nav_frame,text='🧾Справочник', border_width=0,fg_color="transparent",text_color="black",hover_color="white",anchor="w",font=("Arial",14),command=lambda:self.change_nav("catalog"))
        self.catalog_btn.pack(pady=10,padx=10)
        self.reestr_btn = ctk.CTkButton(self.nav_frame,text='🧾Реестр', border_width=0,fg_color="transparent",text_color="black",hover_color="white",anchor="w",font=("Arial",14),command=lambda:self.change_nav("reestr"))
        self.reestr_btn.pack(pady=10,padx=10)
        self.logs_btn = ctk.CTkButton(self.nav_frame,text='🧾Логи', border_width=0,fg_color="transparent",text_color="black",hover_color="white",anchor="w",font=("Arial",14),command=lambda:self.change_nav("logs"))
        self.logs_btn.pack(pady=10,padx=10)

        # Информация о пользователе
        self.infoframe = ctk.CTkFrame(self.nav_frame,height=40,width=100, fg_color="#ebebeb",border_width=0,corner_radius=15)
        self.infoframe.place(x=10,y=850)
        self.infoimg = ctk.CTkImage(Image.open("images/user.png"), size=(32, 32))
        self.infolabel = ctk.CTkLabel(self.infoframe, image=self.infoimg, text="", fg_color="transparent")
        self.infolabel.place(y=4, x=10)
        self.infolabel2 = ctk.CTkLabel(self.infoframe, fg_color="transparent",text_color="black",text=f"{self.login}")
        self.infolabel2.place(y=8,x=52)

        # Основной фрейм
        self.main_frame = ctk.CTkFrame(self,fg_color="#edfbff")
        self.main_frame.pack(side='right',expand=True,fill='both')

        # Фрейм заголовок
        self.title_frame = ctk.CTkFrame(self.main_frame,fg_color="#2596be",height=46,corner_radius=0)
        self.title_frame.pack(side='top',fill='x')
        self.vektorlogo = ctk.CTkImage(Image.open("images/vektorlogo.png"), size=(24,46))
        self.title_label = ctk.CTkLabel(self.title_frame, text="Реестр закупки оборудования",font=("Arial",22,"bold"),text_color="white")
        self.title_label.place(rely=0.25,x=40)
        self.vektorlabel = ctk.CTkLabel(self.title_frame,image=self.vektorlogo,text="",fg_color="transparent")
        self.vektorlabel.place(x=5,y=0)
        self.timelabel = ctk.CTkLabel(self.title_frame, text=f"{self.now.strftime("%d.%m.%Y %H:%M")}", fg_color="transparent", text_color="white",font=("Arial",18))
        self.timelabel.place(relx=0.88,rely=0.225)

        # Фрейм кнопок действий
        self.action_frame=ctk.CTkFrame(self.main_frame)
        self.action_frame.pack(side="bottom",fill="x",pady=10)
        self.add_btn = ctk.CTkButton(self.action_frame,text="Добавить")
        self.add_btn.pack(side="left",padx=5)
        self.delete_btn = ctk.CTkButton(self.action_frame,text="Удалить")

        self.update_time()

    def update_time(self):
        self.now = datetime.now()

        self.timelabel.configure(text=f"{self.now.strftime("%H:%M")} | {self.now.strftime("%d.%m.%Y")}")
        self.after(1000, self.update_time)
    
    def change_nav(self,name):
        buttons = {
            "menu": self.menu_btn,
            "users": self.users_btn,
            "roles": self.roles_btn,
            "catalog": self.catalog_btn,
            "reestr": self.reestr_btn,
            "logs": self.logs_btn
        }

        # Сбрасываем все кнопки
        for btn_name, btn in buttons.items():
            btn.configure(
                fg_color="transparent",
                hover_color="white",
                font=("Arial", 14),
                text_color="black"
            )

        # Подсвечиваем активную кнопку
        if name in buttons:
            buttons[name].configure(
                fg_color="#2596be",
                hover_color="#227fa1", ##2596be
                font=("Arial", 18),
                text_color="white"
            )
        match name:
            case "users":
                self.show_users()
            case "menu":
                self.show_menu()

    def clear_main_frame(self):
        for widget in self.main_frame.winfo_children():
            if widget != self.action_frame:
                if widget != self.title_frame:
                    widget.destroy()
               #widget.destroy()

    def show_menu(self):
        self.clear_main_frame()

        self.stat_frame1 = ctk.CTkFrame(self.main_frame, height=250,width=250,corner_radius=15,fg_color="#51cf51")
        self.stat_frame1.place(x=75,y=150)
        self.stat_frame2 = ctk.CTkFrame(self.main_frame, height=250,width=250,corner_radius=15,fg_color="#51cf51")
        self.stat_frame2.place(x=340,y=150)
        self.stat_frame3 = ctk.CTkFrame(self.main_frame, height=250,width=250,corner_radius=15,fg_color="#51cf51")
        self.stat_frame3.place(x=605,y=150)
        self.stat_frame4 = ctk.CTkFrame(self.main_frame, height=250,width=250,corner_radius=15,fg_color="#51cf51")
        self.stat_frame4.place(x=870,y=150)
        self.stat_label1 = ctk.CTkLabel(self.stat_frame1, fg_color="transparent",text=f"Кол-во пользователей: {self.userssum}",text_color="white",font=("Arial",24),wraplength=175)
        self.stat_label1.place(relx=0.5, rely=0.5, anchor="center")
        self.stat_label2 = ctk.CTkLabel(self.stat_frame2, fg_color="transparent",text=f"Кол-во ролей: {self.rolessum}",text_color="white",font=("Arial",24),wraplength=175)
        self.stat_label2.place(relx=0.5, rely=0.5, anchor="center")
        self.stat_label3 = ctk.CTkLabel(self.stat_frame3, fg_color="transparent",text=f"Кол-во записей в справочнике: {self.catalogsum}",text_color="white",font=("Arial",24),wraplength=175)
        self.stat_label3.place(relx=0.5, rely=0.5, anchor="center")
        self.stat_label4 = ctk.CTkLabel(self.stat_frame4, fg_color="transparent",text=f"Кол-во записей в реестре: {self.reestrsum}",text_color="white",font=("Arial",24),wraplength=175)
        self.stat_label4.place(relx=0.5, rely=0.5, anchor="center")


    def show_users (self):
        """Вызывает загрузку пользователей и оторбражает их"""
        self.current_table = 'users'
        self.clear_main_frame()
        ctk.CTkLabel(self.main_frame,text="Список пользователей",font=("Arial",14)).pack(pady=10)

        self.tree = ttk.Treeview(self.main_frame,columns=("ID","Логин","Пароль","Роль","Имя","Фамилия","Отчество","Дата регистрации"),show="headings")
        self.tree.heading("ID",text="ID",anchor="c")
        self.tree.column("ID",width=50,anchor="c")

        self.tree.heading("Логин",text="Логин",anchor="c")
        self.tree.column("Логин",width=228,anchor="c")

        self.tree.heading("Пароль", text="Пароль", anchor="c")
        self.tree.column("Пароль", width=120, anchor="c")

        self.tree.heading("Роль", text="Роль", anchor="c")
        self.tree.column("Роль", width=78, anchor="c")

        self.tree.heading("Имя", text="Имя", anchor="c")
        self.tree.column("Имя", width=78, anchor="c")

        self.tree.heading("Фамилия", text="Фамилия", anchor="c")
        self.tree.column("Фамилия", width=78, anchor="c")

        self.tree.heading("Отчество", text="Отчество", anchor="c")
        self.tree.column("Отчество", width=78, anchor="c")

        self.tree.heading("Дата регистрации", text="Дата регистрации", anchor="c")
        self.tree.column("Дата регистрации", width=78, anchor="c")


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

        self.tree.pack(expand=True,fill="both")
        #self.tree.bind("<<TreeviewSelect>>",self.on_select)
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

    def on_cell_double_click(self, event):
        selected_item = self.tree.selection()
        if not selected_item:
            return
        column_id = self.tree.identify_column(event.x) #Определяем колонку
        column_index = int(column_id[1:]) - 1
        #Полуаем данные (Trinter считает с 1)
        column_header = self.tree["columns"][column_index] #название колонки
        item = self.tree.item(selected_item) #Получаем данные строки
        entry_id = item["values"][0] #ID записи
        old_value = item["values"][column_index] #Текущее значение ячейки
        column_name = self.column_mapping.get(column_header)
        #Запрашиваем новое значение
        #new_value = simpledialog.askstring("Редактирование",f"Новое значение для {column_name}:",initialvalue = old_value)

        if new_value and new_value != old_value:
            self.presenter.update_cell(self.current_table,entry_id,column_name,new_value)


