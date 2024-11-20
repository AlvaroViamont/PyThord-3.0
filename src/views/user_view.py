import tkinter as tk
from tkinter import ttk
from .general_view import General_View

class User_View (General_View):
    
    def __init__(self, root, controller):
        super().__init__(root, controller)
        """
            Register/Search User Components:
        """
        self.register_user_view_top_frame = tk.Frame(self.root, bg=self.ONYX, width=self.root.winfo_screenwidth())
        self.register_user_view_bottom_frame = tk.Frame(self.root, bg=self.OUTER_SPACE, height=self.root.winfo_screenheight()-60, width=self.root.winfo_screenwidth())
            # Top Frame Components:
        self.register_user_view_logo_label = tk.Label(self.register_user_view_top_frame, image=self.img_1, bg=self.ONYX)
        self.register_user_view_title_label = tk.Label(self.register_user_view_top_frame, text='PyTHORD', foreground=self.ANTI_FLASH_WHITE, font=self.SUB_TITLE_FONT, bg=self.ONYX)
        self.register_search_user_view_user_name_label = tk.Label(self.register_user_view_top_frame, text='', foreground=self.ANTI_FLASH_WHITE, font=self.SUB_TITLE_FONT, bg=self.ONYX)
            # Bottom Frame Components:
        self.register_user_view_buttons_frame = tk.Frame(self.register_user_view_bottom_frame, bg=self.OUTER_SPACE)
        self.register_user_view_forms_frame_a = tk.Frame(self.register_user_view_bottom_frame, bg=self.OUTER_SPACE)
        self.register_user_view_forms_frame_b = tk.Frame(self.register_user_view_bottom_frame, bg=self.OUTER_SPACE)
            # Buttons Frame Components:
        self.register_user_view_create_user_buttom = tk.Button(self.register_user_view_buttons_frame, bg=self.ANTI_FLASH_WHITE, activebackground=self.OUTER_SPACE, fg=self.ONYX, activeforeground=self.EART_YELLOW, text="Nuevo", font=self.MENU_TITLE_FONT, width=10)
        self.register_user_view_search_user_buttom = tk.Button(self.register_user_view_buttons_frame, bg=self.ANTI_FLASH_WHITE, activebackground=self.OUTER_SPACE, fg=self.ONYX, activeforeground=self.EART_YELLOW, text="Buscar", font=self.MENU_TITLE_FONT, width=10)
        self.register_user_view_exit_buttom = tk.Button(self.register_user_view_buttons_frame, bg=self.BITTERSWEET_SHIMMER, activebackground=self.ONYX, fg=self.ANTI_FLASH_WHITE, activeforeground=self.ANTI_FLASH_WHITE, text="Salir", font=self.MENU_TITLE_FONT, width=10)
        self.register_user_view_separator = ttk.Separator(self.register_user_view_buttons_frame, orient='horizontal', style='top.TSeparator')
            # New User
        self.register_user_view_user_name_label = tk.Label(self.register_user_view_forms_frame_a, text='Usuario:', foreground=self.ANTI_FLASH_WHITE, font=self.REGULAR_FONT, bg=self.OUTER_SPACE, justify='right')
        self.register_user_view_new_password_label = tk.Label(self.register_user_view_forms_frame_a, text='Password:', foreground=self.ANTI_FLASH_WHITE, font=self.REGULAR_FONT, bg=self.OUTER_SPACE, justify='right')
        self.register_user_view_repeat_password_label = tk.Label(self.register_user_view_forms_frame_a, text='Repeat Password:', foreground=self.ANTI_FLASH_WHITE, font=self.REGULAR_FONT, bg=self.OUTER_SPACE, justify='right')
        self.register_user_view_user_name_entry = tk.Entry(self.register_user_view_forms_frame_a, font=self.REGULAR_FONT, foreground=self.ONYX, bg=self.ANTI_FLASH_WHITE, width=60)
        self.register_user_view_new_password_entry = tk.Entry(self.register_user_view_forms_frame_a, font=self.REGULAR_FONT, foreground=self.ONYX, bg=self.ANTI_FLASH_WHITE, width=60)
        self.register_user_view_repeat_password_entry = tk.Entry(self.register_user_view_forms_frame_a, font=self.REGULAR_FONT, foreground=self.ONYX, bg=self.ANTI_FLASH_WHITE, width=60)
        self.register_user_view_cancel_buttom = tk.Button(self.register_user_view_forms_frame_a, font=self.REGULAR_FONT, bg=self.ONYX, foreground=self.ANTI_FLASH_WHITE, activebackground=self.ANTI_FLASH_WHITE, activeforeground=self.ONYX, text="Cancelar")
        self.register_user_view_registrer_buttom = tk.Button(self.register_user_view_forms_frame_a, font=self.REGULAR_FONT, bg=self.EART_YELLOW, foreground=self.ONYX, activebackground=self.ANTI_FLASH_WHITE, activeforeground=self.ONYX, text="Registrar")
            # Search User
        self.register_user_view_search_top_frame = tk.Frame(self.register_user_view_forms_frame_b, bg=self.OUTER_SPACE)
        self.register_user_view_search_bottom_frame = tk.Frame(self.register_user_view_forms_frame_b, bg=self.OUTER_SPACE)
        self.register_user_view_search_user_name_label = tk.Label(self.register_user_view_search_top_frame, text='Usuario:', foreground=self.ANTI_FLASH_WHITE, font=self.REGULAR_FONT, bg=self.OUTER_SPACE, justify='right')
        self.register_user_view_search_user_name_entry = tk.Entry(self.register_user_view_search_top_frame, font=self.REGULAR_FONT, foreground=self.ONYX, bg=self.ANTI_FLASH_WHITE, width=60)
        self.register_user_view_search_name_buttom = tk.Button(self.register_user_view_search_top_frame, font=self.REGULAR_FONT, bg=self.EART_YELLOW, foreground=self.ONYX, activebackground=self.ANTI_FLASH_WHITE, activeforeground=self.ONYX, text="Buscar Usuario")
        self.register_user_view_search_all_buttom = tk.Button(self.register_user_view_search_top_frame, font=self.REGULAR_FONT, bg=self.EART_YELLOW, foreground=self.ONYX, activebackground=self.ANTI_FLASH_WHITE, activeforeground=self.ONYX, text="Lista Usuarios")
            # Delete/Update User
        self.register_user_view_user_info_user_name_label = tk.Label(self.register_user_view_search_bottom_frame, text='', foreground=self.EART_YELLOW, font=self.SUB_TITLE_FONT, bg=self.OUTER_SPACE, justify='right')
        self.register_user_view_user_info_update_user_password_buttom = tk.Button(self.register_user_view_search_bottom_frame, font=self.REGULAR_FONT, bg=self.ANTI_FLASH_WHITE, foreground=self.ONYX, activebackground=self.ONYX, activeforeground=self.ANTI_FLASH_WHITE, text="Actualizar Contraseña")
        self.register_user_view_user_info_delete_user_buttom = tk.Button(self.register_user_view_search_bottom_frame, font=self.REGULAR_FONT, bg=self.ANTI_FLASH_WHITE, foreground=self.ONYX, activebackground=self.ONYX, activeforeground=self.ANTI_FLASH_WHITE, text="Eliminar Usuario")
            # Update Password
        self.register_user_view_update_password_label = tk.Label(self.register_user_view_search_bottom_frame, text='New Password:', foreground=self.ANTI_FLASH_WHITE, font=self.REGULAR_FONT, bg=self.OUTER_SPACE, justify='right')
        self.register_user_view_update_repeat_password_label = tk.Label(self.register_user_view_search_bottom_frame, text='Repeat Password:', foreground=self.ANTI_FLASH_WHITE, font=self.REGULAR_FONT, bg=self.OUTER_SPACE, justify='right')
        self.register_user_view_update_password_entry = tk.Entry(self.register_user_view_search_bottom_frame, font=self.REGULAR_FONT, foreground=self.ONYX, bg=self.ANTI_FLASH_WHITE, width=60)
        self.register_user_view_update_repeat_password_entry = tk.Entry(self.register_user_view_search_bottom_frame, font=self.REGULAR_FONT, foreground=self.ONYX, bg=self.ANTI_FLASH_WHITE, width=60)
        self.register_user_view_update_cancel_buttom = tk.Button(self.register_user_view_search_bottom_frame, font=self.REGULAR_FONT, bg=self.ONYX, foreground=self.ANTI_FLASH_WHITE, activebackground=self.ANTI_FLASH_WHITE, activeforeground=self.ONYX, text="Cancelar")
        self.register_user_view_update_registrer_buttom = tk.Button(self.register_user_view_search_bottom_frame, font=self.REGULAR_FONT, bg=self.EART_YELLOW, foreground=self.ONYX, activebackground=self.ANTI_FLASH_WHITE, activeforeground=self.ONYX, text="Registrar")
            # Load methods
        self.register_user_view_create_user_buttom.configure(command=self.register_new_user_buttom)
        self.register_user_view_registrer_buttom.configure(command=self.controller.create_new_user_buttom)
        self.register_user_view_cancel_buttom.configure(command=self.controller.cancel_button_funtion)
        self.register_user_view_search_user_buttom.configure(command=self.search_user_button)
        self.register_user_view_search_name_buttom.configure(command=self.update_delete_user_view_buttom)
        self.register_user_view_search_all_buttom.configure(command=self.search_all_users_buttom)
        self.register_user_view_user_info_update_user_password_buttom.configure(command=self.update_password_widget_buttom)
        self.register_user_view_update_registrer_buttom.configure(command=self.controller.update_password_buttom)
        self.register_user_view_update_cancel_buttom.configure(command=self.update_password_cancel_buttom)
        self.register_user_view_user_info_delete_user_buttom.configure(command=self.controller.delete_user_buttom)
        self.register_user_view_exit_buttom.configure(command=self.controller.logout_buttom)

    def crud_user_frame (self):
        self.widget_pack_forget(self.root)
        self.root.title("SAZPF/Users")
        self.root.state('zoomed')
        self.register_user_view_top_frame.pack(side='top', fill='x')
        self.register_user_view_bottom_frame.pack(side='bottom', fill='both', expand=True)
        self.register_user_view_logo_label.pack(side='left', padx=10, pady=10, ipadx=10)
        self.register_user_view_title_label.pack(side='left', pady=10)
        self.register_search_user_view_user_name_label.pack(side='right', anchor='e', padx=10)
        self.register_user_view_buttons_frame.pack(side='top', fill='x', anchor='n')
        self.register_user_view_create_user_buttom.pack(side='left', anchor='w')
        self.register_user_view_search_user_buttom.pack(side='left', anchor='w')
        self.register_user_view_exit_buttom.pack(side='right', anchor='e')
        self.register_user_view_separator.pack(side='bottom', fill='x')
    
    def register_new_user_buttom (self):
        self.widget_grid_forget(self.register_user_view_search_bottom_frame)
        self.register_user_view_forms_frame_b.pack_forget()
        self.register_user_view_forms_frame_a.pack(side='bottom', fill='both', expand=True)
        self.widget_pack_forget(self.register_user_view_forms_frame_a) 
            # Pack elements
        self.register_user_view_user_name_label.grid(column=0, columnspan=2, row=2, padx=10, ipady=10, pady=10, sticky='E')
        self.register_user_view_new_password_label.grid(column=0, columnspan=2, row=3, padx=10, ipady=10, pady=10, sticky='E')
        self.register_user_view_repeat_password_label.grid(column=0, columnspan=2, row=4, padx=10, ipady=10, pady=10, sticky='E')
        self.register_user_view_user_name_entry.grid(column=2, columnspan=2, row=2, padx=10, ipady=10, pady=10, sticky='E')
        self.register_user_view_new_password_entry.grid(column=2, columnspan=2, row=3, padx=10, ipady=10, pady=10, sticky='E')
        self.register_user_view_repeat_password_entry.grid(column=2, columnspan=2, row=4, padx=10, ipady=10, pady=10, sticky='E')
        self.register_user_view_cancel_buttom.grid(column=0, columnspan=2, row=6, rowspan=3, padx=10, ipady=10, pady=10, sticky='E')
        self.register_user_view_registrer_buttom.grid(column=2, columnspan=2, row=6, rowspan=3, padx=10, ipady=10, pady=10, sticky='E')
            # Set color
        self.register_user_view_create_user_buttom.configure(background=self.EART_YELLOW)
        self.register_user_view_create_user_buttom.configure(foreground=self.ONYX)
        self.register_user_view_search_user_buttom.configure(background=self.ANTI_FLASH_WHITE)
        self.register_user_view_search_user_buttom.configure(foreground=self.ONYX)
    
    def search_user_button (self):
        self.widget_grid_forget(self.register_user_view_search_bottom_frame)
        self.register_user_view_forms_frame_a.pack_forget()
        self.register_user_view_search_bottom_frame.pack_forget()
        self.register_user_view_forms_frame_b.pack(side='bottom', fill='both', expand=True)
        self.widget_pack_forget(self.register_user_view_forms_frame_b)
            # Pack elements
        self.register_user_view_search_top_frame.pack(side='top', fill='x')
        self.register_user_view_search_user_name_label.grid(column=0, columnspan=2, row=0, padx=10, ipady=10, pady=10, sticky='E')
        self.register_user_view_search_user_name_entry.grid(column=2, columnspan=2, row=0, padx=10, ipady=10, pady=10, sticky='E')
        self.register_user_view_search_name_buttom.grid(column=4, columnspan=2, row=0, padx=10, ipady=10, pady=10, sticky='E')
        self.register_user_view_search_all_buttom.grid(column=6, columnspan=2, row=0, padx=10, ipady=10, pady=10, sticky='E')
            # Set color
        self.register_user_view_create_user_buttom.configure(background=self.ANTI_FLASH_WHITE)
        self.register_user_view_create_user_buttom.configure(foreground=self.ONYX)
        self.register_user_view_search_user_buttom.configure(background=self.EART_YELLOW)
        self.register_user_view_search_user_buttom.configure(foreground=self.ONYX)

    def update_delete_user_view_buttom (self):
        self.register_user_view_search_bottom_frame.pack(side='bottom', fill='both', expand=True)
        self.widget_grid_forget(self.register_user_view_search_bottom_frame)
        user = self.register_user_view_search_user_name_entry.get()
        if user == "":
            self.show_error("Error", "Nombre de usuario vacio")
        else:
            user_data = self.controller.user_db.get_user(user)
            if user_data:
                    # Pack elements
                self.register_user_view_user_info_user_name_label.configure(text=user_data[1])
                self.register_user_view_user_info_user_name_label.grid(column=0, columnspan=4, row=0, padx=10, ipady=10, pady=10, sticky='W')
                if self.controller.login_user == self.register_user_view_user_info_user_name_label['text']:
                    self.register_user_view_user_info_update_user_password_buttom.grid(column=0, columnspan=2, row=1, padx=10, ipady=10, pady=10, sticky='W')
                    self.register_user_view_user_info_delete_user_buttom.grid(column=2, columnspan=2, row=1, padx=10, ipady=10, pady=10, sticky='W')
                elif self.controller.login_user == 'user':
                    self.register_user_view_user_info_delete_user_buttom.grid(column=2, columnspan=2, row=1, padx=10, ipady=10, pady=10, sticky='W')
            else:
                self.show_error("Error", "Usuario no encontrado")
            self.register_user_view_search_user_name_entry.delete(0, tk.END)
    
    def update_delete_unknown_user_view_buttom (self, user):
        self.register_user_view_search_bottom_frame.pack(side='bottom', fill='both', expand=True)
        self.widget_grid_forget(self.register_user_view_search_bottom_frame)
        if user == "":
            self.show_error("Error", "Nombre de usuario vacio")
        else:
            user_data = self.controller.user_db.get_user(user)
            if user_data:
                    # Pack elements
                self.register_user_view_user_info_user_name_label.configure(text=user_data[1])
                self.register_user_view_user_info_user_name_label.grid(column=0, columnspan=4, row=0, padx=10, ipady=10, pady=10, sticky='W')
                if self.controller.login_user == self.register_user_view_user_info_user_name_label['text']:
                    self.register_user_view_user_info_update_user_password_buttom.grid(column=0, columnspan=2, row=1, padx=10, ipady=10, pady=10, sticky='W')
                    self.register_user_view_user_info_delete_user_buttom.grid(column=2, columnspan=2, row=1, padx=10, ipady=10, pady=10, sticky='W')
                elif self.controller.login_user == 'user':
                    self.register_user_view_user_info_delete_user_buttom.grid(column=2, columnspan=2, row=1, padx=10, ipady=10, pady=10, sticky='W')
            else:
                self.show_error("Error", "Usuario no encontrado")
            self.register_user_view_search_user_name_entry.delete(0, tk.END)
    
    def search_all_users_buttom (self):
        self.register_user_view_search_bottom_frame.pack(side='bottom', fill='both', expand=True)
        self.widget_grid_forget(self.register_user_view_search_bottom_frame)
        user_data = self.controller.user_db.get_all_users()
        if user_data:
            c = 0
            for user in user_data:
                user_buttom = tk.Button(self.register_user_view_search_bottom_frame, font=self.REGULAR_FONT, borderwidth=0, bg=self.OUTER_SPACE, foreground=self.ANTI_FLASH_WHITE, activebackground=self.ANTI_FLASH_WHITE, activeforeground=self.OUTER_SPACE, text=user, command=lambda u=user: self.update_delete_unknown_user_view_buttom(u))
                user_buttom.grid(column=0, columnspan=2, row=c, padx=10, ipady=10, pady=10, sticky='E')
                c = c + 1
        else:
            self.show_error("Error", "Usuario no encontrado")
        self.register_user_view_search_user_name_entry.delete(0, tk.END)
    
    def update_password_widget_buttom (self):
            # Update Password
        self.register_user_view_search_bottom_frame.pack(side='bottom', fill='both', expand=True)
        self.widget_grid_forget(self.register_user_view_search_bottom_frame)
            # pack items
        self.register_user_view_update_password_label.grid(column=0, columnspan=2, row=2, padx=10, ipady=10, pady=10, sticky='W')
        self.register_user_view_update_repeat_password_label.grid(column=0, columnspan=2, row=3, padx=10, ipady=10, pady=10, sticky='W')
        self.register_user_view_update_password_entry.grid(column=2, columnspan=2, row=2, padx=10, ipady=10, pady=10, sticky='W')
        self.register_user_view_update_repeat_password_entry.grid(column=2, columnspan=2, row=3, padx=10, ipady=10, pady=10, sticky='W')
        self.register_user_view_update_cancel_buttom.grid(column=0, columnspan=2, row=4, padx=10, ipady=10, pady=10, sticky='W')
        self.register_user_view_update_registrer_buttom.grid(column=2, columnspan=2, row=4, padx=10, ipady=10, pady=10, sticky='W')
    
    def update_password_cancel_buttom (self):
        self.register_user_view_update_password_entry.delete(0, tk.END)
        self.register_user_view_update_repeat_password_entry.delete(0, tk.END)
        self.widget_grid_forget(self.register_user_view_search_bottom_frame)