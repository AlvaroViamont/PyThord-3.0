import tkinter as tk
from tkinter import ttk
from .general_view import General_View
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np


# Aplicar el estilo personalizado
plt.style.use('seaborn-v0_8-dark')  # Usar un estilo base que armonice con los colores

colors = {
    "EART_YELLOW": "#FAB860",
    "ONYX": "#32373B",
    "OUTER_SPACE": "#4A5859",
    "ANTI_FLASH_WHITE": "#F0F0F0",
    "BITTERSWEET_SHIMMER": "#C83E4D",
    "CELADON_GREEN": "#2E8B57",   
    "DEEP_CARMINE_PINK": "#EF3038",
    "SMOKY_TOPAZ": "#935A5C"
}

custom_style = {
    "axes.facecolor": colors["OUTER_SPACE"],
    "axes.edgecolor": colors["ONYX"],
    "axes.labelcolor": colors["ANTI_FLASH_WHITE"],
    "xtick.color": colors["EART_YELLOW"],
    "ytick.color": colors["EART_YELLOW"],
    "text.color": colors["ANTI_FLASH_WHITE"],
    "figure.facecolor": colors["ONYX"],
    "figure.edgecolor": colors["ONYX"],
    "grid.color": colors["CELADON_GREEN"],
    "lines.linewidth": 2.5,
    "lines.color": colors["BITTERSWEET_SHIMMER"],
    "patch.edgecolor": colors["DEEP_CARMINE_PINK"],
    "patch.facecolor": colors["BITTERSWEET_SHIMMER"],
    "axes.prop_cycle": plt.cycler('color', [
        colors["EART_YELLOW"],
        colors["BITTERSWEET_SHIMMER"],
        colors["CELADON_GREEN"],
        colors["DEEP_CARMINE_PINK"],
        colors["ANTI_FLASH_WHITE"]
    ])
}

plt.rcParams.update(custom_style)



