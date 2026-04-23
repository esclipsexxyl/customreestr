from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import simpledialog, messagebox, filedialog
import customtkinter as ctk
from PIL import Image
import CTkMessagebox as box
from customtkinter import CTkImage
from datetime import datetime
import sqlite3
import json
import os

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
            command=lambda: self.change_nav("add_reestr")
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
            command=lambda: self.change_nav("catalog")
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
            command=lambda: self.change_nav("dropdown")
        )
        self.dropdown_btn.pack(pady=2, padx=15, fill="x")

        # Кнопка выхода
        self.exit_btn = ctk.CTkButton(
            self.nav_frame,
            text='🚪 Выход',
            border_width=0,
            fg_color="transparent",
            text_color="#ef4444",
            hover_color="#fee2e2",
            anchor="w",
            font=("Segoe UI", 14),
            height=40,
            corner_radius=8,
            command=self.on_exit
        )
        self.exit_btn.pack(pady=(20, 2), padx=15, fill='x')

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

    def show_catalog(self):
        self.clear_main_frame()

        # Создаем PriceCatalog фрейм
        db_path = "model/customreestr.db"
        self.price_catalog = PriceCatalog(
            self.main_frame,
            db_path
        )
        self.price_catalog.pack(fill="both", expand=True)

    def show_dropdown(self):
        self.clear_main_frame()

        # Создаем DropdownEditor фрейм
        db_path = "model/customreestr.db"
        self.dropdown_editor = DropdownEditor(
            self.main_frame,
            db_path
        )
        self.dropdown_editor.pack(fill="both", expand=True)

    def show_addreestr(self):
        self.clear_main_frame()

        # Создаем RecordAdder фрейм
        db_path = "model/customreestr.db"
        self.record_adder = RecordAdder(
            self.main_frame,
            db_path,
            on_record_added=self.on_record_added_callback
        )
        self.record_adder.pack(fill="both", expand=True)

        # Добавляем callback для обновления метки заявки
        self.record_adder.entries['purchase_status'].configure(
            command=self.record_adder.update_request_label
        )

    def on_record_added_callback(self):
        """Callback после добавления записи"""
        pass

    def on_exit(self):
        self.destroy()


class EquipmentRow:
    """Класс для одной строки оборудования"""

    def __init__(self, parent, index, on_change_callback, record_adder_instance):
        self.parent = parent
        self.index = index
        self.on_change_callback = on_change_callback
        self.record_adder = record_adder_instance
        self.frame = None
        self.equipment_var = ctk.StringVar()
        self.quantity_var = ctk.StringVar(value="1")
        self.unit_price = 0.0
        self.create_widgets()

    def create_widgets(self):
        """Создание виджетов для строки оборудования"""
        self.frame = ctk.CTkFrame(self.parent, fg_color="transparent")
        self.frame.pack(fill="x", pady=5)

        # Номер строки
        self.number_label = ctk.CTkLabel(
            self.frame,
            text=f"{self.index + 1}.",
            width=30,
            font=("Segoe UI", 12)
        )
        self.number_label.pack(side="left", padx=(5, 10))

        # Выбор оборудования
        self.equipment_combo = ctk.CTkComboBox(
            self.frame,
            variable=self.equipment_var,
            width=250,
            values=self.record_adder.get_equipment_list(),
            state="normal",
            command=self.on_equipment_selected
        )
        self.equipment_combo.pack(side="left", padx=(0, 10))
        self.equipment_combo.bind('<KeyRelease>', self.on_equipment_typed)

        # Количество
        ctk.CTkLabel(self.frame, text="Кол-во:", width=50).pack(side="left", padx=(0, 5))
        self.quantity_entry = ctk.CTkEntry(
            self.frame,
            textvariable=self.quantity_var,
            width=80
        )
        self.quantity_entry.pack(side="left", padx=(0, 10))
        self.quantity_entry.bind('<KeyRelease>', self.on_quantity_changed)

        # Цена за единицу
        self.unit_price_label = ctk.CTkLabel(
            self.frame,
            text="0 ₽",
            text_color="#2563eb",
            width=100
        )
        self.unit_price_label.pack(side="left", padx=(0, 10))

        # Стоимость позиции
        self.position_price_label = ctk.CTkLabel(
            self.frame,
            text="0 ₽",
            text_color="#16a34a",
            font=("Segoe UI", 12, "bold"),
            width=120
        )
        self.position_price_label.pack(side="left", padx=(0, 10))

        # Кнопка удаления (кроме первой строки)
        if self.index > 0:
            self.delete_button = ctk.CTkButton(
                self.frame,
                text="✖",
                width=30,
                height=30,
                fg_color="#ef4444",
                hover_color="#dc2626",
                command=self.remove_row
            )
            self.delete_button.pack(side="left", padx=(0, 5))

    def on_equipment_selected(self, event=None):
        """Обработка выбора оборудования"""
        equipment_name = self.equipment_var.get().strip()
        if equipment_name:
            self.unit_price = self.record_adder.get_equipment_price(equipment_name) or 0.0
            self.update_display()
            self.on_change_callback()

    def on_equipment_typed(self, event=None):
        """Обработка ручного ввода оборудования"""
        self.frame.after(500, self.delayed_price_check)

    def delayed_price_check(self):
        """Отложенная проверка цены"""
        equipment_name = self.equipment_var.get().strip()
        if equipment_name:
            self.unit_price = self.record_adder.get_equipment_price(equipment_name) or 0.0
            self.update_display()
            self.on_change_callback()

    def on_quantity_changed(self, event=None):
        """Обработка изменения количества"""
        self.update_display()
        self.on_change_callback()

    def format_price(self, price):
        """Форматирование цены"""
        if price >= 1000:
            return f"{price:,.0f} ₽".replace(",", " ")
        return f"{int(price)} ₽"

    def update_display(self):
        """Обновление отображения цен"""
        try:
            quantity = int(self.quantity_var.get() or "1")
        except ValueError:
            quantity = 1

        if self.unit_price and self.unit_price > 0:
            self.unit_price_label.configure(text=self.format_price(self.unit_price), text_color="#2563eb")
            position_price = self.unit_price * quantity
            self.position_price_label.configure(text=self.format_price(position_price), text_color="#16a34a")
        else:
            self.unit_price_label.configure(text="не найдена", text_color="#ef4444")
            self.position_price_label.configure(text="0 ₽", text_color="#16a34a")

    def remove_row(self):
        """Удаление строки"""
        self.frame.destroy()
        self.record_adder.remove_equipment_row(self.index)

    def get_data(self):
        """Получение данных строки"""
        try:
            quantity = int(self.quantity_var.get() or "1")
        except ValueError:
            quantity = 1

        return {
            'equipment': self.equipment_var.get().strip(),
            'quantity': quantity,
            'unit_price': self.unit_price,
            'position_price': self.unit_price * quantity
        }


