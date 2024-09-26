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
        self.stride_view_exit_buttom = tk.Button(self.stride_view_patient_information_frame, bg=self.SMOKY_TOPAZ, activebackground=self.ONYX, fg=self.ANTI_FLASH_WHITE, activeforeground=self.ANTI_FLASH_WHITE, text="Volver", font=self.BLACK_REGULAR_FONT, padx=5)
        self.stride_view_main_buttons_frame_separator = ttk.Separator(self.stride_view_main_buttons_frame, orient='horizontal', style='top.TSeparator')
        self.stride_view_top_main_buttons_frame_separator = ttk.Separator(self.stride_view_main_buttons_frame, orient='horizontal', style='top.TSeparator')
            # Lateral Menu Frame and Components:
                # Left Frame Components
        self.stride_view_components_left_frame = tk.Frame(self.stride_view_components_frame, bg=self.ONYX)
        
        self.style_config.configure('SComparative.TCombobox', foreground=self.ANTI_FLASH_WHITE, background=self.ONYX, fieldbackground=self.CELADON_GREEN)
        
        self.stride_view_time_label = tk.Label(self.stride_view_components_left_frame, text='Tiempo:', foreground=self.ANTI_FLASH_WHITE, font=self.BLACK_REGULAR_FONT, bg=self.ONYX, justify=tk.LEFT)
        
        self.time_list = [f'{i} segundos' for i in range(3, 9)]
        self.time_var = tk.StringVar
        self.stride_view_time_combobox = ttk.Combobox(self.stride_view_components_left_frame, style='SComparative.TCombobox', values=self.time_list, font=self.REGULAR_FONT, state='readonly', textvariable=self.time_var, foreground=self.ONYX, width=15)
        self.stride_view_time_combobox.current(0)
        
        self.plot_view_var = tk.IntVar()
        self.stride_view_plot_radiobuttom_label = tk.Label(self.stride_view_components_left_frame, text='Datos:', foreground=self.ANTI_FLASH_WHITE, font=self.BLACK_REGULAR_FONT, bg=self.ONYX, justify=tk.LEFT)
        self.stride_view_unique_plot_radiobuttom = tk.Radiobutton(self.stride_view_components_left_frame, font=self.REGULAR_FONT, foreground=self.ANTI_FLASH_WHITE, bg=self.ONYX, text='Original', variable=self.plot_view_var, value=0, selectcolor=self.BITTERSWEET_SHIMMER, state='disabled', command=self.change_data_radiobuttom_selected)
        self.stride_view_multiple_plot_radiobuttom = tk.Radiobutton(self.stride_view_components_left_frame, font=self.REGULAR_FONT, foreground=self.ANTI_FLASH_WHITE, bg=self.ONYX, text='Convertir', variable=self.plot_view_var, value=1, selectcolor=self.BITTERSWEET_SHIMMER, state='disabled', command=self.change_data_radiobuttom_selected)
        
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
        
        self.comparative_plot_var = tk.IntVar()
        self.stride_view_comparative_plot_checkbuttom = tk.Checkbutton(self.stride_view_components_left_frame, bg=self.ONYX, fg=self.ANTI_FLASH_WHITE, font=self.REGULAR_FONT, text="Análisis Comparativo", variable=self.comparative_plot_var, offvalue=0, onvalue=1, activebackground=self.ONYX, activeforeground=self.ANTI_FLASH_WHITE, highlightcolor=self.ONYX, selectcolor=self.BITTERSWEET_SHIMMER)
        
        self.comparative_var = tk.StringVar()
        self.stride_view_search_comparative_plot_combobox = ttk.Combobox(self.stride_view_components_left_frame, style='SComparative.TCombobox', values=['', 'Análisis Realizados'], font=self.REGULAR_FONT, state='disabled', textvariable=self.comparative_var)

                # Right Frame Components
        self.stride_view_components_right_frame = tk.Frame(self.stride_view_components_frame, bg=self.CELADON_GREEN)
        self.stride_view_left_components_right_frame_separator = ttk.Separator(self.stride_view_components_right_frame, orient='vertical', style='top.TSeparator')
                    # Right Top Frame Components
        
        self.stride_view_top_components_right_frame = tk.Frame(self.stride_view_components_right_frame, bg=self.CELADON_GREEN)
        self.stride_view_top_components_right_canvas = None
                    # Right Bottom Frame Components
        self.stride_view_bottom_components_right_frame = tk.Frame(self.stride_view_components_right_frame, bg=self.OUTER_SPACE)
        self.stride_view_bottom_components_right_frame_separator = ttk.Separator(self.stride_view_bottom_components_right_frame, orient='horizontal', style='top.TSeparator')
        self.stride_view_save_buttom = tk.Button(self.stride_view_bottom_components_right_frame, bg=self.ONYX, activebackground=self.ANTI_FLASH_WHITE, fg=self.ANTI_FLASH_WHITE, activeforeground=self.ONYX, text="Guardar", font=self.BLACK_REGULAR_FONT, padx=5, state='disabled')
        self.stride_view_to_doc_buttom = tk.Button(self.stride_view_bottom_components_right_frame, bg=self.ONYX, activebackground=self.ANTI_FLASH_WHITE, fg=self.ANTI_FLASH_WHITE, activeforeground=self.ONYX, text="Reporte", font=self.BLACK_REGULAR_FONT, padx=5, state='disabled')
        
            # Configurations:
        self.stride_view_comparative_plot_checkbuttom.configure(command=self.comparative_version_plot_control)
        self.stride_view_exit_buttom.configure(command=self.back_to_patient_view)
        self.stride_view_serial_conection_buttom.configure(command=self.create_canvas)
        self.stride_view_start_collection_buttom.configure(command=self.controller.collect_data)
        self.stride_view_save_buttom.configure(command=self.save_stride_view)
        self.stride_view_to_doc_buttom.configure(command=self.create_report_buttom)
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
        self.stride_view_main_buttons_frame_separator.pack(side=tk.BOTTOM, fill='x', expand=True)
        self.stride_view_components_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.stride_view_components_left_frame.pack(side=tk.LEFT, fill='y')
        self.stride_view_components_right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        self.stride_view_time_label.grid(column=0, row=0, columnspan=1, padx=5, pady=10, sticky='w')
        self.stride_view_time_combobox.grid(column=1, row=0, columnspan=2, padx=5, pady=10, sticky='w')
        self.stride_view_plot_radiobuttom_label.grid(column=0, row=1, columnspan=2, padx=5, pady=10, sticky='w')
        self.stride_view_unique_plot_radiobuttom.grid(column=0, row=2, columnspan=1, padx=5, pady=10, sticky='w')
        self.stride_view_multiple_plot_radiobuttom.grid(column=1, row=2, columnspan=1, padx=5, pady=10, sticky='w')
        self.stride_view_motion_planes_radiobuttom_label.grid(column=0, row=3, columnspan=2, padx=5, pady=10, sticky='w')
        self.stride_view_frontal_motion_planes_radiobuttom.grid(column=0, row=4, columnspan=1, padx=5, pady=10, sticky='w')
        self.stride_view_sagittal_motion_planes_radiobuttom.grid(column=1, row=4, columnspan=1, padx=5, pady=10, sticky='w')
        self.stride_view_joints_radiobuttom_label.grid(column=0, row=5, columnspan=2, padx=5, pady=10, sticky='w')
        self.stride_view_hip_joint_radiobuttom.grid(column=0, row=6, columnspan=1, padx=5, pady=10, sticky='w')
        self.stride_view_knee_joint_radiobuttom.grid(column=1, row=6, columnspan=1, padx=5, pady=10, sticky='w')
        self.stride_view_laterality_radiobuttom_label.grid(column=0, row=7, columnspan=2, padx=5, pady=10, sticky='w')
        self.stride_view_left_laterality_radiobuttom.grid(column=0, row=8, columnspan=1, padx=5, pady=10, sticky='w')
        self.stride_view_right_laterality_radiobuttom.grid(column=1, row=8, columnspan=1, padx=5, pady=10, sticky='w')
        self.stride_view_ignore_laterality_radiobuttom.grid(column=2, row=8, columnspan=1, padx=5, pady=10, sticky='w')
        self.stride_view_comparative_plot_checkbuttom.grid(column=0, row=9, columnspan=2, padx=5, pady=10, sticky='w')
        self.stride_view_search_comparative_plot_combobox.grid(column=0, row=10, columnspan=3, padx=5, pady=10, sticky='w')
        self.stride_view_left_components_right_frame_separator.pack(side=tk.LEFT, fill='y')
        self.stride_view_top_components_right_frame.pack(side=tk.TOP, fill='both', expand=True)
        self.stride_view_bottom_components_right_frame.pack(side=tk.BOTTOM, fill='x')
        self.stride_view_bottom_components_right_frame_separator.pack(side=tk.TOP, anchor='e', fill='x', expand=True)
        self.stride_view_save_buttom.pack(side=tk.RIGHT, anchor='e', padx=5, pady=10)
        self.stride_view_to_doc_buttom.pack(side=tk.RIGHT, anchor='e', padx=5, pady=10)
    
    def comparative_version_plot_control (self):
        if self.comparative_plot_var.get():
            self.stride_view_search_comparative_plot_combobox.configure(state='readonly')
        else:
            self.stride_view_search_comparative_plot_combobox.configure(state='disabled')
    
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
            self.stride_view_top_components_right_canvas = PlotFrame(self.stride_view_top_components_right_frame)
        else:
            try:
                self.stride_view_serial_data_taked_label.config(text='')
                self.stride_view_top_components_right_canvas.destroy_plot()
            except:
                pass

    def upload_plot_radiobuttoms (self):
        try:
            self.stride_view_top_components_right_canvas.update_plot(self.motion_planes_var.get(), self.joints_var.get(), self.laterality_var.get())
        except:
            pass
    
    def change_data_radiobuttom_selected (self):
        if self.plot_view_var.get():
            self.stride_view_top_components_right_canvas.clear_list()
            self.stride_view_top_components_right_canvas.data_collected = self.stride_view_top_components_right_canvas.data_transformed.copy()
            self.stride_view_top_components_right_canvas.min = 100
            self.stride_view_top_components_right_canvas.max = 250
            self.upload_plot_radiobuttoms()
        else:
            if self.stride_view_top_components_right_canvas.data_transformed:
                self.stride_view_top_components_right_canvas.clear_list()
            self.stride_view_top_components_right_canvas.data_collected = self.stride_view_top_components_right_canvas.data_collected_saved.copy()
            self.stride_view_top_components_right_canvas.min = -60
            self.stride_view_top_components_right_canvas.max = 60
            self.upload_plot_radiobuttoms()
    
    def save_stride_view (self):
        if self.ask_yes_no('Salvar datos de Zancasa', '¿Está seguro de guardar los datos?'):
            self.controller.save_raw_stride()

    def time_selected (self, event):
        num = self.stride_view_time_combobox.get().split(" ")
        time = int(num[0])*100
        self.controller.data_size = time
    
    def create_report_buttom(self):
        if self.ask_yes_no('Generar reporte', '¿Quiere generar un reporte?'):
            self.controller.make_report_pdf()