class Analytic_View (General_View):
    
    def __init__ (self, root, controller):
        super().__init__(root, controller)
        def on_closing():
            if self.show_ok_cancel("Quit", "Do you want to quit?"):
                plt.close('all')
                self.root.destroy()

        self.root.protocol("WM_DELETE_WINDOW", on_closing)
        # Main stride view
        self.stride_view_top_frame = tk.Frame(self.root, bg=self.ONYX, width=self.root.winfo_screenwidth())
        self.stride_view_bottom_frame = tk.Frame(self.root, bg=self.OUTER_SPACE, height=self.root.winfo_screenheight()-30, width=self.root.winfo_screenwidth())
            # Top Frame Components:
        self.stride_view_top_frame_logo_label = tk.Label(self.stride_view_top_frame, image=self.img_1, bg=self.ONYX)
        self.stride_view_top_frame_title_label = tk.Label(self.stride_view_top_frame, text='PyTHORD', foreground=self.ANTI_FLASH_WHITE, font=self.SUB_TITLE_FONT, bg=self.ONYX)
        self.stride_view_top_frame_user_name_label = tk.Label(self.stride_view_top_frame, text='', foreground=self.ANTI_FLASH_WHITE, font=self.SUB_TITLE_FONT, bg=self.ONYX)
            # Bottom Frame Components:
        self.stride_view_main_buttons_frame = tk.Frame(self.stride_view_bottom_frame, bg=self.OUTER_SPACE)
        self.stride_view_components_frame = tk.Frame(self.stride_view_bottom_frame, bg=self.CELADON_GREEN)
            # Main Buttons Frame Components:
        self.stride_view_patient_information_frame = tk.Frame(self.stride_view_main_buttons_frame, bg=self.OUTER_SPACE)
        self.stride_view_patient_name_label = tk.Label(self.stride_view_patient_information_frame, text='Paciente: ', foreground=self.ANTI_FLASH_WHITE, font=self.BLACK_REGULAR_FONT, bg=self.OUTER_SPACE, justify=tk.LEFT, padx=5)
        self.stride_view_patient_full_name_label = tk.Label(self.stride_view_patient_information_frame, text='', foreground=self.ANTI_FLASH_WHITE, font=self.REGULAR_FONT, bg=self.OUTER_SPACE, justify=tk.LEFT, padx=5)
        self.stride_view_patient_title_age_label = tk.Label(self.stride_view_patient_information_frame, text='Edad: ', foreground=self.ANTI_FLASH_WHITE, font=self.BLACK_REGULAR_FONT, bg=self.OUTER_SPACE, justify=tk.LEFT, padx=5)
        self.stride_view_patient_age_label = tk.Label(self.stride_view_patient_information_frame, text='', foreground=self.ANTI_FLASH_WHITE, font=self.REGULAR_FONT, bg=self.OUTER_SPACE, justify=tk.LEFT, padx=5)
        self.stride_view_serial_conection_title_label = tk.Label(self.stride_view_patient_information_frame, text='Puerto: ', foreground=self.ANTI_FLASH_WHITE, font=self.BLACK_REGULAR_FONT, bg=self.OUTER_SPACE, justify=tk.LEFT, padx=5)
        self.stride_view_serial_conection_label = tk.Label(self.stride_view_patient_information_frame, text='Sin Conexión', foreground=self.ANTI_FLASH_WHITE, font=self.REGULAR_FONT, bg=self.OUTER_SPACE, justify=tk.LEFT, padx=5)
        self.stride_view_serial_conection_buttom = tk.Button(self.stride_view_patient_information_frame, bg=self.ONYX, activebackground=self.ANTI_FLASH_WHITE, fg=self.ANTI_FLASH_WHITE, activeforeground=self.ONYX, text="Conectar", font=self.BLACK_REGULAR_FONT, padx=5)
        self.stride_view_start_collection_buttom = tk.Button(self.stride_view_patient_information_frame, bg=self.ONYX, activebackground=self.ANTI_FLASH_WHITE, fg=self.ANTI_FLASH_WHITE, activeforeground=self.ONYX, text="Iniciar", font=self.BLACK_REGULAR_FONT, state='disabled')
        self.stride_view_serial_data_taked_label = tk.Label(self.stride_view_patient_information_frame, text='', foreground=self.ANTI_FLASH_WHITE, font=self.REGULAR_FONT, bg=self.OUTER_SPACE, justify=tk.LEFT, padx=5)
        self.stride_view_save_buttom = tk.Button(self.stride_view_patient_information_frame, bg=self.CELADON_GREEN, activebackground=self.ONYX, fg=self.ONYX, activeforeground=self.CELADON_GREEN, text="Guardar", font=self.BLACK_REGULAR_FONT, padx=5, state='disabled')
        self.stride_view_exit_buttom = tk.Button(self.stride_view_patient_information_frame, bg=self.SMOKY_TOPAZ, activebackground=self.ONYX, fg=self.ANTI_FLASH_WHITE, activeforeground=self.ANTI_FLASH_WHITE, text="Volver", font=self.BLACK_REGULAR_FONT, padx=5)
        self.stride_view_main_buttons_frame_separator = ttk.Separator(self.stride_view_main_buttons_frame, orient='horizontal', style='top.TSeparator')
        self.stride_view_top_main_buttons_frame_separator = ttk.Separator(self.stride_view_main_buttons_frame, orient='horizontal', style='top.TSeparator')
            # Lateral Menu Frame and Components:
                # Left Frame Components
        self.stride_view_components_left_frame = tk.Frame(self.stride_view_components_frame, bg=self.ONYX)
        
        self.style_config.configure('SComparative.TCombobox', foreground=self.ANTI_FLASH_WHITE, background=self.ONYX, fieldbackground=self.CELADON_GREEN)
        
        self.stride_view_time_label = tk.Label(self.stride_view_components_left_frame, text='Tiempo:', foreground=self.ANTI_FLASH_WHITE, font=self.BLACK_REGULAR_FONT, bg=self.ONYX, justify=tk.LEFT)
        
        self.time_list = [f'{i} segundos' for i in range(3, 6)]
        self.time_var = tk.StringVar
        self.stride_view_time_combobox = ttk.Combobox(self.stride_view_components_left_frame, style='SComparative.TCombobox', values=self.time_list, font=self.REGULAR_FONT, state='readonly', textvariable=self.time_var, foreground=self.ONYX, width=15)
        self.stride_view_time_combobox.current(0)
        
        self.motion_planes_var = tk.IntVar()
        self.stride_view_motion_planes_radiobuttom_label = tk.Label(self.stride_view_components_left_frame, text='Planos de Movimiento:', foreground=self.ANTI_FLASH_WHITE, font=self.BLACK_REGULAR_FONT, bg=self.ONYX, justify=tk.LEFT)
        self.stride_view_frontal_motion_planes_radiobuttom = tk.Radiobutton(self.stride_view_components_left_frame, font=self.REGULAR_FONT, foreground=self.ANTI_FLASH_WHITE, bg=self.ONYX, text='Frontal', variable=self.motion_planes_var, value=0, selectcolor=self.BITTERSWEET_SHIMMER, command=self.upload_plot_radiobuttoms)
        self.stride_view_sagittal_motion_planes_radiobuttom = tk.Radiobutton(self.stride_view_components_left_frame, font=self.REGULAR_FONT, foreground=self.ANTI_FLASH_WHITE, bg=self.ONYX, text='Sagital', variable=self.motion_planes_var, value=1, selectcolor=self.BITTERSWEET_SHIMMER, command=self.upload_plot_radiobuttoms)
        
        self.joints_var = tk.IntVar()
        self.stride_view_joints_radiobuttom_label = tk.Label(self.stride_view_components_left_frame, text='Articulaciones:', foreground=self.ANTI_FLASH_WHITE, font=self.BLACK_REGULAR_FONT, bg=self.ONYX, justify=tk.LEFT)
        self.stride_view_hip_joint_radiobuttom = tk.Radiobutton(self.stride_view_components_left_frame, font=self.REGULAR_FONT, foreground=self.ANTI_FLASH_WHITE, bg=self.ONYX, text='Cadera', variable=self.joints_var, value=0, selectcolor=self.BITTERSWEET_SHIMMER, command=self.upload_plot_radiobuttoms)
        self.stride_view_knee_joint_radiobuttom = tk.Radiobutton(self.stride_view_components_left_frame, font=self.REGULAR_FONT, foreground=self.ANTI_FLASH_WHITE, bg=self.ONYX, text='Rodilla', variable=self.joints_var, value=1, selectcolor=self.BITTERSWEET_SHIMMER, command=self.upload_plot_radiobuttoms)
        
        self.laterality_var = tk.IntVar()
        self.stride_view_laterality_radiobuttom_label = tk.Label(self.stride_view_components_left_frame, text='Lateralidad:', foreground=self.ANTI_FLASH_WHITE, font=self.BLACK_REGULAR_FONT, bg=self.ONYX, justify=tk.LEFT)
        self.stride_view_left_laterality_radiobuttom = tk.Radiobutton(self.stride_view_components_left_frame, font=self.REGULAR_FONT, foreground=self.ANTI_FLASH_WHITE, bg=self.ONYX, text='Izquierda', variable=self.laterality_var, value=2, selectcolor=self.BITTERSWEET_SHIMMER, command=self.upload_plot_radiobuttoms)
        self.stride_view_right_laterality_radiobuttom = tk.Radiobutton(self.stride_view_components_left_frame, font=self.REGULAR_FONT, foreground=self.ANTI_FLASH_WHITE, bg=self.ONYX, text='Derecha', variable=self.laterality_var, value=1, selectcolor=self.BITTERSWEET_SHIMMER, command=self.upload_plot_radiobuttoms)
        self.stride_view_ignore_laterality_radiobuttom = tk.Radiobutton(self.stride_view_components_left_frame, font=self.REGULAR_FONT, foreground=self.ANTI_FLASH_WHITE, bg=self.ONYX, text='~graf', variable=self.laterality_var, value=0, selectcolor=self.BITTERSWEET_SHIMMER, command=self.upload_plot_radiobuttoms)

                # Right Frame Components
        self.stride_view_components_right_frame = tk.Frame(self.stride_view_components_frame, bg=self.CELADON_GREEN)
        self.stride_view_left_components_right_frame_separator = ttk.Separator(self.stride_view_components_right_frame, orient='vertical', style='top.TSeparator')
                    # Right Top Frame Components
        
        self.stride_view_top_components_right_frame = tk.Frame(self.stride_view_components_right_frame, bg=self.CELADON_GREEN)
        self.stride_view_top_components_right_canvas = None
                    # Right Bottom Frame Components
        self.stride_view_bottom_components_right_frame = tk.Frame(self.stride_view_components_right_frame, bg=self.OUTER_SPACE)
        self.stride_view_bottom_components_right_frame_separator = ttk.Separator(self.stride_view_bottom_components_right_frame, orient='horizontal', style='top.TSeparator')
        self.stride_view_bottom_labels_components_right_frame = tk.Frame(self.stride_view_bottom_components_right_frame, bg=self.OUTER_SPACE)
        self.stride_view_raw_data_max_min_valor_buttom = tk.Button(self.stride_view_bottom_labels_components_right_frame, bg=self.ONYX, activebackground=self.ANTI_FLASH_WHITE, fg=self.ANTI_FLASH_WHITE, activeforeground=self.ONYX, text="Valores", font=self.BLACK_REGULAR_FONT, padx=5, state='disabled', command=self._show_general_analytics)
        
        self.stride_view_pop_win:tk.Toplevel|None = None
        self.stride_view_pop_win_top_frame:tk.Frame|None = None
        self.stride_view_pop_win_topc_frame:tk.Frame|None = None
        self.stride_view_pop_win_left_frame:tk.Frame|None = None
        self.stride_view_pop_win_left_canvas:PlotFrame|None = None
        self.stride_view_pop_win_right_frame:tk.Frame|None = None
        self.stride_view_pop_win_rightc_frame:tk.Frame|None = None
        
        
            # Configurations:
        self.stride_view_exit_buttom.configure(command=self.back_to_patient_view)
        self.stride_view_serial_conection_buttom.configure(command=self.create_canvas)
        self.stride_view_start_collection_buttom.configure(command=self.controller.collect_data)
        self.stride_view_save_buttom.configure(command=self.save_stride_view)
        self.stride_view_time_combobox.bind("<<ComboboxSelected>>", self.time_selected)
    
    def build_main_stride_view (self):
        self.widget_pack_forget(self.root)
        self.root.title("SAZPF/Strides")
        self.root.state('zoomed')
        self.stride_view_top_frame.pack(side=tk.TOP, fill='x')
        self.stride_view_bottom_frame.pack(side=tk.BOTTOM, fill='both', expand=True)
        self.stride_view_top_frame_logo_label.pack(side=tk.LEFT, padx=10, pady=10, ipadx=10)
        self.stride_view_top_frame_title_label.pack(side=tk.LEFT, pady=10)
        self.stride_view_top_frame_user_name_label.pack(side=tk.RIGHT, anchor='e', padx=10)
        self.stride_view_top_main_buttons_frame_separator.pack(side=tk.TOP, fill='x', expand=True)
        self.stride_view_main_buttons_frame.pack(side=tk.TOP, fill='x', anchor='n')
        self.stride_view_patient_information_frame.pack(side=tk.TOP, fill='x', expand=True)
        self.stride_view_patient_name_label.pack(side=tk.LEFT, anchor='w')
        self.stride_view_patient_full_name_label.pack(side=tk.LEFT, anchor='w')
        self.stride_view_patient_title_age_label.pack(side=tk.LEFT, anchor='w')
        self.stride_view_patient_age_label.pack(side=tk.LEFT, anchor='w')
        self.stride_view_serial_conection_title_label.pack(side=tk.LEFT, anchor='w')
        self.stride_view_serial_conection_label.pack(side=tk.LEFT, anchor='w')
        self.stride_view_serial_conection_buttom.pack(side=tk.LEFT, anchor='w', padx=5)
        self.stride_view_start_collection_buttom.pack(side=tk.LEFT, anchor='w', padx=5)
        self.stride_view_serial_data_taked_label.pack(side=tk.LEFT, anchor='w', padx=5)
        self.stride_view_exit_buttom.pack(side=tk.RIGHT, anchor='e', padx=5, pady=10)
        self.stride_view_save_buttom.pack(side=tk.RIGHT, anchor='e', padx=5, pady=10)
        self.stride_view_main_buttons_frame_separator.pack(side=tk.BOTTOM, fill='x', expand=True)
        self.stride_view_components_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.stride_view_components_left_frame.pack(side=tk.LEFT, fill='y')
        self.stride_view_components_right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        self.stride_view_time_label.grid(column=0, row=0, columnspan=1, padx=5, pady=10, sticky='w')
        self.stride_view_time_combobox.grid(column=1, row=0, columnspan=2, padx=5, pady=10, sticky='w')

        self.stride_view_motion_planes_radiobuttom_label.grid(column=0, row=1, columnspan=2, padx=5, pady=10, sticky='w')
        self.stride_view_frontal_motion_planes_radiobuttom.grid(column=0, row=2, columnspan=1, padx=5, pady=10, sticky='w')
        self.stride_view_sagittal_motion_planes_radiobuttom.grid(column=1, row=2, columnspan=1, padx=5, pady=10, sticky='w')
        self.stride_view_joints_radiobuttom_label.grid(column=0, row=3, columnspan=2, padx=5, pady=10, sticky='w')
        self.stride_view_hip_joint_radiobuttom.grid(column=0, row=4, columnspan=1, padx=5, pady=10, sticky='w')
        self.stride_view_knee_joint_radiobuttom.grid(column=1, row=4, columnspan=1, padx=5, pady=10, sticky='w')
        self.stride_view_laterality_radiobuttom_label.grid(column=0, row=5, columnspan=2, padx=5, pady=10, sticky='w')
        self.stride_view_left_laterality_radiobuttom.grid(column=0, row=6, columnspan=1, padx=5, pady=10, sticky='w')
        self.stride_view_right_laterality_radiobuttom.grid(column=1, row=6, columnspan=1, padx=5, pady=10, sticky='w')
        self.stride_view_ignore_laterality_radiobuttom.grid(column=2, row=6, columnspan=1, padx=5, pady=10, sticky='w')
        self.stride_view_left_components_right_frame_separator.pack(side=tk.LEFT, fill='y')
        self.stride_view_top_components_right_frame.pack(side=tk.TOP, fill='both', expand=True)
        self.stride_view_bottom_components_right_frame.pack(side=tk.BOTTOM, fill='x')
        self.stride_view_bottom_components_right_frame_separator.pack(side=tk.TOP, anchor='e', fill='x', expand=True)
        self.stride_view_bottom_labels_components_right_frame.pack(side=tk.BOTTOM, anchor='e', fill=tk.BOTH)
        self.stride_view_raw_data_max_min_valor_buttom.pack(side=tk.RIGHT, anchor='e', padx=5, pady=5, ipadx=5, ipady=5)
    
    def back_to_patient_view (self):
        try:
            self.stride_view_top_components_right_canvas.destroy_plot()
            self.stride_view_serial_data_taked_label.config(text='')
        except:
            pass
        self.controller.back_to_patient_view()
    
    def create_canvas (self):
        self.controller.get_conection()
        if not self.controller.connection_status:
            try:
                self.stride_view_top_components_right_canvas.destroy_plot()
            except:
                pass
            self.new_canvas()
        else:
            try:
                self.stride_view_serial_data_taked_label.config(text='')
                self.stride_view_top_components_right_canvas.destroy_plot()
            except:
                pass
    
    def new_canvas (self):
        self.stride_view_top_components_right_canvas = PlotFrame(self.stride_view_top_components_right_frame)

    def upload_plot_radiobuttoms (self):
        try:
            self.controller.update_plot(self.motion_planes_var.get(), self.joints_var.get(), self.laterality_var.get())
        except:
            pass
    
    def save_stride_view (self):
        if self.ask_yes_no('Salvar datos de Zancasa', '¿Está seguro de guardar los datos?'):
            self.controller.save_raw_stride()
            self.controller.make_report_pdf()

    def time_selected (self, event):
        num = self.stride_view_time_combobox.get().split(" ")
        time = int(num[0])*100
        self.controller.data.data_size = time
        self.controller.data.data_time = int(num[0])
    
    def _show_general_analytics (self):
        self.stride_view_raw_data_max_min_valor_buttom.configure(state=tk.DISABLED)
        self.stride_view_pop_win = tk.Toplevel()
        def on_closing():
            self.stride_view_raw_data_max_min_valor_buttom.configure(state=tk.NORMAL)
            self.stride_view_pop_win.destroy()
        self.stride_view_pop_win.protocol("WM_DELETE_WINDOW", on_closing)
        self.stride_view_pop_win.geometry("1000x600")
        self.stride_view_pop_win.title('Analisis numéricos')
        self.stride_view_pop_win_top_frame = tk.Frame(self.stride_view_pop_win, bg=self.OUTER_SPACE) #, width=self.stride_view_pop_win.winfo_screenwidth()
        self.stride_view_pop_win_top_frame.pack(side=tk.TOP, fill=tk.X)
        self.stride_view_pop_win_topc_frame = tk.Frame(self.stride_view_pop_win_top_frame, bg=self.OUTER_SPACE) #, width=self.stride_view_pop_win.winfo_screenwidth()
        self.stride_view_pop_win_topc_frame.pack(side=tk.TOP, fill=tk.X)
        close_buttom = tk.Button(self.stride_view_pop_win_topc_frame, bg=self.SMOKY_TOPAZ, activebackground=self.ONYX, fg=self.ANTI_FLASH_WHITE, activeforeground=self.ANTI_FLASH_WHITE, text="Cerrar", font=self.BLACK_REGULAR_FONT, padx=5, command=self.close)
        close_buttom.pack(side=tk.RIGHT, pady=10, padx=10)
        top_separator = ttk.Separator(self.stride_view_pop_win_top_frame, orient='horizontal', style='top.TSeparator')
        top_separator.pack(side=tk.TOP, anchor='e', fill='x', expand=True)
        self.stride_view_pop_win_left_frame = tk.Frame(self.stride_view_pop_win, bg=self.OUTER_SPACE) #, width=60, height=self.stride_view_pop_win.winfo_screenheight()-60
        self.stride_view_pop_win_left_frame.pack(side=tk.LEFT, fill=tk.Y)
        raw_data_buttom = tk.Button(self.stride_view_pop_win_left_frame, bg=self.ONYX, activebackground=self.ANTI_FLASH_WHITE, fg=self.ANTI_FLASH_WHITE, activeforeground=self.ONYX, text="Min/Max", font=self.BLACK_REGULAR_FONT, padx=5, width=15, command=self.generate_raw_data)
        raw_data_buttom.pack(side=tk.TOP, pady=10, padx=10)
        raw_data_calc_buttom = tk.Button(self.stride_view_pop_win_left_frame, bg=self.ONYX, activebackground=self.ANTI_FLASH_WHITE, fg=self.ANTI_FLASH_WHITE, activeforeground=self.ONYX, text="Metricas", font=self.BLACK_REGULAR_FONT, padx=5, width=15, command=self.build_metrics_data)
        raw_data_calc_buttom.pack(side=tk.TOP, pady=10, padx=10)
        self.stride_view_pop_win_right_frame = tk.Frame(self.stride_view_pop_win, bg=self.CELADON_GREEN) #, width=self.stride_view_pop_win.winfo_screenwidth-60, height=self.stride_view_pop_win.winfo_screenheight()-60
        self.stride_view_pop_win_right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        self.stride_view_pop_win_rightc_frame = tk.Frame(self.stride_view_pop_win_right_frame, bg=self.CELADON_GREEN) #, width=self.stride_view_pop_win.winfo_screenwidth-60, height=self.stride_view_pop_win.winfo_screenheight()-60
        self.stride_view_pop_win_rightc_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        left_separator = ttk.Separator(self.stride_view_pop_win_right_frame, orient='vertical', style='top.TSeparator')
        left_separator.pack(side=tk.LEFT, anchor='w', fill='y')
        
    def close(self):
        self.stride_view_raw_data_max_min_valor_buttom.configure(state=tk.NORMAL)
        self.stride_view_pop_win.destroy()

    def generate_raw_data (self):
        try:
            self.stride_view_pop_win_left_canvas.destroy_plot()
        except:
            pass
        self.widget_grid_forget(self.stride_view_pop_win_rightc_frame)
        self.widget_pack_forget(self.stride_view_pop_win_rightc_frame)
        title_label = tk.Label(self.stride_view_pop_win_rightc_frame, text='Valores mínimos y máximos', foreground=self.ONYX, font=self.SUB_TITLE_FONT, bg=self.CELADON_GREEN, justify=tk.CENTER, padx=5)
        title_label.grid(column=0, row=0, columnspan=8, pady=5, ipady=5)
        subtitle_label = tk.Label(self.stride_view_pop_win_rightc_frame, text='Sensor', foreground=self.ONYX, font=self.BLACK_REGULAR_FONT, bg=self.CELADON_GREEN, justify=tk.LEFT)
        subtitle_label.grid(column=0, row=1, pady=5, ipady=5, columnspan=8)
        
        rd = tk.Label(self.stride_view_pop_win_rightc_frame, text='Pierna Derecha:', foreground=self.ONYX, font=self.BLACK_REGULAR_FONT, bg=self.CELADON_GREEN, justify=tk.LEFT)
        rd.grid(column=0, row=2, columnspan=8, pady=2)
        rd_min_lb = tk.Label(self.stride_view_pop_win_rightc_frame, text='Rodilla (max):', foreground=self.ONYX, font=self.REGULAR_FONT, bg=self.CELADON_GREEN, justify=tk.RIGHT)
        rd_min_lb.grid(column=0, row=3, pady=2)
        rd_min_d = tk.Label(self.stride_view_pop_win_rightc_frame, text=self.controller.data.stride_angle['MaxRD'], foreground=self.ONYX, font=self.REGULAR_FONT, bg=self.CELADON_GREEN, justify=tk.LEFT)
        rd_min_d.grid(column=1, row=3, pady=2)
        rd_max_lb = tk.Label(self.stride_view_pop_win_rightc_frame, text='Rodilla (min):', foreground=self.ONYX, font=self.REGULAR_FONT, bg=self.CELADON_GREEN, justify=tk.RIGHT)
        rd_max_lb.grid(column=2, row=3, pady=2)
        rd_max_d = tk.Label(self.stride_view_pop_win_rightc_frame, text=self.controller.data.stride_angle['MinRD'], foreground=self.ONYX, font=self.REGULAR_FONT, bg=self.CELADON_GREEN, justify=tk.LEFT)
        rd_max_d.grid(column=3, row=3, pady=2)
        
        cd_min_lb = tk.Label(self.stride_view_pop_win_rightc_frame, text='Cadera (max)', foreground=self.ONYX, font=self.REGULAR_FONT, bg=self.CELADON_GREEN, justify=tk.RIGHT)
        cd_min_lb.grid(column=4, row=3, pady=2)
        cd_min_d = tk.Label(self.stride_view_pop_win_rightc_frame, text=self.controller.data.stride_angle['MaxCD'], foreground=self.ONYX, font=self.REGULAR_FONT, bg=self.CELADON_GREEN, justify=tk.LEFT)
        cd_min_d.grid(column=5, row=3, pady=2)
        cd_max_lb = tk.Label(self.stride_view_pop_win_rightc_frame, text='Cadera (min):', foreground=self.ONYX, font=self.REGULAR_FONT, bg=self.CELADON_GREEN, justify=tk.RIGHT)
        cd_max_lb.grid(column=6, row=3, pady=2)
        cd_max_d = tk.Label(self.stride_view_pop_win_rightc_frame, text=self.controller.data.stride_angle['MinCD'], foreground=self.ONYX, font=self.REGULAR_FONT, bg=self.CELADON_GREEN, justify=tk.LEFT)
        cd_max_d.grid(column=7, row=3, pady=2)
        
        ri = tk.Label(self.stride_view_pop_win_rightc_frame, text='Pierna Izquierda:', foreground=self.ONYX, font=self.BLACK_REGULAR_FONT, bg=self.CELADON_GREEN, justify=tk.CENTER)
        ri.grid(column=0, row=4, columnspan=8, pady=2)
        ri_min_lb = tk.Label(self.stride_view_pop_win_rightc_frame, text='Rodilla (max):', foreground=self.ONYX, font=self.REGULAR_FONT, bg=self.CELADON_GREEN, justify=tk.RIGHT)
        ri_min_lb.grid(column=0, row=5, pady=2)
        ri_min_d = tk.Label(self.stride_view_pop_win_rightc_frame, text=self.controller.data.stride_angle['MaxRI'], foreground=self.ONYX, font=self.REGULAR_FONT, bg=self.CELADON_GREEN, justify=tk.LEFT)
        ri_min_d.grid(column=1, row=5, pady=2)
        ri_max_lb = tk.Label(self.stride_view_pop_win_rightc_frame, text='Rodilla (min):', foreground=self.ONYX, font=self.REGULAR_FONT, bg=self.CELADON_GREEN, justify=tk.RIGHT)
        ri_max_lb.grid(column=2, row=5, pady=2)
        ri_max_d = tk.Label(self.stride_view_pop_win_rightc_frame, text=self.controller.data.stride_angle['MinRI'], foreground=self.ONYX, font=self.REGULAR_FONT, bg=self.CELADON_GREEN, justify=tk.LEFT)
        ri_max_d.grid(column=3, row=5, pady=2)
        
        ci_min_lb = tk.Label(self.stride_view_pop_win_rightc_frame, text='Cadera (max):', foreground=self.ONYX, font=self.REGULAR_FONT, bg=self.CELADON_GREEN, justify=tk.RIGHT)
        ci_min_lb.grid(column=4, row=5, pady=2)
        ci_min_d = tk.Label(self.stride_view_pop_win_rightc_frame, text=self.controller.data.stride_angle['MaxCI'], foreground=self.ONYX, font=self.REGULAR_FONT, bg=self.CELADON_GREEN, justify=tk.LEFT)
        ci_min_d.grid(column=5, row=5, pady=2)
        ci_max_lb = tk.Label(self.stride_view_pop_win_rightc_frame, text='Cadera (min):', foreground=self.ONYX, font=self.REGULAR_FONT, bg=self.CELADON_GREEN, justify=tk.RIGHT)
        ci_max_lb.grid(column=6, row=5, pady=2)
        ci_max_d = tk.Label(self.stride_view_pop_win_rightc_frame, text=self.controller.data.stride_angle['MinCI'], foreground=self.ONYX, font=self.REGULAR_FONT, bg=self.CELADON_GREEN, justify=tk.LEFT)
        ci_max_d.grid(column=7, row=5, pady=2)
        
        subtitle_label2 = tk.Label(self.stride_view_pop_win_rightc_frame, text='Calculos', foreground=self.ONYX, font=self.BLACK_REGULAR_FONT, bg=self.CELADON_GREEN, justify=tk.LEFT)
        subtitle_label2.grid(column=0, row=6, pady=5, ipady=5, columnspan=8)
        
        trd = tk.Label(self.stride_view_pop_win_rightc_frame, text='Pierna Derecha:', foreground=self.ONYX, font=self.BLACK_REGULAR_FONT, bg=self.CELADON_GREEN, justify=tk.LEFT)
        trd.grid(column=0, row=7, columnspan=8, pady=2)
        trd_min_lb = tk.Label(self.stride_view_pop_win_rightc_frame, text='Rodilla (max):', foreground=self.ONYX, font=self.REGULAR_FONT, bg=self.CELADON_GREEN, justify=tk.RIGHT)
        trd_min_lb.grid(column=0, row=8, pady=2)
        trd_min_d = tk.Label(self.stride_view_pop_win_rightc_frame, text=self.controller.data.stride_angle['TMaxRD'], foreground=self.ONYX, font=self.REGULAR_FONT, bg=self.CELADON_GREEN, justify=tk.LEFT)
        trd_min_d.grid(column=1, row=8, pady=2)
        trd_max_lb = tk.Label(self.stride_view_pop_win_rightc_frame, text='Rodilla (min):', foreground=self.ONYX, font=self.REGULAR_FONT, bg=self.CELADON_GREEN, justify=tk.RIGHT)
        trd_max_lb.grid(column=2, row=8, pady=2)
        trd_max_d = tk.Label(self.stride_view_pop_win_rightc_frame, text=self.controller.data.stride_angle['TMinRD'], foreground=self.ONYX, font=self.REGULAR_FONT, bg=self.CELADON_GREEN, justify=tk.LEFT)
        trd_max_d.grid(column=3, row=8, pady=2)
        
        tcd_min_lb = tk.Label(self.stride_view_pop_win_rightc_frame, text='Cadera (max)', foreground=self.ONYX, font=self.REGULAR_FONT, bg=self.CELADON_GREEN, justify=tk.RIGHT)
        tcd_min_lb.grid(column=4, row=8, pady=2)
        tcd_min_d = tk.Label(self.stride_view_pop_win_rightc_frame, text=self.controller.data.stride_angle['TMaxCD'], foreground=self.ONYX, font=self.REGULAR_FONT, bg=self.CELADON_GREEN, justify=tk.LEFT)
        tcd_min_d.grid(column=5, row=8, pady=2)
        tcd_max_lb = tk.Label(self.stride_view_pop_win_rightc_frame, text='Cadera (min):', foreground=self.ONYX, font=self.REGULAR_FONT, bg=self.CELADON_GREEN, justify=tk.RIGHT)
        tcd_max_lb.grid(column=6, row=8, pady=2)
        tcd_max_d = tk.Label(self.stride_view_pop_win_rightc_frame, text=self.controller.data.stride_angle['TMinCD'], foreground=self.ONYX, font=self.REGULAR_FONT, bg=self.CELADON_GREEN, justify=tk.LEFT)
        tcd_max_d.grid(column=7, row=8, pady=2)
        
        ri = tk.Label(self.stride_view_pop_win_rightc_frame, text='Pierna Izquierda:', foreground=self.ONYX, font=self.BLACK_REGULAR_FONT, bg=self.CELADON_GREEN, justify=tk.CENTER)
        ri.grid(column=0, row=9, columnspan=8, pady=2)
        ri_min_lb = tk.Label(self.stride_view_pop_win_rightc_frame, text='Rodilla (max):', foreground=self.ONYX, font=self.REGULAR_FONT, bg=self.CELADON_GREEN, justify=tk.RIGHT)
        ri_min_lb.grid(column=0, row=10, pady=2)
        ri_min_d = tk.Label(self.stride_view_pop_win_rightc_frame, text=self.controller.data.stride_angle['TMaxRI'], foreground=self.ONYX, font=self.REGULAR_FONT, bg=self.CELADON_GREEN, justify=tk.LEFT)
        ri_min_d.grid(column=1, row=10, pady=2)
        ri_max_lb = tk.Label(self.stride_view_pop_win_rightc_frame, text='Rodilla (min):', foreground=self.ONYX, font=self.REGULAR_FONT, bg=self.CELADON_GREEN, justify=tk.RIGHT)
        ri_max_lb.grid(column=2, row=10, pady=2)
        ri_max_d = tk.Label(self.stride_view_pop_win_rightc_frame, text=self.controller.data.stride_angle['TMinRI'], foreground=self.ONYX, font=self.REGULAR_FONT, bg=self.CELADON_GREEN, justify=tk.LEFT)
        ri_max_d.grid(column=3, row=10, pady=2)
        
        ci_min_lb = tk.Label(self.stride_view_pop_win_rightc_frame, text='Cadera (max):', foreground=self.ONYX, font=self.REGULAR_FONT, bg=self.CELADON_GREEN, justify=tk.RIGHT)
        ci_min_lb.grid(column=4, row=10, pady=2)
        ci_min_d = tk.Label(self.stride_view_pop_win_rightc_frame, text=self.controller.data.stride_angle['TMaxCI'], foreground=self.ONYX, font=self.REGULAR_FONT, bg=self.CELADON_GREEN, justify=tk.LEFT)
        ci_min_d.grid(column=5, row=10, pady=2)
        ci_max_lb = tk.Label(self.stride_view_pop_win_rightc_frame, text='Cadera (min):', foreground=self.ONYX, font=self.REGULAR_FONT, bg=self.CELADON_GREEN, justify=tk.RIGHT)
        ci_max_lb.grid(column=6, row=10, pady=2)
        ci_max_d = tk.Label(self.stride_view_pop_win_rightc_frame, text=self.controller.data.stride_angle['TMinCI'], foreground=self.ONYX, font=self.REGULAR_FONT, bg=self.CELADON_GREEN, justify=tk.LEFT)
        ci_max_d.grid(column=7, row=10, pady=2)
    
    def build_metrics_data (self):
        try:
            self.stride_view_pop_win_left_canvas.destroy_plot()
        except:
            pass
        self.widget_grid_forget(self.stride_view_pop_win_rightc_frame)
        self.widget_pack_forget(self.stride_view_pop_win_rightc_frame)
        title_label = tk.Label(self.stride_view_pop_win_rightc_frame, text='Metricas Obtenidas', foreground=self.ONYX, font=self.SUB_TITLE_FONT, bg=self.CELADON_GREEN, justify=tk.CENTER, padx=5)
        title_label.grid(column=0, row=0, columnspan=8, pady=5, ipady=5)
        
        cadence_text = f'Cadencia: {self.controller.patient.cadence} pasos/minuto'
        cadence = tk.Label(self.stride_view_pop_win_rightc_frame, text=cadence_text, foreground=self.ONYX, font=self.REGULAR_FONT, bg=self.CELADON_GREEN, justify=tk.RIGHT)
        cadence.grid(column=0, row=2, pady=2)
        
        rtime_text = f'Tiempo Promedio Zancasa Derecha: {self.controller.patient.right_time} segundos'
        rtime = tk.Label(self.stride_view_pop_win_rightc_frame, text=rtime_text, foreground=self.ONYX, font=self.REGULAR_FONT, bg=self.CELADON_GREEN, justify=tk.RIGHT)
        rtime.grid(column=0, row=3, pady=2)
        
        ltime_text = f'Tiempo Promedio Zancasa Izquierda: {self.controller.patient.left_time} segundos'
        ltime = tk.Label(self.stride_view_pop_win_rightc_frame, text=ltime_text, foreground=self.ONYX, font=self.REGULAR_FONT, bg=self.CELADON_GREEN, justify=tk.RIGHT)
        ltime.grid(column=0, row=4, pady=2)
        
        velocity_text = f'Velocidad Media: {self.controller.patient.speed} metros/segundos'
        velocity = tk.Label(self.stride_view_pop_win_rightc_frame, text=velocity_text, foreground=self.ONYX, font=self.REGULAR_FONT, bg=self.CELADON_GREEN, justify=tk.RIGHT)
        velocity.grid(column=1, row=2, pady=2)
        
        rtime_text = f'Promedio Zancasa Derecha: {self.controller.patient.mean_distancer} metros'
        rtime = tk.Label(self.stride_view_pop_win_rightc_frame, text=rtime_text, foreground=self.ONYX, font=self.REGULAR_FONT, bg=self.CELADON_GREEN, justify=tk.RIGHT)
        rtime.grid(column=1, row=3, pady=2)
        
        ltime_text = f'Promedio Zancasa Izquierda: {self.controller.patient.mean_distancel} metros'
        ltime = tk.Label(self.stride_view_pop_win_rightc_frame, text=ltime_text, foreground=self.ONYX, font=self.REGULAR_FONT, bg=self.CELADON_GREEN, justify=tk.RIGHT)
        ltime.grid(column=1, row=4, pady=2)

class PlotFrame():
    def __init__(self, parent):
        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.fig, master=parent)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        self.min = -60
        self.max = 60

    def plot_data(self, x_data, y_data, label):
        self.ax.plot(x_data, y_data, label=label)
        plt.ylim(self.min, self.max)
        plt.xlabel('Tiempo (ms)')
        plt.ylabel('Angulo (grados)')
        y_min, y_max = plt.ylim()
        y_ticks = np.arange(y_min, y_max + 20, 20)
        plt.yticks(y_ticks)
    
    def destroy_plot(self):
        """Método para destruir el canvas y liberar recursos cuando no sea necesario."""
        self.canvas.get_tk_widget().destroy()
        plt.close(self.fig)