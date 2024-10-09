import tkinter as tk
from tkinter import ttk
from .general_view import General_View
from controllers.patient_controller import PatientController

class Patient_View (General_View):
    
    def __init__ (self, root, controller):
        super().__init__(root, controller)
            # Main patient view
        self.patient_view_top_frame = tk.Frame(self.root, bg=self.ONYX, width=self.root.winfo_screenwidth())
        self.patient_view_bottom_frame = tk.Frame(self.root, bg=self.OUTER_SPACE, height=self.root.winfo_screenheight()-30, width=self.root.winfo_screenwidth())
            # Top Frame Components:
        self.patient_view_top_frame_logo_label = tk.Label(self.patient_view_top_frame, image=self.img_1, bg=self.ONYX)
        self.patient_view_top_frame_title_label = tk.Label(self.patient_view_top_frame, text='PyTHORD', foreground=self.ANTI_FLASH_WHITE, font=self.SUB_TITLE_FONT, bg=self.ONYX)
        self.patient_view_top_frame_user_name_label = tk.Label(self.patient_view_top_frame, text='', foreground=self.ANTI_FLASH_WHITE, font=self.SUB_TITLE_FONT, bg=self.ONYX)
            # Bottom Frame Components:
        self.patient_view_main_buttons_frame = tk.Frame(self.patient_view_bottom_frame, bg=self.OUTER_SPACE)
        self.patient_view_new_patient_frame = tk.Frame(self.patient_view_bottom_frame, bg=self.OUTER_SPACE)
        self.patient_view_search_patient_frame = tk.Frame(self.patient_view_bottom_frame, bg=self.OUTER_SPACE)
            # Main Buttons Frame Components:
        self.patient_view_create_buttom = tk.Button(self.patient_view_main_buttons_frame, bg=self.ANTI_FLASH_WHITE, activebackground=self.OUTER_SPACE, fg=self.ONYX, activeforeground=self.EART_YELLOW, text="Nuevo Paciente", font=self.MENU_TITLE_FONT, width=20)
        self.patient_view_search_buttom = tk.Button(self.patient_view_main_buttons_frame, bg=self.ANTI_FLASH_WHITE, activebackground=self.OUTER_SPACE, fg=self.ONYX, activeforeground=self.EART_YELLOW, text="Buscar Paciente", font=self.MENU_TITLE_FONT, width=20)
        self.patient_view_exit_buttom = tk.Button(self.patient_view_main_buttons_frame, bg=self.BITTERSWEET_SHIMMER, activebackground=self.ONYX, fg=self.ANTI_FLASH_WHITE, activeforeground=self.ANTI_FLASH_WHITE, text="Salir", font=self.MENU_TITLE_FONT, width=10)
        self.patient_view_main_buttons_frame_separator = ttk.Separator(self.patient_view_main_buttons_frame, orient='horizontal', style='top.TSeparator')
            # New Patients Frame Components:
                # New Patients Labels:
        self.patient_view_main_information_label = tk.Label(self.patient_view_new_patient_frame, text='Información Principal del Paciente:', foreground=self.EART_YELLOW, font=self.REGULAR_FONT, bg=self.OUTER_SPACE, justify='left')
        self.patient_view_patient_ci_label = tk.Label(self.patient_view_new_patient_frame, text='Cédula de Identidad (CI):', foreground=self.ANTI_FLASH_WHITE, font=self.REGULAR_FONT, bg=self.OUTER_SPACE, justify='right')
        self.patient_view_patient_birthdate_label = tk.Label(self.patient_view_new_patient_frame, text='Fecha de Nacimiento (dd/MM/YYYY):', foreground=self.ANTI_FLASH_WHITE, font=self.REGULAR_FONT, bg=self.OUTER_SPACE, justify='right')
        self.patient_view_patient_name_label = tk.Label(self.patient_view_new_patient_frame, text='Nombre (s):', foreground=self.ANTI_FLASH_WHITE, font=self.REGULAR_FONT, bg=self.OUTER_SPACE, justify='right')
        self.patient_view_patient_lastname_label = tk.Label(self.patient_view_new_patient_frame, text='Apellidos:', foreground=self.ANTI_FLASH_WHITE, font=self.REGULAR_FONT, bg=self.OUTER_SPACE, justify='right')
        self.patient_view_patient_gender_label = tk.Label(self.patient_view_new_patient_frame, text='Género:', foreground=self.ANTI_FLASH_WHITE, font=self.REGULAR_FONT, bg=self.OUTER_SPACE, justify='right')
        self.patient_view_patient_contact_information = tk.Label(self.patient_view_new_patient_frame, text='Información de Contacto del Paciente:', foreground=self.EART_YELLOW, font=self.REGULAR_FONT, bg=self.OUTER_SPACE, justify='left')
        self.patient_view_patient_measures_information = tk.Label(self.patient_view_new_patient_frame, text='Información de las medidas del Paciente:', foreground=self.EART_YELLOW, font=self.REGULAR_FONT, bg=self.OUTER_SPACE, justify='left')
        self.patient_view_patient_phone_label = tk.Label(self.patient_view_new_patient_frame, text='Teléfono:', foreground=self.ANTI_FLASH_WHITE, font=self.REGULAR_FONT, bg=self.OUTER_SPACE, justify='right')
        self.patient_view_patient_right_leg_size_label = tk.Label(self.patient_view_new_patient_frame, text='Medida Pierna Derecha:', foreground=self.ANTI_FLASH_WHITE, font=self.REGULAR_FONT, bg=self.OUTER_SPACE, justify='right')
        self.patient_view_patient_left_leg_size_label = tk.Label(self.patient_view_new_patient_frame, text='Medida Pierna Izquierda:', foreground=self.ANTI_FLASH_WHITE, font=self.REGULAR_FONT, bg=self.OUTER_SPACE, justify='right')
        self.patient_view_patient_mail_label = tk.Label(self.patient_view_new_patient_frame, text='Correo:', foreground=self.ANTI_FLASH_WHITE, font=self.REGULAR_FONT, bg=self.OUTER_SPACE, justify='right')
                # New Patients Entrys:
        self.patient_view_patient_ci_entry = tk.Entry(self.patient_view_new_patient_frame, font=self.REGULAR_FONT, foreground=self.ONYX, bg=self.ANTI_FLASH_WHITE, width=30)
        self.patient_view_birthdate_frame = tk.Frame(self.patient_view_new_patient_frame, bg=self.OUTER_SPACE)
        self.patient_view_patient_birthdate_day_entry = tk.Entry(self.patient_view_birthdate_frame, font=self.REGULAR_FONT, foreground=self.ONYX, bg=self.ANTI_FLASH_WHITE, width=3)
        self.patient_view_patient_birthdate_month_entry = tk.Entry(self.patient_view_birthdate_frame, font=self.REGULAR_FONT, foreground=self.ONYX, bg=self.ANTI_FLASH_WHITE, width=3)
        self.patient_view_patient_birthdate_year_entry = tk.Entry(self.patient_view_birthdate_frame, font=self.REGULAR_FONT, foreground=self.ONYX, bg=self.ANTI_FLASH_WHITE, width=5)
        self.patient_view_patient_name_entry = tk.Entry(self.patient_view_new_patient_frame, font=self.REGULAR_FONT, foreground=self.ONYX, bg=self.ANTI_FLASH_WHITE, width=30)
        self.patient_view_patient_lastname_entry = tk.Entry(self.patient_view_new_patient_frame, font=self.REGULAR_FONT, foreground=self.ONYX, bg=self.ANTI_FLASH_WHITE, width=30)
        self.patient_view_checkbutton_frame = tk.Frame(self.patient_view_new_patient_frame, bg=self.OUTER_SPACE)
        self.patient_view_check_var = tk.IntVar()
        self.patient_view_patient_gender_male_checkbutton = tk.Radiobutton(self.patient_view_checkbutton_frame, font=self.REGULAR_FONT, foreground=self.ANTI_FLASH_WHITE, bg=self.OUTER_SPACE, text='M', variable=self.patient_view_check_var, value=1, selectcolor=self.BITTERSWEET_SHIMMER)
        self.patient_view_patient_gender_female_checkbutton = tk.Radiobutton(self.patient_view_checkbutton_frame, font=self.REGULAR_FONT, foreground=self.ANTI_FLASH_WHITE, bg=self.OUTER_SPACE, text='F', variable=self.patient_view_check_var, value=2, selectcolor=self.BITTERSWEET_SHIMMER)
        self.patient_view_patient_phone_entry = tk.Entry(self.patient_view_new_patient_frame, font=self.REGULAR_FONT, foreground=self.ONYX, bg=self.ANTI_FLASH_WHITE, width=30)
        self.patient_view_patient_right_leg_size_entry = tk.Entry(self.patient_view_new_patient_frame, font=self.REGULAR_FONT, foreground=self.ONYX, bg=self.ANTI_FLASH_WHITE, width=30)
        self.patient_view_patient_left_leg_size_entry = tk.Entry(self.patient_view_new_patient_frame, font=self.REGULAR_FONT, foreground=self.ONYX, bg=self.ANTI_FLASH_WHITE, width=30)
        self.patient_view_patient_mail_entry = tk.Entry(self.patient_view_new_patient_frame, font=self.REGULAR_FONT, foreground=self.ONYX, bg=self.ANTI_FLASH_WHITE, width=30)
                # New Patients Buttoms:
        self.patient_view_buttom_frame = tk.Frame(self.patient_view_new_patient_frame, bg=self.OUTER_SPACE)
        self.patient_view_cancel_buttom = tk.Button(self.patient_view_buttom_frame, font=self.REGULAR_FONT, bg=self.ONYX, foreground=self.ANTI_FLASH_WHITE, activebackground=self.ANTI_FLASH_WHITE, activeforeground=self.ONYX, text="Cancelar")
        self.patient_view_register_buttom = tk.Button(self.patient_view_buttom_frame, font=self.REGULAR_FONT, bg=self.EART_YELLOW, foreground=self.ONYX, activebackground=self.ANTI_FLASH_WHITE, activeforeground=self.ONYX, text="Registrar")
            # Search Patient Frame Components
                # Options Frame
        self.patient_search_view_top_frame = tk.Frame(self.patient_view_search_patient_frame, bg=self.OUTER_SPACE)
        self.patient_search_view_bottom_frame = tk.Frame(self.patient_view_search_patient_frame, bg=self.OUTER_SPACE)
                # Top Frame Components
        self.patient_search_view_top_label = tk.Label(self.patient_search_view_top_frame, text='Cédula de Identidad (CI):', foreground=self.ANTI_FLASH_WHITE, font=self.REGULAR_FONT, bg=self.OUTER_SPACE, justify='right')
        self.patient_search_view_top_entry = tk.Entry(self.patient_search_view_top_frame, font=self.REGULAR_FONT, foreground=self.ONYX, bg=self.ANTI_FLASH_WHITE, width=15)
        self.patient_search_view_top_search_buttom = tk.Button(self.patient_search_view_top_frame, font=self.REGULAR_FONT, bg=self.ONYX, foreground=self.ANTI_FLASH_WHITE, activebackground=self.ANTI_FLASH_WHITE, activeforeground=self.ONYX, text="Buscar")
        self.patient_search_view_top_search_all_buttom = tk.Button(self.patient_search_view_top_frame, font=self.REGULAR_FONT, bg=self.ONYX, foreground=self.ANTI_FLASH_WHITE, activebackground=self.ANTI_FLASH_WHITE, activeforeground=self.ONYX, text="Listar")
                # Bottom Frame Components
        self.style_config.configure('TScrollbar', width=30, background=self.ONYX, troughcolor=self.ANTI_FLASH_WHITE, gripcount=0, relief='flat', borderwidth=0)
        self.patient_search_view_scroll = ttk.Scrollbar(self.patient_search_view_bottom_frame, orient=tk.VERTICAL, style='TScrollbar')
        self.patient_search_view_conteiner_canvas = tk.Canvas(self.patient_search_view_bottom_frame, bg=self.OUTER_SPACE, highlightthickness=0, yscrollcommand = self.patient_search_view_scroll.set)
        self.patient_search_view_conteiner_frame = tk.Frame(self.patient_search_view_conteiner_canvas, bg=self.OUTER_SPACE)
                # Patient information components
        self.patient_search_get_ci_frame = tk.Frame(self.patient_search_view_conteiner_frame, bg=self.OUTER_SPACE)
        self.patient_search_get_ci_label = tk.Label(self.patient_search_get_ci_frame, text='', foreground=self.ANTI_FLASH_WHITE, font=self.BLACK_REGULAR_FONT, bg=self.OUTER_SPACE, justify='left')
        self.patient_search_focus_ci_label = tk.Label(self.patient_search_get_ci_frame, text='', foreground=self.EART_YELLOW, font=self.REGULAR_FONT, bg=self.OUTER_SPACE, justify='left')
        self.patient_search_get_full_name_frame = tk.Frame(self.patient_search_view_conteiner_frame, bg=self.OUTER_SPACE)
        self.patient_search_get_full_name_label = tk.Label(self.patient_search_get_full_name_frame, text='', foreground=self.ANTI_FLASH_WHITE, font=self.BLACK_REGULAR_FONT, bg=self.OUTER_SPACE, justify='left')
        self.patient_search_focus_full_name_label = tk.Label(self.patient_search_get_full_name_frame, text='', foreground=self.ANTI_FLASH_WHITE, font=self.REGULAR_FONT, bg=self.OUTER_SPACE, justify='left')
        self.patient_search_get_birthdate_frame = tk.Frame(self.patient_search_view_conteiner_frame, bg=self.OUTER_SPACE)
        self.patient_search_get_birthdate_label = tk.Label(self.patient_search_get_birthdate_frame, text='', foreground=self.ANTI_FLASH_WHITE, font=self.BLACK_REGULAR_FONT, bg=self.OUTER_SPACE, justify='left')
        self.patient_search_focus_birthdate_label = tk.Label(self.patient_search_get_birthdate_frame, text='', foreground=self.ANTI_FLASH_WHITE, font=self.REGULAR_FONT, bg=self.OUTER_SPACE, justify='left')
        self.patient_search_get_age_frame = tk.Frame(self.patient_search_view_conteiner_frame, bg=self.OUTER_SPACE)
        self.patient_search_get_age_label = tk.Label(self.patient_search_get_age_frame, text='', foreground=self.ANTI_FLASH_WHITE, font=self.BLACK_REGULAR_FONT, bg=self.OUTER_SPACE, justify='left')
        self.patient_search_focus_age_label = tk.Label(self.patient_search_get_age_frame, text='', foreground=self.ANTI_FLASH_WHITE, font=self.REGULAR_FONT, bg=self.OUTER_SPACE, justify='left')
        self.patient_search_get_gender_frame = tk.Frame(self.patient_search_view_conteiner_frame, bg=self.OUTER_SPACE)
        self.patient_search_get_gender_label = tk.Label(self.patient_search_get_gender_frame, text='', foreground=self.ANTI_FLASH_WHITE, font=self.BLACK_REGULAR_FONT, bg=self.OUTER_SPACE, justify='left')
        self.patient_search_focus_gender_label = tk.Label(self.patient_search_get_gender_frame, text='', foreground=self.ANTI_FLASH_WHITE, font=self.REGULAR_FONT, bg=self.OUTER_SPACE, justify='left')
        self.patient_search_get_phone_frame = tk.Frame(self.patient_search_view_conteiner_frame, bg=self.OUTER_SPACE)
        self.patient_search_get_phone_label = tk.Label(self.patient_search_get_phone_frame, text='', foreground=self.ANTI_FLASH_WHITE, font=self.BLACK_REGULAR_FONT, bg=self.OUTER_SPACE, justify='left')
        self.patient_search_focus_phone_entry = tk.Entry(self.patient_search_get_phone_frame, font=self.REGULAR_FONT, foreground=self.ONYX, bg=self.ANTI_FLASH_WHITE, width=20)
        self.patient_search_focus_phone_label = tk.Label(self.patient_search_get_phone_frame, text='', foreground=self.ANTI_FLASH_WHITE, font=self.REGULAR_FONT, bg=self.OUTER_SPACE, justify='left')
        self.patient_search_get_mail_frame = tk.Frame(self.patient_search_view_conteiner_frame, bg=self.OUTER_SPACE)
        self.patient_search_get_mail_label = tk.Label(self.patient_search_get_mail_frame, text='', foreground=self.ANTI_FLASH_WHITE, font=self.BLACK_REGULAR_FONT, bg=self.OUTER_SPACE, justify='left')
        self.patient_search_focus_mail_label = tk.Label(self.patient_search_get_mail_frame, text='', foreground=self.ANTI_FLASH_WHITE, font=self.REGULAR_FONT, bg=self.OUTER_SPACE, justify='left')
        self.patient_search_focus_mail_entry = tk.Entry(self.patient_search_get_mail_frame, font=self.REGULAR_FONT, foreground=self.ONYX, bg=self.ANTI_FLASH_WHITE, width=30)
        
        self.patient_search_get_right_leg_size_frame = tk.Frame(self.patient_search_view_conteiner_frame, bg=self.OUTER_SPACE)
        self.patient_search_get_right_leg_size_label = tk.Label(self.patient_search_get_right_leg_size_frame, text='', foreground=self.ANTI_FLASH_WHITE, font=self.BLACK_REGULAR_FONT, bg=self.OUTER_SPACE, justify='left')
        self.patient_search_focus_right_leg_size_label = tk.Label(self.patient_search_get_right_leg_size_frame, text='', foreground=self.ANTI_FLASH_WHITE, font=self.REGULAR_FONT, bg=self.OUTER_SPACE, justify='left')
        self.patient_search_focus_right_leg_size_entry = tk.Entry(self.patient_search_get_right_leg_size_frame, font=self.REGULAR_FONT, foreground=self.ONYX, bg=self.ANTI_FLASH_WHITE, width=10)
        
        self.patient_search_get_left_leg_size_frame = tk.Frame(self.patient_search_view_conteiner_frame, bg=self.OUTER_SPACE)
        self.patient_search_get_left_leg_size_label = tk.Label(self.patient_search_get_left_leg_size_frame, text='', foreground=self.ANTI_FLASH_WHITE, font=self.BLACK_REGULAR_FONT, bg=self.OUTER_SPACE, justify='left')
        self.patient_search_focus_left_leg_size_label = tk.Label(self.patient_search_get_left_leg_size_frame, text='', foreground=self.ANTI_FLASH_WHITE, font=self.REGULAR_FONT, bg=self.OUTER_SPACE, justify='left')
        self.patient_search_focus_left_leg_size_entry = tk.Entry(self.patient_search_get_left_leg_size_frame, font=self.REGULAR_FONT, foreground=self.ONYX, bg=self.ANTI_FLASH_WHITE, width=10)
        
        self.patient_search_button_gruop_frame = tk.Frame(self.patient_search_view_conteiner_frame, bg=self.OUTER_SPACE)
        self.patient_search_delete_buttom = tk.Button(self.patient_search_button_gruop_frame, font=self.REGULAR_FONT, bg=self.BITTERSWEET_SHIMMER, foreground=self.ANTI_FLASH_WHITE, activebackground=self.ANTI_FLASH_WHITE, activeforeground=self.BITTERSWEET_SHIMMER, text="Eliminar")
        self.patient_search_update_buttom = tk.Button(self.patient_search_button_gruop_frame, font=self.REGULAR_FONT, bg=self.ONYX, foreground=self.ANTI_FLASH_WHITE, activebackground=self.ANTI_FLASH_WHITE, activeforeground=self.ONYX, text="Modificar")
        self.patient_search_folder_buttom = tk.Button(self.patient_search_button_gruop_frame, font=self.REGULAR_FONT, bg=self.ONYX, foreground=self.ANTI_FLASH_WHITE, activebackground=self.ANTI_FLASH_WHITE, activeforeground=self.ONYX, text="Carpeta")
        self.patient_search_report_buttom = tk.Button(self.patient_search_button_gruop_frame, font=self.REGULAR_FONT, bg=self.ONYX, foreground=self.ANTI_FLASH_WHITE, activebackground=self.ANTI_FLASH_WHITE, activeforeground=self.ONYX, text="Reportes")
        self.patient_search_take_buttom = tk.Button(self.patient_search_button_gruop_frame, font=self.REGULAR_FONT, bg=self.EART_YELLOW, foreground=self.ONYX, activebackground=self.ONYX, activeforeground=self.EART_YELLOW, text="Análisis")
        
        self.patient_search_upper_level_search_pdf_window:tk.Toplevel|None = None
        self.patient_search_upper_level_label:tk.Label|None = None
        self.patient_search_upper_level_combobox:ttk.Combobox|None = None
        self.patient_search_upper_level_button:tk.Button|None = None
        self.patient_search_upper_level_cancel_button:tk.Button|None = None
        
            # Page Components Configure
        self.patient_view_create_buttom.configure(command=self.build_create_patient_view)
        self.patient_view_search_buttom.configure(command=self.build_search_patient_view)
        self.patient_search_view_conteiner_canvas.create_window((0, 0), window=self.patient_search_view_conteiner_frame, anchor='nw')
        self.patient_search_view_scroll.configure(command=self.patient_search_view_conteiner_canvas.yview)
        self.patient_view_exit_buttom.configure(command=self.controller.search_logout_buttom)
        self.patient_view_cancel_buttom.configure(command=self.create_cancel_buttom)
        self.patient_view_register_buttom.configure(command=self.create_buttom)
        self.patient_search_view_top_search_buttom.configure(command=self.build_search_patient_result_view)
        self.patient_search_view_top_search_all_buttom.configure(command=self.build_list_of_patients_view)
        self.patient_search_delete_buttom.configure(command=self.build_delete_patient_view)
        self.patient_search_update_buttom.configure(command=self.build_update_patient_view)
        self.patient_search_folder_buttom.configure(command=self.controller.open_patient_folder)
        self.patient_search_take_buttom.configure(command=self.controller.launch_analytics_view) 
        self.patient_search_report_buttom.configure(command=self.build_search_pdf_view)
    
    def build_main_patient_view (self):
        self.widget_pack_forget(self.root)
        self.root.title("SAZPF/Patients")
        self.root.state('zoomed')
        self.patient_view_top_frame.pack(side='top', fill='x')
        self.patient_view_bottom_frame.pack(side='bottom', fill='both', expand=True)
        self.patient_view_top_frame_logo_label.pack(side='left', padx=10, pady=10, ipadx=10)
        self.patient_view_top_frame_title_label.pack(side='left', pady=10)
        self.patient_view_top_frame_user_name_label.pack(side='right', anchor='e', padx=10)
        self.patient_view_main_buttons_frame.pack(side='top', fill='x', anchor='n')
        self.patient_view_create_buttom.pack(side='left', anchor='w')
        self.patient_view_search_buttom.pack(side='left', anchor='w')
        self.patient_view_exit_buttom.pack(side='right', anchor='e')
        self.patient_view_main_buttons_frame_separator.pack(side='bottom', fill='x')
    
    def build_create_patient_view (self):
        self.widget_pack_forget(self.patient_view_bottom_frame)
        self.patient_view_main_buttons_frame.pack(side='top', fill='x', anchor='n')
        self.patient_view_new_patient_frame.pack(side='bottom', fill='both', expand=True)
        self.widget_pack_forget(self.patient_view_new_patient_frame)
            # Labels Grid:
        self.patient_view_main_information_label.grid(column=0, row=0, padx=10, pady=10, columnspan=5, sticky='W')
        self.patient_view_patient_ci_label.grid(column=0, row=1, padx=10, pady=10, columnspan=1, sticky='E')
        self.patient_view_patient_birthdate_label.grid(column=2, row=1, padx=10, pady=10, columnspan=1, sticky='E')
        self.patient_view_patient_name_label.grid(column=0, row=2, padx=10, pady=10, columnspan=1, sticky='E')
        self.patient_view_patient_lastname_label.grid(column=0, row=3, padx=10, pady=10, columnspan=1, sticky='E')
        self.patient_view_patient_gender_label.grid(column=2, row=2, padx=10, pady=10, columnspan=1, sticky='E')
        self.patient_view_patient_contact_information.grid(column=0, row=4, padx=10, pady=10, columnspan=2, sticky='W')
        self.patient_view_patient_measures_information.grid(column=2, row=4, padx=10, pady=10, columnspan=2, sticky='W')
        self.patient_view_patient_phone_label.grid(column=0, row=5, padx=10, pady=10, columnspan=1, sticky='E')
        self.patient_view_patient_right_leg_size_label.grid(column=2, row=5, padx=10, pady=10, columnspan=1, sticky='E')
        self.patient_view_patient_mail_label.grid(column=0, row=6, padx=10, pady=10, columnspan=1, sticky='E')
        self.patient_view_patient_left_leg_size_label.grid(column=2, row=6, padx=10, pady=10, columnspan=1, sticky='E')
            # Entrys Grid
        self.patient_view_patient_ci_entry.grid(column=1, row=1, padx=10, pady=10, columnspan=1, sticky='E')
        self.patient_view_birthdate_frame.grid(column=3, row=1, columnspan=3, sticky='W')
        self.widget_grid_forget(self.patient_view_birthdate_frame)
        self.patient_view_patient_birthdate_day_entry.grid(column=0, row=0, padx=10, pady=10, columnspan=1, sticky='W')
        self.patient_view_patient_birthdate_month_entry.grid(column=1, row=0, padx=10, pady=10, columnspan=1, sticky='W')
        self.patient_view_patient_birthdate_year_entry.grid(column=2, row=0, padx=10, pady=10, columnspan=1, sticky='W')
        self.patient_view_patient_name_entry.grid(column=1, row=2, padx=10, pady=10, columnspan=1, sticky='E')
        self.patient_view_patient_lastname_entry.grid(column=1, row=3, padx=10, pady=10, columnspan=1, sticky='E')
        self.patient_view_checkbutton_frame.grid(column=3, row=2, columnspan=1, sticky='W')
        self.widget_grid_forget(self.patient_view_checkbutton_frame)
        self.patient_view_patient_gender_male_checkbutton.grid(column=0, row=0, padx=10, pady=10, columnspan=1, sticky='E')
        self.patient_view_patient_gender_female_checkbutton.grid(column=1, row=0, padx=10, pady=10, columnspan=1, sticky='E')
        self.patient_view_patient_phone_entry.grid(column=1, row=5, padx=10, pady=10, columnspan=1, sticky='E')
        self.patient_view_patient_right_leg_size_entry.grid(column=3, row=5, padx=10, pady=10, columnspan=1, sticky='E')
        self.patient_view_patient_mail_entry.grid(column=1, row=6, padx=10, pady=10, columnspan=1, sticky='E')
        self.patient_view_patient_left_leg_size_entry.grid(column=3, row=6, padx=10, pady=10, columnspan=1, sticky='E')
            # Buttoms Grid
        self.patient_view_buttom_frame.grid(column=3, row=7, columnspan=3, sticky='E')
        self.patient_view_cancel_buttom.grid(column=0, row=0, padx=10, pady=10, columnspan=1, sticky='E')
        self.patient_view_register_buttom.grid(column=1, row=0, padx=10, pady=10, columnspan=1, sticky='E')
            # Frame Components Configure        
        self.patient_view_create_buttom.configure(background=self.EART_YELLOW)
        self.patient_view_create_buttom.configure(foreground=self.ONYX)
        self.patient_view_search_buttom.configure(background=self.ANTI_FLASH_WHITE)
        self.patient_view_search_buttom.configure(foreground=self.ONYX)
        self.patient_view_patient_gender_male_checkbutton.deselect()
        self.patient_view_patient_gender_female_checkbutton.deselect()
    
    def create_cancel_buttom (self):
        self.patient_view_patient_ci_entry.delete(0, tk.END)
        self.patient_view_patient_birthdate_day_entry.delete(0, tk.END)
        self.patient_view_patient_birthdate_month_entry.delete(0, tk.END)
        self.patient_view_patient_birthdate_year_entry.delete(0, tk.END)
        self.patient_view_patient_name_entry.delete(0, tk.END)
        self.patient_view_patient_lastname_entry.delete(0, tk.END)
        self.patient_view_patient_gender_male_checkbutton.deselect()
        self.patient_view_patient_gender_female_checkbutton.deselect()
        self.patient_view_patient_phone_entry.delete(0, tk.END)
        self.patient_view_patient_mail_entry.delete(0, tk.END)
    
    def create_buttom (self):
        create_patient = self.controller.create_new_patient()
        if create_patient[0]:
            if create_patient[1] == 'Success':
                self.show_info(create_patient[1], create_patient[2])
                self.build_search_patient_view()
                self.patient_search_view_top_entry.delete(0, tk.END)
                self.patient_search_view_top_entry.insert(0, self.patient_view_patient_ci_entry.get())
                self.build_search_patient_result_view()
            else:
                self.show_error(create_patient[1], create_patient[2])
            self.patient_view_patient_ci_entry.delete(0, tk.END)
            self.patient_view_patient_birthdate_day_entry.delete(0, tk.END)
            self.patient_view_patient_birthdate_month_entry.delete(0, tk.END)
            self.patient_view_patient_birthdate_year_entry.delete(0, tk.END)
            self.patient_view_patient_name_entry.delete(0, tk.END)
            self.patient_view_patient_lastname_entry.delete(0, tk.END)
            self.patient_view_patient_gender_male_checkbutton.deselect()
            self.patient_view_patient_gender_female_checkbutton.deselect()
            self.patient_view_patient_phone_entry.delete(0, tk.END)
            self.patient_view_patient_mail_entry.delete(0, tk.END)
        else:
            self.show_error(create_patient[1], create_patient[2])
    
    def build_search_patient_view (self):
        self.widget_pack_forget(self.patient_view_bottom_frame)
        self.patient_view_main_buttons_frame.pack(side='top', fill='x', anchor='n')
        self.patient_view_search_patient_frame.pack(side='bottom', fill='both', expand=True)
        self.widget_pack_forget(self.patient_view_search_patient_frame)
            # Top Frame
        self.patient_search_view_top_frame.pack(side='top', fill='x', anchor='n')
        self.widget_pack_forget(self.patient_search_view_top_frame)
        self.patient_search_view_top_label.pack(side='left', anchor='w', padx=10, pady=10)
        self.patient_search_view_top_entry.pack(side='left', anchor='w', padx=10, pady=10)
        self.patient_search_view_top_entry.delete(0, tk.END)
        self.patient_search_view_top_search_buttom.pack(side='left', anchor='w', padx=10, pady=10)
        self.patient_search_view_top_search_all_buttom.pack(side='left', anchor='w', padx=10, pady=10)
            # Bottom Frame
        self.patient_search_view_bottom_frame.pack(side='bottom', fill='both', expand=True)
        self.widget_pack_forget(self.patient_search_view_bottom_frame)
        self.patient_search_view_scroll.pack(side='right', anchor='e', fill='y')
        self.patient_search_view_conteiner_canvas.pack(side='left', anchor='w', fill='both', expand=True )
        self.widget_grid_forget(self.patient_search_view_conteiner_frame)        
            # Frame Components Configure
        self.patient_view_create_buttom.configure(background=self.ANTI_FLASH_WHITE)
        self.patient_view_create_buttom.configure(foreground=self.ONYX)
        self.patient_view_search_buttom.configure(background=self.EART_YELLOW)
        self.patient_view_search_buttom.configure(foreground=self.ONYX)
    
    def build_search_patient_result_view (self):
        self.widget_grid_forget(self.patient_search_view_conteiner_frame)
        if self.patient_search_view_top_entry.get() != '':
            patient:PatientController = self.controller.search_pattient_by_ci()
            if patient:
                self.patient_search_get_ci_frame.grid(column=0, row=0, padx=10, columnspan=1, sticky='W')
                self.widget_grid_forget(self.patient_search_get_ci_frame)
                self.patient_search_get_ci_label.grid(column=0, row=0, padx=10, pady=10, columnspan=1, sticky='W')
                self.patient_search_focus_ci_label.grid(column=1, row=0, pady=10, columnspan=1, sticky='W')
                self.patient_search_get_full_name_frame.grid(column=0, row=1, padx=10, columnspan=1, sticky='W')
                self.widget_grid_forget(self.patient_search_get_full_name_frame)
                self.patient_search_get_full_name_label.grid(column=0, row=0, padx=10, pady=10, columnspan=1, sticky='W')
                self.patient_search_focus_full_name_label.grid(column=1, row=0, pady=10, columnspan=1, sticky='W')
                self.patient_search_get_gender_frame.grid(column=1, row=1, padx=10, columnspan=1, sticky='W')
                self.widget_grid_forget(self.patient_search_get_gender_frame)
                self.patient_search_get_gender_label.grid(column=0, row=0, padx=10, pady=10, columnspan=1, sticky='W')
                self.patient_search_focus_gender_label.grid(column=1, row=0, pady=10, columnspan=1, sticky='W')
                
                self.patient_search_get_right_leg_size_frame.grid(column=2, row=1, padx=10, columnspan=1, sticky='W')
                self.widget_grid_forget(self.patient_search_get_right_leg_size_frame)
                self.patient_search_get_right_leg_size_label.grid(column=0, row=0, padx=10, pady=10, columnspan=1, sticky='W')
                self.patient_search_focus_right_leg_size_label.grid(column=1, row=0, pady=10, columnspan=1, sticky='W')
                
                
                self.patient_search_get_birthdate_frame.grid(column=0, row=2, padx=10, columnspan=1, sticky='W')
                self.widget_grid_forget(self.patient_search_get_birthdate_frame)
                self.patient_search_get_birthdate_label.grid(column=0, row=0, padx=10, pady=10, columnspan=1, sticky='W')
                self.patient_search_focus_birthdate_label.grid(column=1, row=0, pady=10, columnspan=1, sticky='W')
                self.patient_search_get_age_frame.grid(column=1, row=2, padx=10, columnspan=1, sticky='W')
                self.widget_grid_forget(self.patient_search_get_age_frame)
                self.patient_search_get_age_label.grid(column=0, row=0, padx=10, pady=10, columnspan=1, sticky='W')
                self.patient_search_focus_age_label.grid(column=1, row=0, pady=10, columnspan=1, sticky='W')
                
                self.patient_search_get_left_leg_size_frame.grid(column=2, row=2, padx=10, columnspan=1, sticky='W')
                self.widget_grid_forget(self.patient_search_get_left_leg_size_frame)
                self.patient_search_get_left_leg_size_label.grid(column=0, row=0, padx=10, pady=10, columnspan=1, sticky='W')
                self.patient_search_focus_left_leg_size_label.grid(column=1, row=0, pady=10, columnspan=1, sticky='W')
                
                self.patient_search_get_phone_frame.grid(column=1, row=3, padx=10, columnspan=1, sticky='W')
                self.widget_grid_forget(self.patient_search_get_phone_frame)
                self.patient_search_get_phone_label.grid(column=0, row=0, padx=10, pady=10, columnspan=1, sticky='W')
                self.patient_search_focus_phone_label.grid(column=1, row=0, pady=10, columnspan=1, sticky='W')
                self.patient_search_get_mail_frame.grid(column=0, row=3, padx=10, columnspan=1, sticky='W')
                self.widget_grid_forget(self.patient_search_get_mail_frame)
                self.patient_search_get_mail_label.grid(column=0, row=0, padx=10, pady=10, columnspan=1, sticky='W')
                self.patient_search_focus_mail_label.grid(column=1, row=0, pady=10, columnspan=1, sticky='W')
                self.patient_search_button_gruop_frame.grid(column=0, row=5, padx=10, columnspan=1, sticky='W')
                self.widget_grid_forget(self.patient_search_button_gruop_frame)
                self.patient_search_delete_buttom.grid(column=0, row=0, padx=10, pady=10, columnspan=1, sticky='W')
                self.patient_search_update_buttom.grid(column=1, row=0, padx=10, pady=10, columnspan=1, sticky='W')
                self.patient_search_folder_buttom.grid(column=2, row=0, padx=10, pady=10, columnspan=1, sticky='W')
                self.patient_search_report_buttom.grid(column=3, row=0, padx=10, pady=10, columnspan=1, sticky='W')
                self.patient_search_take_buttom.grid(column=4, row=0, padx=10, pady=10, columnspan=1, sticky='W')
                
                self.patient_search_get_ci_label.configure(text='CI: ')
                self.patient_search_focus_ci_label.configure(text=str(patient.ci))
                self.patient_search_get_full_name_label.configure(text='Nombre del Paciente: ')
                self.patient_search_focus_full_name_label.configure(text=patient.name)
                self.patient_search_get_birthdate_label.configure(text='Fecha de Nacimiento: ')
                self.patient_search_focus_birthdate_label.configure(text=patient.birthday)
                self.patient_search_get_age_label.configure(text='Edad: ')
                self.patient_search_focus_age_label.configure(text=str(patient.age))
                self.patient_search_get_gender_label.configure(text='Genero: ')
                self.patient_search_focus_gender_label.configure(text=patient.gender)
                self.patient_search_get_right_leg_size_label.configure(text='Medida Pierna Derecha (m): ')
                self.patient_search_focus_right_leg_size_label.configure(text=patient.right_leg_size)
                self.patient_search_get_left_leg_size_label.configure(text='Medida Pierna Izquierda (m): ')
                self.patient_search_focus_left_leg_size_label.configure(text=patient.left_leg_size)
                
                self.patient_search_get_phone_label.configure(text='Número: ')
                self.patient_search_focus_phone_label.configure(text=patient.phone)
                self.patient_search_get_mail_label.configure(text='Correo: ')
                self.patient_search_focus_mail_label.configure(text=patient.mail)
                self.patient_search_view_conteiner_frame.update_idletasks()
                self.patient_search_view_conteiner_canvas.config(scrollregion=self.patient_search_view_conteiner_canvas.bbox("all"))
            else:
                self.show_error('Search Error', 'No patient was found')
        else:
            self.show_error('Error', 'Empty CI')
    
    def focus_patient_list (self, ci):
        self.patient_search_view_top_entry.delete(0, tk.END)
        self.patient_search_view_top_entry.insert(0, ci)
        self.build_search_patient_result_view()
    
    def build_list_of_patients_view (self):
        self.widget_grid_forget(self.patient_search_view_conteiner_frame)
        self.patient_search_view_top_entry.delete(0, tk.END)
        patient_list = self.controller.search_all_pattient()
        ci_label = tk.Label(self.patient_search_view_conteiner_frame, text='CI', foreground=self.BITTERSWEET_SHIMMER, font=self.MENU_TITLE_FONT, bg=self.OUTER_SPACE, justify=tk.CENTER)
        ci_label.grid(column=0, row=0, padx=10, pady=10, columnspan=1, sticky='W')
        name_label = tk.Label(self.patient_search_view_conteiner_frame, text='Nombre', foreground=self.BITTERSWEET_SHIMMER, font=self.MENU_TITLE_FONT, bg=self.OUTER_SPACE, justify=tk.CENTER)
        name_label.grid(column=1, row=0, padx=10, pady=10, columnspan=1, sticky='W')
        age_label = tk.Label(self.patient_search_view_conteiner_frame, text='Edad', foreground=self.BITTERSWEET_SHIMMER, font=self.MENU_TITLE_FONT, bg=self.OUTER_SPACE, justify=tk.CENTER)
        age_label.grid(column=2, row=0, padx=10, pady=10, columnspan=1, sticky='W')
        gender_label = tk.Label(self.patient_search_view_conteiner_frame, text='Genero', foreground=self.BITTERSWEET_SHIMMER, font=self.MENU_TITLE_FONT, bg=self.OUTER_SPACE, justify=tk.CENTER)
        gender_label.grid(column=3, row=0, padx=10, pady=10, columnspan=1, sticky='W')
        hseparator = ttk.Separator(self.patient_search_view_conteiner_frame, orient="horizontal")
        hseparator.grid(column=0, row=1, padx=10, pady=10, columnspan=4, sticky='EW')
        row_n = 2
        for patient in patient_list:
            patient_ci_label = tk.Button(self.patient_search_view_conteiner_frame, font=self.REGULAR_FONT, borderwidth=0, bg=self.OUTER_SPACE, foreground=self.EART_YELLOW, activebackground=self.ANTI_FLASH_WHITE, activeforeground=self.OUTER_SPACE, text=str(patient[0]), command=lambda u=patient[0]: self.focus_patient_list(u))
            patient_ci_label.grid(column=0, row=row_n, padx=10, pady=10, columnspan=1, sticky='W')
            patient_name_label = tk.Label(self.patient_search_view_conteiner_frame, text=patient[1], foreground=self.ANTI_FLASH_WHITE, font=self.REGULAR_FONT, bg=self.OUTER_SPACE, justify=tk.LEFT)
            patient_name_label.grid(column=1, row=row_n, padx=10, pady=10, columnspan=1, sticky='W')
            patient_age_label = tk.Label(self.patient_search_view_conteiner_frame, text=patient[2], foreground=self.ANTI_FLASH_WHITE, font=self.REGULAR_FONT, bg=self.OUTER_SPACE, justify=tk.LEFT)
            patient_age_label.grid(column=2, row=row_n, padx=10, pady=10, columnspan=1, sticky='W')
            patient_gender_label = tk.Label(self.patient_search_view_conteiner_frame, text=patient[3], foreground=self.ANTI_FLASH_WHITE, font=self.REGULAR_FONT, bg=self.OUTER_SPACE, justify=tk.LEFT)
            patient_gender_label.grid(column=3, row=row_n, padx=10, pady=10, columnspan=1, sticky='W')
            row_n += 1
    
    def build_delete_patient_view (self):
        if self.patient_search_delete_buttom['text'] == 'Eliminar':
            res = self.ask_yes_no('Delete Patient', 'Are you sure you want to delete this patient?')
            if res:
                delete = self.controller.delete_patient()
                if delete[0]:
                    self.show_info(delete[1], delete[2])
                else:
                    self.show_error(delete[1], delete[2])
                self.widget_grid_forget(self.patient_search_get_ci_frame)
                self.widget_grid_forget(self.patient_search_button_gruop_frame)
                self.widget_grid_forget(self.patient_search_view_conteiner_frame)
        elif self.patient_search_delete_buttom['text'] == 'Cancelar':
            self.patient_search_focus_phone_entry.grid_forget()
            self.patient_search_focus_phone_label.grid(column=1, row=0, pady=10, columnspan=1, sticky='W')
            self.patient_search_focus_mail_entry.grid_forget()
            self.patient_search_focus_mail_label.grid(column=1, row=0, pady=10, columnspan=1, sticky='W')
            self.patient_search_focus_right_leg_size_entry.grid_forget()
            self.patient_search_focus_right_leg_size_label.grid(column=1, row=0, pady=10, columnspan=1, sticky='W')
            self.patient_search_focus_left_leg_size_entry.grid_forget()
            self.patient_search_focus_left_leg_size_label.grid(column=1, row=0, pady=10, columnspan=1, sticky='W')
            self.patient_search_folder_buttom.grid(column=2, row=0, padx=10, pady=10, columnspan=1, sticky='W')
            self.patient_search_report_buttom.grid(column=3, row=0, padx=10, pady=10, columnspan=1, sticky='W')
            self.patient_search_take_buttom.grid(column=4, row=0, padx=10, pady=10, columnspan=1, sticky='W')
            self.patient_search_delete_buttom.configure(text='Eliminar')
            self.patient_search_update_buttom.configure(text='Modificar')
    
    def build_update_patient_view (self):
        if self.patient_search_update_buttom['text'] == 'Modificar':
            self.patient_search_focus_phone_entry.delete(0, tk.END)
            self.patient_search_focus_phone_entry.insert(0, self.patient_search_focus_phone_label['text'])
            self.patient_search_focus_phone_label.grid_forget()
            self.patient_search_focus_phone_entry.grid(column=1, row=0, pady=10, columnspan=1, sticky='WE')
            self.patient_search_focus_mail_entry.delete(0, tk.END)
            self.patient_search_focus_mail_entry.insert(0, self.patient_search_focus_mail_label['text'])
            self.patient_search_focus_mail_label.grid_forget()
            self.patient_search_focus_mail_entry.grid(column=1, row=0, pady=10, columnspan=1, sticky='WE')
            
            self.patient_search_focus_right_leg_size_entry.delete(0, tk.END)
            self.patient_search_focus_right_leg_size_entry.insert(0, self.patient_search_focus_right_leg_size_label['text'])
            self.patient_search_focus_right_leg_size_label.grid_forget()
            self.patient_search_focus_right_leg_size_entry.grid(column=1, row=0, pady=10, columnspan=1, sticky='W')
            
            self.patient_search_focus_left_leg_size_entry.delete(0, tk.END)
            self.patient_search_focus_left_leg_size_entry.insert(0, self.patient_search_focus_left_leg_size_label['text'])
            self.patient_search_focus_left_leg_size_label.grid_forget()
            self.patient_search_focus_left_leg_size_entry.grid(column=1, row=0, pady=10, columnspan=1, sticky='W')
            
            self.patient_search_take_buttom.grid_forget()
            self.patient_search_folder_buttom.grid_forget()
            self.patient_search_report_buttom.grid_forget()
            self.patient_search_delete_buttom.configure(text='Cancelar')
            self.patient_search_update_buttom.configure(text='Guardar')
        elif self.patient_search_update_buttom['text'] == 'Guardar':
            update_status = self.controller.update_patient()
            if update_status[0]:
                self.show_info(update_status[1], update_status[2])
            else:
                self.show_error(update_status[1], update_status[2])
            self.patient_search_view_top_entry.delete(0, tk.END)
            self.patient_search_view_top_entry.insert(0, self.patient_search_focus_ci_label['text'])
            self.patient_search_update_buttom.configure(text='Modificar')
            self.patient_search_delete_buttom.configure(text='Eliminar')
            self.patient_search_focus_phone_entry.grid_forget()
            self.patient_search_focus_mail_entry.grid_forget()
            self.build_search_patient_result_view()
    
    def build_search_pdf_view  (self):     
        dates_list = self.controller.get_stride_date_patient()
        if dates_list:
            self.button_state_fun(tk.DISABLED)
            self.patient_search_upper_level_search_pdf_window = tk.Toplevel()
            def on_closing():
                self.button_state_fun(tk.NORMAL)
                self.patient_search_upper_level_search_pdf_window.destroy()
            self.patient_search_upper_level_search_pdf_window.protocol("WM_DELETE_WINDOW", on_closing)
            self.patient_search_upper_level_search_pdf_window.geometry("420x150")
            self.patient_search_upper_level_search_pdf_window.title('Abrir PDF')
            self.patient_search_upper_level_search_pdf_window.configure(background=self.OUTER_SPACE)
            
            self.patient_search_upper_level_label = tk.Label(self.patient_search_upper_level_search_pdf_window, text='Seleccionar PDF:', foreground=self.ANTI_FLASH_WHITE, font=self.BLACK_REGULAR_FONT, bg=self.OUTER_SPACE, justify='left')
            self.patient_search_upper_level_label.grid(column=0, row=0, padx=10, pady=10, sticky='E')
            self.patient_search_upper_level_combobox = ttk.Combobox(self.patient_search_upper_level_search_pdf_window, values=dates_list, style="TCombobox", width=30)
            self.patient_search_upper_level_combobox.grid(column=1, row=0, padx=10, pady=10, sticky='E')
            self.patient_search_upper_level_button = tk.Button(self.patient_search_upper_level_search_pdf_window, font=self.REGULAR_FONT, bg=self.EART_YELLOW, foreground=self.ONYX, activebackground=self.ONYX, activeforeground=self.EART_YELLOW, text="Abrir", width=10, command=self.open_pdf_buttom)
            self.patient_search_upper_level_button.grid(column=1, row=1, padx=10, pady=10, sticky='E')
            self.patient_search_upper_level_cancel_button = tk.Button(self.patient_search_upper_level_search_pdf_window, font=self.REGULAR_FONT, bg=self.EART_YELLOW, foreground=self.ONYX, activebackground=self.ONYX, activeforeground=self.EART_YELLOW, text="Cancelar", width=10, command=on_closing)
            self.patient_search_upper_level_cancel_button.grid(column=0, row=1, padx=10, pady=10, sticky='E')
        else:
            self.show_info('Error', 'No existen reportes anteriores')
    
    def button_state_fun (self, state):
        self.patient_search_delete_buttom.configure(state=state)
        self.patient_search_update_buttom.configure(state=state)
        self.patient_search_folder_buttom.configure(state=state)
        self.patient_search_report_buttom.configure(state=state)
        self.patient_search_take_buttom.configure(state=state)
    
    def open_pdf_buttom (self):
        pdf_path = self.patient_search_upper_level_combobox.get()
        self.controller.open_pdf_patient_document(pdf_path)
        self.button_state_fun(tk.NORMAL)
        self.patient_search_upper_level_search_pdf_window.destroy()
        