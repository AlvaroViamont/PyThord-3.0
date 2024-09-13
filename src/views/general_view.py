import tkinter as tk
from tkinter import ttk
import tkinter.font as fnt
from PIL import Image, ImageTk
from tkinter import messagebox
from controller import AppController
from paths import ICON_LOGO_PATH, IMG_F_PP_01_PATH, IMG_F_PP_02_PATH, IMG_F_PP_03_PATH, IMG_F_PP_04_PATH, IMG_F_PP_05_PATH, IMG_F_PP_06_PATH, IMG_F_PP_07_PATH, IMG_F_PP_08_PATH, IMG_LOGO_PATH



class General_View:
    def __init__(self, root:tk.Tk, controller:AppController):
        self.EART_YELLOW = "#FAB860"
        self.ONYX = "#32373B"
        self.OUTER_SPACE = "#4A5859"
        self.ANTI_FLASH_WHITE = "#F0F0F0"
        self.BITTERSWEET_SHIMMER = "#C83E4D"
        self.SMOKY_TOPAZ = "#935A5C"
        self.CELADON_GREEN = "#83A598"

        self.IMG_LOGO = ICON_LOGO_PATH
        self.IMG_F_PP_01 = IMG_F_PP_01_PATH
        self.IMG_F_PP_02 = IMG_F_PP_02_PATH
        self.IMG_F_PP_03 = IMG_F_PP_03_PATH
        self.IMG_F_PP_04 = IMG_F_PP_04_PATH
        self.IMG_F_PP_05 = IMG_F_PP_05_PATH
        self.IMG_F_PP_06 = IMG_F_PP_06_PATH
        self.IMG_F_PP_07 = IMG_F_PP_07_PATH
        self.IMG_F_PP_08 = IMG_F_PP_08_PATH
        self.ICON_LOGO = IMG_LOGO_PATH

        self.controller = controller
        self.root = root
        icono_img = Image.open(self.ICON_LOGO) 
        icono = ImageTk.PhotoImage(icono_img)
        self.root.iconphoto(False, icono)
        self.root.configure(background=self.OUTER_SPACE)
        self.root.geometry("{0}x{1}+0+0".format(self.root.winfo_screenwidth(), self.root.winfo_screenheight()))
        self.root.bind('<Escape>', lambda event: self.root.state('normal'))
        self.root.bind('<F11>', lambda event: self.root.state('zoomed'))
        
        self.style_config = ttk.Style()
        
        self.REGULAR_FONT = fnt.Font(family='Lato', size=16)
        self.BLACK_REGULAR_FONT = fnt.Font(family='Lato Black', size=16)
        self.TITLE_FONT = fnt.Font(family='Lato Black', size=62)
        self.SUB_TITLE_FONT = fnt.Font(family='Lato Black', size=32)
        self.REGULAR_TITLE_FONT = fnt.Font(family='Lato Black', size=24, underline=True)
        self.MENU_TITLE_FONT = fnt.Font(family='Lato Black', size=24)

        self.img_1 = ImageTk.PhotoImage(Image.open(self.IMG_LOGO))
        self.img_2 = ImageTk.PhotoImage(Image.open(self.IMG_F_PP_01))
        self.img_3 = ImageTk.PhotoImage(Image.open(self.IMG_F_PP_02))
        
        self.principal_view_top_frame = tk.Frame(self.root, bg=self.ONYX, width=self.root.winfo_screenwidth())
        self.principal_view_bottom_frame = tk.Frame(self.root, bg=self.OUTER_SPACE, height=self.root.winfo_screenheight()-60, width=self.root.winfo_screenwidth())
        
        """
            Principal Frame Components:
        """
        self.left_bottom_frame = tk.Frame(self.principal_view_bottom_frame, bg=self.OUTER_SPACE)
        self.right_bottom_frame = tk.Frame(self.principal_view_bottom_frame, bg=self.OUTER_SPACE)
        self.image_label_1 = tk.Label(self.principal_view_top_frame, image=self.img_1, bg=self.ONYX)
        self.image_label_2 = tk.Label(self.right_bottom_frame, image=self.img_2, bg=self.OUTER_SPACE)
        self.image_label_3 = tk.Label(self.left_bottom_frame, image=self.img_3, bg=self.OUTER_SPACE)
        self.title_label_logo = tk.Label(self.principal_view_top_frame, text='PyTHORD', foreground=self.ANTI_FLASH_WHITE, font=self.SUB_TITLE_FONT, bg=self.ONYX)
        self.login_buttom = tk.Button(self.principal_view_top_frame, text='Iniciar Sesión', foreground=self.EART_YELLOW, bg=self.ONYX, font=self.SUB_TITLE_FONT, borderwidth=0, activebackground=self.ONYX, activeforeground=self.ANTI_FLASH_WHITE)
        self.phrase_1_label = tk.Label(self.left_bottom_frame, text="CADA \nPASO CUENTA", foreground=self.EART_YELLOW, bg=self.OUTER_SPACE, font=self.TITLE_FONT, justify='left')
        self.phrase_2_label = tk.Label(self.left_bottom_frame, text="El camino hacia una recuperación exitosa", foreground=self.ANTI_FLASH_WHITE, bg=self.OUTER_SPACE, font=self.SUB_TITLE_FONT, justify='center')
        self.logup_buttom = tk.Button(self.left_bottom_frame, text='Empieza Ahora', foreground=self.EART_YELLOW, bg=self.OUTER_SPACE, font=self.REGULAR_TITLE_FONT, borderwidth=0, activebackground=self.OUTER_SPACE, activeforeground=self.ANTI_FLASH_WHITE)
        """
            LogIn Components:
        """
        self.login_view_top_frame = tk.Frame(self.root, bg=self.ONYX, width=self.root.winfo_screenwidth())
        self.login_view_bottom_frame = tk.Frame(self.root, bg=self.OUTER_SPACE, height=self.root.winfo_screenheight()-60, width=self.root.winfo_screenwidth())
        self.login_view_logo_label = tk.Label(self.login_view_top_frame, image=self.img_1, bg=self.ONYX)
        self.login_view_title_label = tk.Label(self.login_view_top_frame, text='PyTHORD', foreground=self.ANTI_FLASH_WHITE, font=self.SUB_TITLE_FONT, bg=self.ONYX)
        self.login_view_user_label = tk.Label(self.login_view_bottom_frame, text='Usuario:', foreground=self.ANTI_FLASH_WHITE, font=self.REGULAR_FONT, bg=self.OUTER_SPACE, justify='right')
        self.login_view_password_label = tk.Label(self.login_view_bottom_frame, text='Password:', foreground=self.ANTI_FLASH_WHITE, font=self.REGULAR_FONT, bg=self.OUTER_SPACE, justify='right')
        self.login_view_user_entry = tk.Entry(self.login_view_bottom_frame, font=self.REGULAR_FONT, foreground=self.ONYX, bg=self.ANTI_FLASH_WHITE, width=30)
        self.login_view_password_entry = tk.Entry(self.login_view_bottom_frame, font=self.REGULAR_FONT, foreground=self.ONYX, bg=self.ANTI_FLASH_WHITE, width=30, show='*')
        self.login_view_login_button = tk.Button(self.login_view_bottom_frame, font=self.REGULAR_FONT, bg=self.EART_YELLOW, foreground=self.ONYX, activebackground=self.ANTI_FLASH_WHITE, activeforeground=self.ONYX, text="Iniciar")
        self.login_view_back_button = tk.Button(self.login_view_bottom_frame, font=self.REGULAR_FONT, bg=self.ONYX, foreground=self.ANTI_FLASH_WHITE, activebackground=self.ANTI_FLASH_WHITE, activeforeground=self.ONYX, text="Atrás")
        
        self.styles_separator = ttk.Style()
        self.styles_separator.configure('top.TSeparator', background=self.ONYX)
        
        self.login_buttom.configure(command=self.controller.login_redirection)
        self.logup_buttom.configure(command=self.controller.logup_redirection)
        self.login_view_back_button.configure(command=self.principal_view)
        self.login_view_login_button.configure(command=self.controller.redirection_login_buttom)
        
        self.principal_view()

    
    def widget_pack_forget(self, frame:tk.Frame):
        for widget in frame.winfo_children():
            try:
                widget.pack_forget()
            except tk.TclError:
                pass
    
    def widget_grid_forget(self, frame:tk.Frame):
        for widget in frame.winfo_children():
            try:
                widget.grid_forget()
            except tk.TclError:
                pass
    
    def principal_view (self):
        self.widget_pack_forget (self.root)
        self.root.title("SAZPF/Pagina de Inicio")
        self.root.state('zoomed')
        self.principal_view_top_frame.pack(side='top', fill='x')
        self.principal_view_bottom_frame.pack(side='bottom', fill='both', expand=True)
        self.image_label_1.pack(side='left', padx=10, pady=10, ipadx=10)
        self.title_label_logo.pack(side='left', pady=10)
        self.login_buttom.pack(side='right', pady=10, padx=20)
        self.left_bottom_frame.grid(column=0, row=0)
        self.right_bottom_frame.grid(column=1, row=0)
        self.phrase_1_label.grid(column=0, row=0, padx=30, sticky='w')
        self.phrase_2_label.grid(column=0, row=1, padx=30, sticky='w')
        self.logup_buttom.grid(column=0, row=2, padx=80, sticky='w', pady=20)
        self.image_label_2.pack(padx=30, pady=20, side='top')
    
    def login_view (self):
        self.widget_pack_forget (self.root)
        self.root.title("SAZPF/LogIn")
        self.root.state('normal')
        self.root.geometry("520x300+400+200")
        self.login_view_top_frame.pack(side='top', fill='x')
        self.login_view_bottom_frame.pack(side='bottom', fill='both', expand=True)
        self.login_view_logo_label.pack(side='left', padx=10, pady=10, ipadx=10)
        self.login_view_title_label.pack(side='left', pady=10)
        self.login_view_user_label.grid(column=0, row=0, padx=10, pady=10)
        self.login_view_user_entry.grid(column=1, row=0, padx=10, pady=10, columnspan=2)
        self.login_view_password_label.grid(column=0, row=1, padx=10, pady=10)
        self.login_view_password_entry.grid(column=1, row=1, padx=10, pady=10, columnspan=2)
        self.login_view_login_button.grid(column=2, row=2, padx=10, pady=10, sticky='E')
        self.login_view_back_button.grid(column=0, row=2, padx=10, pady=10, sticky='E')
    
    def show_error(self, tittle, message):
        messagebox.showerror(tittle, message)
    
    def ask_yes_no(self, tittle, message):
        return messagebox.askyesno(tittle, message)
    
    def show_info(self, tittle, message):
        messagebox.showinfo(tittle, message)
    
    def show_ok_cancel (self, tittle, message):
        return messagebox.askokcancel(tittle, message)