class RecordAdder(ctk.CTkFrame):
    def __init__(self, parent, db_path, on_record_added=None):
        super().__init__(parent, fg_color="transparent")
        self.db_path = db_path
        self.on_record_added = on_record_added

        # Инициализация атрибутов
        self.entries = {}
        self.file_paths = {"pdf": "", "excel": ""}
        self.equipment_rows = []
        self.equipment_list = []

        self.create_widgets()
        self.load_equipment_list_cache()
        self.load_purchase_status_values()

    def get_equipment_excel_file(self, equipment_name):
        """Получение пути к Excel файлу оборудования"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute("SELECT excel_file_path FROM Price_catalog WHERE name = ?", (equipment_name,))
            result = cursor.fetchone()
            conn.close()
            return result[0] if result and result[0] else None
        except Exception as e:
            print(f"Ошибка получения Excel файла: {e}")
            return None

    def auto_attach_excel(self, event=None):
        """Автоматическое прикрепление Excel файла при выборе оборудования"""
        try:
            if self.equipment_rows:
                equipment_name = self.equipment_rows[0].equipment_var.get().strip()
                if equipment_name:
                    excel_file_path = self.get_equipment_excel_file(equipment_name)
                    if excel_file_path and os.path.exists(excel_file_path):
                        self.file_paths["excel"] = excel_file_path
                        self.update_file_status()
                    else:
                        self.file_paths["excel"] = ""
                        self.update_file_status()
        except Exception as e:
            print(f"Ошибка автоматического прикрепления Excel: {e}")

    def create_widgets(self):
        """Создание интерфейса для добавления записи"""
        # Основной скроллируемый фрейм
        self.main_scrollable_frame = ctk.CTkScrollableFrame(self, fg_color="transparent")
        self.main_scrollable_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Заголовок
        header_label = ctk.CTkLabel(
            self.main_scrollable_frame,
            text="Добавление новой записи",
            font=("Segoe UI", 18, "bold"),
            text_color="#1e293b"
        )
        header_label.pack(pady=(0, 20))

        # Форма ввода основных данных
        form_frame = ctk.CTkFrame(self.main_scrollable_frame, corner_radius=12, fg_color="white")
        form_frame.pack(fill="x", pady=(0, 15))

        form_inner = ctk.CTkFrame(form_frame, fg_color="transparent")
        form_inner.pack(fill="x", padx=20, pady=20)

        self.entries = {}

        # Уровень 1: Форма заявки и № заявки
        ctk.CTkLabel(form_inner, text="Форма заявки*:", width=120).grid(row=0, column=0, sticky="w", pady=10, padx=(0, 10))
        self.entries['purchase_status'] = ctk.CTkComboBox(form_inner, width=200, state="readonly")
        self.entries['purchase_status'].grid(row=0, column=1, sticky="w", pady=10, padx=(0, 30))

        self.request_label = ctk.CTkLabel(form_inner, text="№ заявки*:", width=80)
        self.request_label.grid(row=0, column=2, sticky="w", pady=10, padx=(0, 10))
        self.entries['request_number'] = ctk.CTkEntry(form_inner, width=200)
        self.entries['request_number'].grid(row=0, column=3, sticky="w", pady=10)

        # Уровень 2: № подразделения и № акта
        ctk.CTkLabel(form_inner, text="№ подразделения:", width=120).grid(row=1, column=0, sticky="w", pady=10, padx=(0, 10))
        self.entries['department_number'] = ctk.CTkEntry(form_inner, width=200)
        self.entries['department_number'].grid(row=1, column=1, sticky="w", pady=10, padx=(0, 30))

        ctk.CTkLabel(form_inner, text="№ акта:", width=80).grid(row=1, column=2, sticky="w", pady=10, padx=(0, 10))
        self.entries['act_number'] = ctk.CTkEntry(form_inner, width=200)
        self.entries['act_number'].grid(row=1, column=3, sticky="w", pady=10)

        # Область для оборудования
        equipment_frame = ctk.CTkFrame(self.main_scrollable_frame, corner_radius=12, fg_color="white")
        equipment_frame.pack(fill="x", pady=(0, 15))

        equipment_inner = ctk.CTkFrame(equipment_frame, fg_color="transparent")
        equipment_inner.pack(fill="x", padx=20, pady=20)

        # Заголовки столбцов
        ctk.CTkLabel(equipment_inner, text="#", width=30).grid(row=0, column=0, padx=(5, 10))
        ctk.CTkLabel(equipment_inner, text="Оборудование*", width=250).grid(row=0, column=1, padx=(0, 10))
        ctk.CTkLabel(equipment_inner, text="Кол-во", width=80).grid(row=0, column=2, padx=(0, 10))
        ctk.CTkLabel(equipment_inner, text="Цена за ед.", width=100).grid(row=0, column=3, padx=(0, 10))
        ctk.CTkLabel(equipment_inner, text="Стоимость", width=120).grid(row=0, column=4, padx=(0, 10))
        ctk.CTkLabel(equipment_inner, text="Действия", width=80).grid(row=0, column=5)

        # Контейнер для строк оборудования
        self.equipment_container = ctk.CTkFrame(equipment_inner, fg_color="transparent")
        self.equipment_container.grid(row=1, column=0, columnspan=6, sticky="ew", pady=10)

        # Добавляем первую строку оборудования
        self.add_equipment_row()

        # Кнопки управления оборудованием
        button_frame = ctk.CTkFrame(equipment_inner, fg_color="transparent")
        button_frame.grid(row=2, column=0, columnspan=6, pady=10)

        ctk.CTkButton(
            button_frame,
            text="➕ Добавить оборудование",
            command=self.add_equipment_row,
            fg_color="#3b82f6",
            hover_color="#2563eb"
        ).pack(side="left", padx=(0, 10))

        ctk.CTkButton(
            button_frame,
            text="🔄 Обновить список",
            command=self.refresh_equipment_lists,
            fg_color="#64748b",
            hover_color="#475569"
        ).pack(side="left")

        # Итоговая стоимость
        total_frame = ctk.CTkFrame(equipment_inner, fg_color="transparent")
        total_frame.grid(row=3, column=0, columnspan=6, pady=10, sticky="e")

        ctk.CTkLabel(total_frame, text="Общая стоимость:", font=("Segoe UI", 14, "bold")).pack(side="left", padx=(0, 10))
        self.total_price_label = ctk.CTkLabel(
            total_frame,
            text="0 ₽",
            text_color="#16a34a",
            font=("Segoe UI", 14, "bold")
        )
        self.total_price_label.pack(side="left")

        # Дополнительные поля
        extra_frame = ctk.CTkFrame(self.main_scrollable_frame, corner_radius=12, fg_color="white")
        extra_frame.pack(fill="x", pady=(0, 15))

        extra_inner = ctk.CTkFrame(extra_frame, fg_color="transparent")
        extra_inner.pack(fill="x", padx=20, pady=20)

        # Примечание
        ctk.CTkLabel(extra_inner, text="Примечание:", anchor="nw").grid(row=0, column=0, sticky="nw", pady=5, padx=(0, 10))
        self.notes_text = ctk.CTkTextbox(extra_inner, height=80, width=400)
        self.notes_text.grid(row=0, column=1, sticky="ew", pady=5)

        # Кнопки файлов
        file_buttons_frame = ctk.CTkFrame(extra_inner, fg_color="transparent")
        file_buttons_frame.grid(row=1, column=1, sticky="w", pady=10)

        ctk.CTkButton(
            file_buttons_frame,
            text="📄 Прикрепить PDF (Акт необходимости)",
            command=self.attach_pdf,
            fg_color="#3b82f6",
            hover_color="#2563eb"
        ).pack(side="left", padx=(0, 10))

        ctk.CTkButton(
            file_buttons_frame,
            text="📊 Прикрепить Excel (ТЗ)",
            command=self.attach_excel,
            fg_color="#3b82f6",
            hover_color="#2563eb"
        ).pack(side="left")

        # Статус файлов
        self.file_status = ctk.CTkLabel(extra_inner, text="Файлы не прикреплены", text_color="#94a3b8")
        self.file_status.grid(row=2, column=1, sticky="w", pady=5)

        # Настройка растягивания
        extra_inner.columnconfigure(1, weight=1)

        # Кнопки действий
        action_frame = ctk.CTkFrame(self.main_scrollable_frame, fg_color="transparent")
        action_frame.pack(pady=20)

        ctk.CTkButton(
            action_frame,
            text="✅ Сохранить запись",
            command=self.save_record,
            fg_color="#22c55e",
            hover_color="#16a34a",
            width=150
        ).pack(side="left", padx=10)

        ctk.CTkButton(
            action_frame,
            text="🔄 Очистить форму",
            command=self.clear_form,
            fg_color="#64748b",
            hover_color="#475569",
            width=150
        ).pack(side="left", padx=10)

        ctk.CTkButton(
            action_frame,
            text="📋 Показать все записи",
            command=self.show_all_records,
            fg_color="#8b5cf6",
            hover_color="#7c3aed",
            width=150
        ).pack(side="left", padx=10)

    def refresh_equipment_lists(self):
        """Обновить списки оборудования во всех строках"""
        self.load_equipment_list_cache()
        for row in self.equipment_rows:
            if hasattr(row, 'equipment_combo'):
                row.equipment_combo.configure(values=self.equipment_list)

    def add_equipment_row(self):
        """Добавление новой строки оборудования"""
        row = EquipmentRow(
            self.equipment_container,
            len(self.equipment_rows),
            self.calculate_total_price,
            self
        )
        self.equipment_rows.append(row)

    def remove_equipment_row(self, index):
        """Удаление строки оборудования"""
        if 0 <= index < len(self.equipment_rows):
            self.equipment_rows.pop(index)

        for i, row in enumerate(self.equipment_rows):
            row.index = i
            if hasattr(row, 'number_label'):
                row.number_label.configure(text=f"{i + 1}.")

        self.calculate_total_price()

    def get_equipment_list(self):
        """Получение списка оборудования"""
        if not self.equipment_list:
            self.load_equipment_list_cache()
        return self.equipment_list

    def get_equipment_price(self, equipment_name):
        """Получение цены оборудования"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute("SELECT unit_price FROM Price_catalog WHERE name = ?", (equipment_name,))
            result = cursor.fetchone()
            conn.close()
            return result[0] if result else None
        except Exception as e:
            print(f"Ошибка получения цены: {e}")
            return None

    def format_price(self, price):
        """Форматирование цены"""
        if price >= 1000:
            return f"{price:,.0f} ₽".replace(",", " ")
        return f"{int(price)} ₽"

    def calculate_total_price(self):
        """Расчет общей стоимости"""
        total_price = 0.0

        for row in self.equipment_rows:
            data = row.get_data()
            if data['equipment']:
                total_price += data['position_price']

        self.total_price_label.configure(text=self.format_price(total_price))

        if self.equipment_rows and self.equipment_rows[0].equipment_var.get().strip():
            self.auto_attach_excel()

    def load_equipment_list_cache(self):
        """Загрузка списка оборудования в кэш"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute("SELECT name FROM Price_catalog ORDER BY name")
            results = cursor.fetchall()
            conn.close()
            self.equipment_list = [result[0] for result in results]
            print(f"✅ Загружено {len(self.equipment_list)} единиц оборудования из базы данных")
        except Exception as e:
            print(f"❌ Ошибка загрузки оборудования: {e}")
            self.equipment_list = []

    def load_purchase_status_values(self):
        """Загрузка значений формы заявки из базы данных"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute("SELECT values_json FROM Dropdown_values WHERE dropdown_name = ?", ('purchase_status',))
            result = cursor.fetchone()
            conn.close()

            if result and result[0]:
                saved_values = json.loads(result[0])
                self.entries['purchase_status'].configure(values=saved_values)
            else:
                default_values = ["Служебная записка", "Заявки по омеге", "Форма 10ИТ"]
                self.entries['purchase_status'].configure(values=default_values)

        except Exception as e:
            print(f"Ошибка загрузки значений формы заявки: {e}")
            default_values = ["Служебная записка", "Заявки по омеге", "Форма 10ИТ"]
            self.entries['purchase_status'].configure(values=default_values)

    def update_request_label(self):
        """Обновление названия поля в зависимости от выбранной формы заявки"""
        selected_form = self.entries['purchase_status'].get()
        if selected_form:
            self.request_label.configure(text=f"№ {selected_form}:")
        else:
            self.request_label.configure(text="№ заявки:")

    def attach_pdf(self):
        """Прикрепление PDF файла"""
        file_path = filedialog.askopenfilename(
            title="Выберите PDF файл (Акт необходимости)",
            filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")]
        )
        if file_path:
            self.file_paths["pdf"] = file_path
            self.update_file_status()

    def attach_excel(self):
        """Прикрепление Excel файла"""
        file_path = filedialog.askopenfilename(
            title="Выберите Excel файл (ТЗ)",
            filetypes=[("Excel files", "*.xlsx *.xls"), ("All files", "*.*")]
        )
        if file_path:
            self.file_paths["excel"] = file_path
            self.update_file_status()

    def update_file_status(self):
        """Обновление статуса прикрепленных файлов"""
        pdf_status = "✓" if self.file_paths["pdf"] else "✗"
        excel_status = "✓" if self.file_paths["excel"] else "✗"
        self.file_status.configure(
            text=f"PDF: {pdf_status} | Excel: {excel_status}",
            text_color="#22c55e" if (self.file_paths["pdf"] or self.file_paths["excel"]) else "#94a3b8"
        )

    def save_record(self):
        """Сохранение новой записи"""
        try:
            request_number = self.entries['request_number'].get().strip()
            request_form = self.entries['purchase_status'].get()

            if not request_number:
                messagebox.showwarning("Внимание", "Введите номер заявки!")
                return
            if not request_form:
                messagebox.showwarning("Внимание", "Выберите форму заявки!")
                return

            equipment_data = []
            for row in self.equipment_rows:
                data = row.get_data()
                if data['equipment']:
                    equipment_data.append(data)

            if not equipment_data:
                messagebox.showwarning("Внимание", "Добавьте хотя бы одно оборудование!")
                return

            equipment_list = [f"{data['equipment']} ({data['quantity']} шт.)" for data in equipment_data]
            equipment_text = "; ".join(equipment_list)
            total_price = sum(data['position_price'] for data in equipment_data)
            total_quantity = sum(data['quantity'] for data in equipment_data)

            data = (
                request_number,
                self.entries['department_number'].get().strip(),
                self.entries['act_number'].get().strip(),
                "",
                equipment_text,
                total_quantity,
                "",
                request_form,
                "",
                self.notes_text.get("1.0", tk.END).strip(),
                self.file_paths["pdf"],
                self.file_paths["excel"],
                "",
                "",
                total_price,
                "",
                ""
            )

            self.add_record(data)
            messagebox.showinfo("Успех", f"Запись с номером '{request_number}' успешно сохранена!")

            if self.on_record_added:
                try:
                    self.on_record_added()
                except Exception as e:
                    print(f"Ошибка при обновлении окон: {e}")

            self.clear_form()

        except Exception as e:
            if "уже существует" in str(e):
                messagebox.showwarning("Внимание", f"Заявка с номером '{request_number}' уже существует!")
            else:
                messagebox.showerror("Ошибка", f"Ошибка при сохранении: {str(e)}")

    def add_record(self, data):
        """Добавление записи в базу данных"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        try:
            cursor.execute("""
                INSERT INTO Procurement (
                    request_number, department_number, act_number, supplier, 
                    equipment, quantity, delivery_date, purchase_status, 
                    payment_status, notes, pdf_file_path, excel_file_path, 
                    contract_number, invoice_number, equipment_price, 
                    status, created_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, data)
            conn.commit()
        except sqlite3.IntegrityError as e:
            conn.close()
            raise Exception(f"Запись с номером '{data[0]}' уже существует!")
        conn.close()

    def get_all_records(self):
        """Получение всех записей"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Procurement")
        records = cursor.fetchall()
        conn.close()
        return records

    def clear_form(self):
        """Очистка формы"""
        for name, widget in self.entries.items():
            if isinstance(widget, ctk.CTkEntry):
                widget.delete(0, tk.END)
            elif isinstance(widget, ctk.CTkComboBox):
                widget.set('')

        self.load_purchase_status_values()
        self.notes_text.delete("1.0", tk.END)
        self.request_label.configure(text="№ заявки:")
        self.file_paths = {"pdf": "", "excel": ""}
        self.update_file_status()

        for i in range(len(self.equipment_rows) - 1, 0, -1):
            self.equipment_rows[i].frame.destroy()
            self.equipment_rows.pop(i)

        if self.equipment_rows:
            self.equipment_rows[0].equipment_var.set("")
            self.equipment_rows[0].quantity_var.set("1")
            self.equipment_rows[0].unit_price = 0.0
            self.equipment_rows[0].update_display()

        self.calculate_total_price()

    def show_all_records(self):
        """Показать все записи"""
        try:
            records_window = ctk.CTkToplevel(self)
            records_window.title("Все записи")
            records_window.geometry("900x600")

            records_window.update_idletasks()
            width = 900
            height = 600
            screen_width = records_window.winfo_screenwidth()
            screen_height = records_window.winfo_screenheight()
            x = (screen_width - width) // 2
            y = (screen_height - height) // 2
            records_window.geometry(f'{width}x{height}+{x}+{y}')

            main_frame = ctk.CTkFrame(records_window, fg_color="transparent")
            main_frame.pack(fill="both", expand=True, padx=20, pady=20)

            tree_frame = ttk.Frame(main_frame)
            tree_frame.pack(fill=tk.BOTH, expand=True)

            columns = ("Заявка", "Подразделение", "Оборудование", "Кол-во", "Форма заявки", "Цена")
            tree = ttk.Treeview(tree_frame, columns=columns, show="headings", height=15)

            column_configs = [
                ("Заявка", 120, "center"),
                ("Подразделение", 120, "center"),
                ("Оборудование", 200, "center"),
                ("Кол-во", 80, "center"),
                ("Форма заявки", 150, "center"),
                ("Цена", 120, "center")
            ]

            for col, width, anchor in column_configs:
                tree.heading(col, text=col)
                tree.column(col, width=width, anchor=anchor)

            records = self.get_all_records()

            for record in records:
                formatted_price = self.format_price(record[15]) if record[15] else "0 ₽"
                tree.insert("", tk.END, values=(
                    record[1] or "-",
                    record[2] or "-",
                    record[5] or "-",
                    record[6] or "0",
                    record[8] or "-",
                    formatted_price
                ))

            scrollbar = ttk.Scrollbar(tree_frame, orient=tk.VERTICAL, command=tree.yview)
            tree.configure(yscrollcommand=scrollbar.set)

            tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
            scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

            close_button = ctk.CTkButton(records_window, text="Закрыть", command=records_window.destroy)
            close_button.pack(pady=10)

        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось загрузить данные: {str(e)}")


class PriceCatalog(ctk.CTkFrame):
    def __init__(self, parent, db_path):
        super().__init__(parent, fg_color="transparent")
        self.db_path = db_path
        self.create_widgets()
        self.load_data()

    def create_widgets(self):
        """Создание интерфейса справочника цен"""
        main_frame = ctk.CTkScrollableFrame(self, fg_color="transparent")
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Заголовок
        ctk.CTkLabel(
            main_frame,
            text="Справочник цен оборудования",
            font=("Segoe UI", 18, "bold"),
            text_color="#1e293b"
        ).pack(pady=(0, 15))

        # Форма быстрого добавления
        form_frame = ctk.CTkFrame(main_frame, corner_radius=12, fg_color="white")
        form_frame.pack(fill="x", pady=(0, 15))

        form_inner = ctk.CTkFrame(form_frame, fg_color="transparent")
        form_inner.pack(fill="x", padx=20, pady=20)

        self.entries = {}
        fields = [
            ("Наименование оборудования*:", "equipment_name"),
            ("Цена за единицу (руб)*:", "unit_price"),
            ("Категория:", "category")
        ]

        for i, (label, name) in enumerate(fields):
            ctk.CTkLabel(form_inner, text=label, width=200).grid(row=i, column=0, sticky="w", pady=5, padx=(0, 10))
            entry = ctk.CTkEntry(form_inner, width=300)
            entry.grid(row=i, column=1, sticky="w", pady=5, padx=(0, 10))
            self.entries[name] = entry

        # Подсказка для формата цены
        price_hint = ctk.CTkLabel(form_inner, text="Пример: 12000 или 12500.50", text_color="#94a3b8", font=("Segoe UI", 10))
        price_hint.grid(row=1, column=2, sticky="w", pady=5, padx=(5, 0))

        # Кнопки управления
        button_frame = ctk.CTkFrame(form_inner, fg_color="transparent")
        button_frame.grid(row=3, column=0, columnspan=3, pady=10)

        ctk.CTkButton(
            button_frame,
            text="➕ Добавить",
            command=self.add_equipment,
            fg_color="#22c55e",
            hover_color="#16a34a"
        ).pack(side="left", padx=5)

        ctk.CTkButton(
            button_frame,
            text="✏️ Редактировать",
            command=self.open_edit_window,
            fg_color="#3b82f6",
            hover_color="#2563eb"
        ).pack(side="left", padx=5)

        ctk.CTkButton(
            button_frame,
            text="🗑️ Удалить",
            command=self.delete_equipment,
            fg_color="#ef4444",
            hover_color="#dc2626"
        ).pack(side="left", padx=5)

        ctk.CTkButton(
            button_frame,
            text="🧹 Очистить форму",
            command=self.clear_form,
            fg_color="#64748b",
            hover_color="#475569"
        ).pack(side="left", padx=5)

        # Таблица оборудования
        table_frame = ctk.CTkFrame(main_frame, corner_radius=12, fg_color="white")
        table_frame.pack(fill="both", expand=True)

        table_inner = ctk.CTkFrame(table_frame, fg_color="transparent")
        table_inner.pack(fill="both", expand=True, padx=20, pady=20)

        columns = ("ID", "Оборудование", "Цена", "Категория", "Excel файл", "Обновлено")
        self.tree = ttk.Treeview(table_inner, columns=columns, show="headings", height=25)

        column_configs = [
            ("ID", 50, "center"),
            ("Оборудование", 200, "center"),
            ("Цена", 120, "center"),
            ("Категория", 120, "center"),
            ("Excel файл", 200, "center"),
            ("Обновлено", 120, "center")
        ]

        for col, width, anchor in column_configs:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=width, anchor=anchor)

        # Scrollbar
        scrollbar = ttk.Scrollbar(table_inner, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Привязка двойного клика для редактирования
        self.tree.bind("<Double-1>", lambda e: self.open_edit_window())

        # Настройка растягивания
        form_inner.columnconfigure(1, weight=1)

    def format_price(self, price):
        """Форматирование цены"""
        if price >= 1000:
            return f"{price:,.0f} ₽".replace(",", " ")
        return f"{int(price)} ₽"

    def parse_price(self, price_text):
        """Парсинг цены из текста"""
        price_text = price_text.replace(" ", "").replace("₽", "").replace(",", ".")
        return float(price_text)

    def add_equipment(self):
        """Добавление нового оборудования"""
        try:
            name = self.entries['equipment_name'].get().strip()
            price_text = self.entries['unit_price'].get().strip()

            if not name:
                messagebox.showwarning("Внимание", "Введите наименование оборудования!")
                return
            if not price_text:
                messagebox.showwarning("Внимание", "Введите цену оборудования!")
                return

            try:
                price = self.parse_price(price_text)
                if price <= 0:
                    messagebox.showwarning("Внимание", "Цена должна быть больше нуля!")
                    return
            except ValueError:
                messagebox.showwarning("Внимание", "Цена должна быть числом!")
                return

            category = self.entries['category'].get().strip()

            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()

            cursor.execute('''
                INSERT INTO Price_catalog (name, unit_price, category, description, excel_file_path, last_updated)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (name, price, category, "", "", datetime.now().strftime("%d.%m.%Y %H:%M")))

            conn.commit()
            conn.close()

            messagebox.showinfo("Успех", "Оборудование добавлено в справочник!")
            self.clear_form()
            self.load_data()

        except sqlite3.IntegrityError:
            messagebox.showwarning("Внимание", "Оборудование с таким названием уже существует!")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Ошибка при добавлении: {str(e)}")

    def open_edit_window(self):
        """Открытие всплывающего окна для редактирования"""
        selection = self.tree.selection()
        if not selection:
            messagebox.showwarning("Внимание", "Выберите оборудование для редактирования!")
            return

        item = self.tree.item(selection[0])
        equipment_id = item['values'][0]
        equipment_name = item['values'][1]

        # Создаем всплывающее окно
        edit_window = ctk.CTkToplevel(self)
        edit_window.title(f"Редактирование: {equipment_name}")
        edit_window.geometry("600x500")
        edit_window.resizable(False, False)

        # Центрируем окно редактирования по центру экрана
        self.center_child_window(edit_window, 600, 500)

        # Загружаем данные оборудования
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Price_catalog WHERE id=?", (equipment_id,))
        record = cursor.fetchone()
        conn.close()

        if not record:
            messagebox.showerror("Ошибка", "Не удалось загрузить данные оборудования!")
            edit_window.destroy()
            return

        # Создаем форму редактирования
        EditEquipmentForm(edit_window, record, self, self.db_path)

    def center_child_window(self, child_window, width, height):
        """Центрирование дочернего окна по центру экрана"""
        screen_width = child_window.winfo_screenwidth()
        screen_height = child_window.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        child_window.geometry(f"{width}x{height}+{x}+{y}")

    def delete_equipment(self):
        """Удаление оборудования"""
        selection = self.tree.selection()
        if not selection:
            messagebox.showwarning("Внимание", "Выберите оборудование для удаления!")
            return

        item = self.tree.item(selection[0])
        equipment_name = item['values'][1]
        equipment_id = item['values'][0]

        if messagebox.askyesno("Подтверждение",
                               f"Удалить оборудование '{equipment_name}'?"):
            try:
                conn = sqlite3.connect(self.db_path)
                cursor = conn.cursor()
                cursor.execute("DELETE FROM Price_catalog WHERE id=?", (equipment_id,))
                conn.commit()
                conn.close()

                messagebox.showinfo("Успех", "Оборудование удалено!")
                self.load_data()

            except Exception as e:
                messagebox.showerror("Ошибка", f"Ошибка при удалении: {str(e)}")

    def clear_form(self):
        """Очистка формы"""
        for name, widget in self.entries.items():
            if isinstance(widget, ctk.CTkEntry):
                widget.delete(0, tk.END)

    def load_data(self):
        """Загрузка данных в таблицу"""
        for item in self.tree.get_children():
            self.tree.delete(item)

        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Price_catalog ORDER BY name")
            records = cursor.fetchall()
            conn.close()

            for record in records:
                formatted_price = self.format_price(record[2])

                excel_file = record[5] if len(record) > 5 and record[5] else "Не прикреплен"
                if excel_file != "Не прикреплен":
                    excel_file = os.path.basename(excel_file)

                last_updated = record[6] if len(record) > 6 else "-"

                self.tree.insert("", tk.END, values=(
                    record[0],
                    record[1],
                    formatted_price,
                    record[4] or "-",
                    excel_file,
                    last_updated
                ))

        except Exception as e:
            messagebox.showerror("Ошибка", f"Ошибка при загрузке данных: {str(e)}")

    def refresh_data(self):
        """Обновление данных после редактирования"""
        self.load_data()


class EditEquipmentForm(ctk.CTkFrame):
    def __init__(self, parent, record, main_app, db_path):
        super().__init__(parent, fg_color="transparent")
        self.record = record
        self.main_app = main_app
        self.db_path = db_path

        self.create_widgets()
        self.load_record_data()
        self.pack(fill="both", expand=True, padx=15, pady=15)

    def create_widgets(self):
        """Создание формы редактирования"""
        main_frame = ctk.CTkFrame(self, fg_color="transparent")
        main_frame.pack(fill="both", expand=True)

        # Заголовок
        ctk.CTkLabel(
            main_frame,
            text="Редактирование оборудования",
            font=("Segoe UI", 14, "bold"),
            text_color="#1e293b"
        ).pack(pady=(0, 15))

        # Форма редактирования
        form_frame = ctk.CTkFrame(main_frame, corner_radius=12, fg_color="white")
        form_frame.pack(fill="both", expand=True, pady=(0, 15))

        form_inner = ctk.CTkFrame(form_frame, fg_color="transparent")
        form_inner.pack(fill="both", expand=True, padx=20, pady=20)

        self.entries = {}
        fields = [
            ("Наименование оборудования*:", "equipment_name"),
            ("Цена за единицу (руб)*:", "unit_price"),
            ("Категория:", "category")
        ]

        for i, (label, name) in enumerate(fields):
            ctk.CTkLabel(form_inner, text=label, width=200).grid(row=i, column=0, sticky="w", pady=5, padx=(0, 10))
            entry = ctk.CTkEntry(form_inner, width=300)
            entry.grid(row=i, column=1, sticky="w", pady=5, padx=(0, 10))
            self.entries[name] = entry

        # Описание
        ctk.CTkLabel(form_inner, text="Описание:").grid(row=3, column=0, sticky="nw", pady=5, padx=(0, 10))
        self.description_text = ctk.CTkTextbox(form_inner, height=80, width=300)
        self.description_text.grid(row=3, column=1, sticky="w", pady=5, padx=(0, 10))

        # Поле для Excel файла
        ctk.CTkLabel(form_inner, text="Excel файл (ТЗ):").grid(row=4, column=0, sticky="w", pady=5, padx=(0, 10))

        file_frame = ctk.CTkFrame(form_inner, fg_color="transparent")
        file_frame.grid(row=4, column=1, sticky="w", pady=5, padx=(0, 10))

        self.excel_file_path = tk.StringVar()
        file_entry = ctk.CTkEntry(file_frame, textvariable=self.excel_file_path, width=250)
        file_entry.pack(side="left", fill="x", expand=True)

        ctk.CTkButton(
            file_frame,
            text="Обзор",
            width=60,
            command=self.attach_excel_file,
            fg_color="#3b82f6",
            hover_color="#2563eb"
        ).pack(side="right", padx=(5, 0))

        ctk.CTkButton(
            file_frame,
            text="Открыть",
            width=60,
            command=self.open_excel_file,
            fg_color="#64748b",
            hover_color="#475569"
        ).pack(side="right", padx=(5, 0))

        # Кнопки действий
        button_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        button_frame.pack(pady=10)

        ctk.CTkButton(
            button_frame,
            text="💾 Сохранить",
            command=self.save_changes,
            fg_color="#22c55e",
            hover_color="#16a34a"
        ).pack(side="left", padx=5)

        ctk.CTkButton(
            button_frame,
            text="❌ Отменить",
            command=self.master.destroy,
            fg_color="#ef4444",
            hover_color="#dc2626"
        ).pack(side="left", padx=5)

        # Настройка растягивания
        form_inner.columnconfigure(1, weight=1)

    def format_price(self, price):
        """Форматирование цены"""
        if price >= 1000:
            return f"{price:,.0f} ₽".replace(",", " ")
        return f"{int(price)} ₽"

    def parse_price(self, price_text):
        """Парсинг цены из текста"""
        price_text = price_text.replace(" ", "").replace("₽", "").replace(",", ".")
        return float(price_text)

    def load_record_data(self):
        """Загрузка данных записи в форму"""
        self.entries['equipment_name'].insert(0, self.record[1])
        self.entries['unit_price'].insert(0, str(self.record[2]))
        self.entries['category'].insert(0, self.record[4] or "")
        self.description_text.insert("1.0", self.record[3] or "")

        if len(self.record) > 5 and self.record[5]:
            self.excel_file_path.set(self.record[5])

    def attach_excel_file(self):
        """Прикрепление Excel файла"""
        file_path = filedialog.askopenfilename(
            title="Выберите Excel файл (ТЗ)",
            filetypes=[("Excel files", "*.xlsx *.xls"), ("All files", "*.*")]
        )
        if file_path:
            self.excel_file_path.set(file_path)

    def open_excel_file(self):
        """Открытие прикрепленного Excel файла"""
        file_path = self.excel_file_path.get()
        if file_path and os.path.exists(file_path):
            os.startfile(file_path)
        else:
            messagebox.showwarning("Внимание", "Файл не прикреплен или не найден!")

    def save_changes(self):
        """Сохранение изменений"""
        try:
            name = self.entries['equipment_name'].get().strip()
            price_text = self.entries['unit_price'].get().strip()

            if not name:
                messagebox.showwarning("Внимание", "Введите наименование оборудования!")
                return
            if not price_text:
                messagebox.showwarning("Внимание", "Введите цену оборудования!")
                return

            try:
                price = self.parse_price(price_text)
                if price <= 0:
                    messagebox.showwarning("Внимание", "Цена должна быть больше нуля!")
                    return
            except ValueError:
                messagebox.showwarning("Внимание", "Цена должна быть числом!")
                return

            category = self.entries['category'].get().strip()
            description = self.description_text.get("1.0", tk.END).strip()
            excel_file = self.excel_file_path.get()

            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()

            # Проверяем, не дублируется ли название с другими записями
            cursor.execute("SELECT id FROM Price_catalog WHERE name = ? AND id != ?",
                           (name, self.record[0]))
            if cursor.fetchone():
                messagebox.showwarning("Внимание", "Оборудование с таким названием уже существует!")
                return

            cursor.execute('''
                UPDATE Price_catalog 
                SET name=?, unit_price=?, category=?, description=?, excel_file_path=?, last_updated=?
                WHERE id=?
            ''', (name, price, category, description, excel_file, datetime.now().strftime("%d.%m.%Y %H:%M"),
                  self.record[0]))

            conn.commit()
            conn.close()

            messagebox.showinfo("Успех", "Данные оборудования обновлены!")
            self.main_app.refresh_data()
            self.master.destroy()

        except Exception as e:
            messagebox.showerror("Ошибка", f"Ошибка при обновлении: {str(e)}")


class DropdownEditor(ctk.CTkFrame):
    """Редактор выпадающих списков"""

    def __init__(self, parent, db_path):
        super().__init__(parent, fg_color="transparent")
        self.db_path = db_path
        self.dropdowns_data = {
            'purchase_status': {
                'name': 'Форма заявки',
                'values': ["Служебная записка", "Заявки по омеге", "Форма 10ИТ"]
            },
            'finance_decision_136': {
                'name': 'Решение 136 отдела',
                'values': ["", "Одобрено", "Отклонено", "На рассмотрении"]
            },
            'finance_decision_150': {
                'name': 'Решение 150 отдела',
                'values': ["", "Одобрено", "Отклонено", "На рассмотрении"]
            }
        }
        self.create_widgets()
        self.load_dropdowns_data()

    def create_widgets(self):
        """Создание интерфейса редактора"""
        main_frame = ctk.CTkScrollableFrame(self, fg_color="transparent")
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        ctk.CTkLabel(
            main_frame,
            text="📋 Редактирование выпадающих списков",
            font=("Segoe UI", 18, "bold"),
            text_color="#1e293b"
        ).pack(pady=(0, 20))

        lists_frame = ctk.CTkFrame(main_frame, corner_radius=12, fg_color="white")
        lists_frame.pack(fill="both", expand=True)

        lists_inner = ctk.CTkFrame(lists_frame, fg_color="transparent")
        lists_inner.pack(fill="both", expand=True, padx=20, pady=20)

        self.dropdown_widgets = {}

        for i, (key, data) in enumerate(self.dropdowns_data.items()):
            ctk.CTkLabel(
                lists_inner,
                text=f"{data['name']}:",
                font=("Segoe UI", 12, "bold"),
                text_color="#475569"
            ).grid(row=i * 2, column=0, sticky="w", pady=(10, 5), padx=(0, 15))

            text_widget = ctk.CTkTextbox(
                lists_inner,
                height=8,
                width=40,
                fg_color="#f8fafc",
                border_width=1,
                border_color="#e2e8f0",
                corner_radius=8
            )
            text_widget.grid(row=i * 2, column=1, sticky="ew", pady=(10, 5), padx=(0, 15))
            text_widget.insert("1.0", "\n".join(data['values']))

            save_btn = ctk.CTkButton(
                lists_inner,
                text="💾 Сохранить",
                command=lambda k=key: self.save_dropdown_values(k),
                fg_color="#22c55e",
                hover_color="#16a34a",
                width=120
            )
            save_btn.grid(row=i * 2 + 1, column=1, sticky="w", pady=(0, 10))

            self.dropdown_widgets[key] = {
                'text_widget': text_widget,
                'save_btn': save_btn
            }

        buttons_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        buttons_frame.pack(fill="x", pady=20)

        ctk.CTkButton(
            buttons_frame,
            text="🔄 Обновить все списки",
            command=self.load_dropdowns_data,
            fg_color="#3b82f6",
            hover_color="#2563eb"
        ).pack(side="left", padx=5)

        ctk.CTkButton(
            buttons_frame,
            text="📥 Сбросить к значениям по умолчанию",
            command=self.reset_to_default,
            fg_color="#f59e0b",
            hover_color="#d97706"
        ).pack(side="left", padx=5)

        info_label = ctk.CTkLabel(
            main_frame,
            text="💡 Каждое значение должно быть на новой строке. Пустые строки будут игнорироваться.",
            text_color="#94a3b8",
            font=("Segoe UI", 10)
        )
        info_label.pack(side="bottom", pady=(10, 0))

        lists_inner.columnconfigure(1, weight=1)

    def load_dropdowns_data(self):
        """Загрузка данных выпадающих списков из базы данных"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Dropdown_values (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    dropdown_name TEXT UNIQUE,
                    values_json TEXT,
                    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')

            for key in self.dropdowns_data.keys():
                cursor.execute(
                    "SELECT values_json FROM Dropdown_values WHERE dropdown_name = ?",
                    (key,)
                )
                result = cursor.fetchone()

                if result:
                    saved_values = json.loads(result[0])
                    self.dropdowns_data[key]['values'] = saved_values

                    text_widget = self.dropdown_widgets[key]['text_widget']
                    text_widget.delete("1.0", tk.END)
                    text_widget.insert("1.0", "\n".join(saved_values))

            conn.close()

        except Exception as e:
            print(f"Ошибка загрузки выпадающих списков: {e}")

    def save_dropdown_values(self, dropdown_key):
        """Сохранение значений для конкретного выпадающего списка"""
        try:
            text_widget = self.dropdown_widgets[dropdown_key]['text_widget']
            text_content = text_widget.get("1.0", tk.END).strip()

            values = [line.strip() for line in text_content.split('\n') if line.strip()]

            if not values:
                messagebox.showwarning("Внимание", "Список не может быть пустым!")
                return

            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()

            values_json = json.dumps(values, ensure_ascii=False)

            cursor.execute('''
                INSERT OR REPLACE INTO Dropdown_values (dropdown_name, values_json)
                VALUES (?, ?)
            ''', (dropdown_key, values_json))

            conn.commit()
            conn.close()

            self.dropdowns_data[dropdown_key]['values'] = values
            messagebox.showinfo("Успех", f"Список '{self.dropdowns_data[dropdown_key]['name']}' успешно сохранен!")

        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось сохранить список:\n{str(e)}")

    def reset_to_default(self):
        """Сброс к значениям по умолчанию"""
        if messagebox.askyesno("Подтверждение",
                               "Вы уверены, что хотите сбросить все списки к значениям по умолчанию?"):

            default_values = {
                'purchase_status': ["Служебная записка", "Заявки по омеге", "Форма 10ИТ"],
                'finance_decision_136': ["", "Одобрено", "Отклонено", "На рассмотрении"],
                'finance_decision_150': ["", "Одобрено", "Отклонено", "На рассмотрении"]
            }

            try:
                conn = sqlite3.connect(self.db_path)
                cursor = conn.cursor()

                for key, values in default_values.items():
                    values_json = json.dumps(values, ensure_ascii=False)

                    cursor.execute('''
                        INSERT OR REPLACE INTO Dropdown_values (dropdown_name, values_json)
                        VALUES (?, ?)
                    ''', (key, values_json))

                    text_widget = self.dropdown_widgets[key]['text_widget']
                    text_widget.delete("1.0", tk.END)
                    text_widget.insert("1.0", "\n".join(values))

                    self.dropdowns_data[key]['values'] = values

                conn.commit()
                conn.close()

                messagebox.showinfo("Успех", "Все списки сброшены к значениям по умолчанию!")

            except Exception as e:
                messagebox.showerror("Ошибка", f"Не удалось сбросить списки:\n{str(e)}")

    def get_dropdown_values(self, dropdown_name):
        """Получение значений для выпадающего списка по имени"""
        return self.dropdowns_data.get(dropdown_name, {}).get('values', [])