class PlotFrame():
    def __init__(self, parent):
        self.data_collected = {
                'RDIndex':[], 'RDTime(ms)':[], 'RDSagital':[], 'RDFrontal':[],
                'CDIndex':[], 'CDTime(ms)':[], 'CDSagital':[], 'CDFrontal':[],
                'RIIndex':[], 'RITime(ms)':[], 'RISagital':[], 'RIFrontal':[],
                'CIIndex':[], 'CITime(ms)':[], 'CISagital':[], 'CIFrontal':[]
                                }
        self.data_transformed = {}
        self.data_collected_saved = {}
        self.graph_type_var = None
        self.graph_joint_var = None
        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.fig, master=parent)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        self.min = -60
        self.max = 60

    def clear_list (self):
        self.data_collected = {
                'RDIndex':[], 'RDTime(ms)':[], 'RDSagital':[], 'RDFrontal':[],
                'CDIndex':[], 'CDTime(ms)':[], 'CDSagital':[], 'CDFrontal':[],
                'RIIndex':[], 'RITime(ms)':[], 'RISagital':[], 'RIFrontal':[],
                'CIIndex':[], 'CITime(ms)':[], 'CISagital':[], 'CIFrontal':[]
                                }

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

    def update_plot(self, graph_type, joint, laterality):
        try:
            self.ax.clear()
            if graph_type == 0:
                if joint == 0:
                    if laterality in [0, 1]:
                        self.plot_data(self.data_collected['CDTime(ms)'], self.data_collected['CDFrontal'], "Cadera Derecha Frontal")
                    if laterality in [0, 2]:
                        self.plot_data(self.data_collected['CITime(ms)'], self.data_collected['CIFrontal'], "Cadera Izquierda Frontal")
                if joint == 1:
                    if laterality in [0, 1]:
                        self.plot_data(self.data_collected['RDTime(ms)'], self.data_collected['RDFrontal'], "Rodilla Derecha Frontal")
                    if laterality in [0, 2]:
                        self.plot_data(self.data_collected['RITime(ms)'], self.data_collected['RIFrontal'], "Rodilla Izquierda Frontal")
            if graph_type == 1:
                if joint == 0:
                    if laterality in [0, 1]:
                        self.plot_data(self.data_collected['CDTime(ms)'], self.data_collected['CDSagital'], "Cadera Derecha Sagital")
                    if laterality in [0, 2]:
                        self.plot_data(self.data_collected['CITime(ms)'], self.data_collected['CISagital'], "Cadera Izquierda Sagital")
                if joint == 1:
                    if laterality in [0, 1]:
                        self.plot_data(self.data_collected['RDTime(ms)'], self.data_collected['RDSagital'], "Rodilla Derecha Sagital")
                    if laterality in [0, 2]:
                        self.plot_data(self.data_collected['RITime(ms)'], self.data_collected['RISagital'], "Rodilla Izquierda Sagital")
            self.ax.grid(True)
            self.ax.legend()
            self.canvas.draw()
        except:
            pass