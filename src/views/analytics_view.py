import tkinter as tk
from tkinter import ttk
from .general_view import General_View
from controllers.canvas_draw import PlotFrame
import matplotlib.pyplot as plt
import numpy as np


class Analytic_View (General_View):
    
    def __init__ (self, root, controller):
        super().__init__(root, controller)
        def on_closing():
            if self.show_ok_cancel("Quit", "Do you want to quit?"):
                if self.controller.thread is not None and self.controller.thread.is_alive():
                    self.controller.thread.join(timeout=1)
                if self.controller.thread2 is not None and self.controller.thread2.is_alive():
                    self.controller.thread2.join(timeout=1)
                self.controller.thread = None
                self.controller.thread2 = None
                self.controller.ani = None
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
        
        self.stride_view_battery_frame = tk.Frame(self.stride_view_components_left_frame, bg=self.ONYX)
        self.stride_view_battery_separator = ttk.Separator(self.stride_view_battery_frame, orient='horizontal', style='top.TSeparator')
        
        self.stride_view_battery_tittle = tk.Label(self.stride_view_components_left_frame, text='% Carga de Baterías:', foreground=self.ANTI_FLASH_WHITE, font=self.BLACK_REGULAR_FONT, bg=self.ONYX, justify=tk.LEFT)
        
        self.max_widht = 24
        self.rd_int_var = tk.IntVar()
        self.rd_int_var.set(10)
        self.stride_view_rd_frame = tk.Frame(self.stride_view_components_left_frame, bg=self.OUTER_SPACE, width=300, height=20)
        self.stride_view_rd_frame.pack_propagate(False)
        self.stride_view_rd_label = tk.Label(self.stride_view_rd_frame, text='RD: ', foreground=self.ANTI_FLASH_WHITE, font=self.SMALL_REGULAR_FONT, bg=self.ONYX, justify=tk.LEFT, width=5)
        self.stride_view_rd_bar_label = tk.Label(self.stride_view_rd_frame, bg=self.BATTERY_COLOR_LOW, width=int(self.max_widht*0.1))
        self.stride_view_rd_var_label = tk.Label(self.stride_view_rd_frame, bg=self.ONYX, text=f'{self.rd_int_var.get()} %', foreground=self.ANTI_FLASH_WHITE, font=self.SMALL_REGULAR_FONT, width=5)

        self.ri_int_var = tk.IntVar()
        self.ri_int_var.set(30)
        self.stride_view_ri_frame = tk.Frame(self.stride_view_components_left_frame, bg=self.OUTER_SPACE, width=300, height=20)
        self.stride_view_ri_frame.pack_propagate(False)
        self.stride_view_ri_label = tk.Label(self.stride_view_ri_frame, text='RI: ', foreground=self.ANTI_FLASH_WHITE, font=self.SMALL_REGULAR_FONT, bg=self.ONYX, justify=tk.LEFT, width=5)
        self.stride_view_ri_bar_label = tk.Label(self.stride_view_ri_frame, bg=self.BATTERY_COLOR_MID, width=int(self.max_widht*0.3))
        self.stride_view_ri_var_label = tk.Label(self.stride_view_ri_frame, bg=self.ONYX, text=f'{self.ri_int_var.get()} %', foreground=self.ANTI_FLASH_WHITE, font=self.SMALL_REGULAR_FONT, width=5)

        self.cd_int_var = tk.IntVar()
        self.cd_int_var.set(60)
        self.stride_view_cd_frame = tk.Frame(self.stride_view_components_left_frame, bg=self.OUTER_SPACE, width=300, height=20)
        self.stride_view_cd_frame.pack_propagate(False)
        self.stride_view_cd_label = tk.Label(self.stride_view_cd_frame, text='CD: ', foreground=self.ANTI_FLASH_WHITE, font=self.SMALL_REGULAR_FONT, bg=self.ONYX, justify=tk.LEFT, width=5)
        self.stride_view_cd_bar_label = tk.Label(self.stride_view_cd_frame, bg=self.BATTERY_COLOR_TOP, width=int(self.max_widht*0.6))
        self.stride_view_cd_var_label = tk.Label(self.stride_view_cd_frame, bg=self.ONYX, text=f'{self.cd_int_var.get()} %', foreground=self.ANTI_FLASH_WHITE, font=self.SMALL_REGULAR_FONT, width=5)

        self.ci_int_var = tk.IntVar()
        self.ci_int_var.set(100)
        self.stride_view_ci_frame = tk.Frame(self.stride_view_components_left_frame, bg=self.OUTER_SPACE, width=300, height=20)
        self.stride_view_ci_frame.pack_propagate(False)
        self.stride_view_ci_label = tk.Label(self.stride_view_ci_frame, text='CI: ', foreground=self.ANTI_FLASH_WHITE, font=self.SMALL_REGULAR_FONT, bg=self.ONYX, justify=tk.LEFT, width=5)
        self.stride_view_ci_bar_label = tk.Label(self.stride_view_ci_frame, bg=self.BATTERY_COLOR_TOP, width=self.max_widht)
        self.stride_view_ci_var_label = tk.Label(self.stride_view_ci_frame, bg=self.ONYX, text=f'{self.ci_int_var.get()} %', foreground=self.ANTI_FLASH_WHITE, font=self.SMALL_REGULAR_FONT, width=5)

                # Right Frame Components
        self.stride_view_components_right_frame = tk.Frame(self.stride_view_components_frame, bg=self.CELADON_GREEN)
        self.stride_view_left_components_right_frame_separator = ttk.Separator(self.stride_view_components_right_frame, orient='vertical', style='top.TSeparator')
                    # Right Top Frame Components
        
        self.stride_view_top_components_right_frame = tk.Frame(self.stride_view_components_right_frame, bg=self.CELADON_GREEN)
        self.stride_view_top_components_right_canvas:PlotFrame|None = None
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
        
        self.stride_view_battery_frame.grid(column=0, row=5, columnspan=3, pady=20, sticky='we')
        self.stride_view_battery_separator.pack(side=tk.BOTTOM, fill='x', expand=True)

        self.stride_view_battery_tittle.grid(column=0, row=6, columnspan=2, padx=5, pady=10, sticky='w')
        
        self.stride_view_rd_frame.grid(column=0, row=7, columnspan=2, padx=5, pady=10, sticky='w')
        self.stride_view_rd_label.pack(side=tk.LEFT, anchor='w')
        self.stride_view_rd_bar_label.pack(side=tk.LEFT, anchor='w')
        self.stride_view_rd_var_label.pack(side=tk.RIGHT, anchor='e', ipadx=10)

        self.stride_view_ri_frame.grid(column=0, row=8, columnspan=2, padx=5, pady=10, sticky='w')
        self.stride_view_ri_label.pack(side=tk.LEFT, anchor='w')
        self.stride_view_ri_bar_label.pack(side=tk.LEFT, anchor='w')
        self.stride_view_ri_var_label.pack(side=tk.RIGHT, anchor='e', ipadx=10)

        self.stride_view_cd_frame.grid(column=0, row=9, columnspan=2, padx=5, pady=10, sticky='w')
        self.stride_view_cd_label.pack(side=tk.LEFT, anchor='w')
        self.stride_view_cd_bar_label.pack(side=tk.LEFT, anchor='w')
        self.stride_view_cd_var_label.pack(side=tk.RIGHT, anchor='e', ipadx=10)
        
        self.stride_view_ci_frame.grid(column=0, row=10, columnspan=2, padx=5, pady=10, sticky='w')
        self.stride_view_ci_label.pack(side=tk.LEFT, anchor='w')
        self.stride_view_ci_bar_label.pack(side=tk.LEFT, anchor='w')
        self.stride_view_ci_var_label.pack(side=tk.RIGHT, anchor='e', ipadx=10)
        
        self.stride_view_left_components_right_frame_separator.pack(side=tk.LEFT, fill='y')
        self.stride_view_top_components_right_frame.pack(side=tk.TOP, fill='both', expand=True)
        self.stride_view_bottom_components_right_frame.pack(side=tk.BOTTOM, fill='x')
        self.stride_view_bottom_components_right_frame_separator.pack(side=tk.TOP, anchor='e', fill='x', expand=True)
        self.stride_view_bottom_labels_components_right_frame.pack(side=tk.BOTTOM, anchor='e', fill=tk.BOTH, padx=10)
        self.stride_view_raw_data_max_min_valor_buttom.pack(side=tk.RIGHT, anchor='e', padx=5, pady=10, ipadx=5, ipady=5)
    
    def back_to_patient_view (self):
        try:
            self.stride_view_top_components_right_canvas.destroy_plot()
            self.stride_view_serial_data_taked_label.config(text='')
        except:
            pass
        self.controller.back_to_patient_view()
    
    def create_canvas (self):
        self.controller.get_conection()
        if self.controller.connection_status:
            self.show_error('Error', 'No se pudo conectar, verifique el puerto')
    
    def new_canvas (self):
        self.stride_view_top_components_right_canvas = PlotFrame(self.stride_view_top_components_right_frame)

    def upload_plot_radiobuttoms (self):
        try:
            self.controller.update_plot(self.motion_planes_var.get(), self.joints_var.get(), 0)
        except:
            pass
    
    def save_stride_view (self):
        if self.ask_yes_no('Advertencia', '¿Está seguro de guardar los datos y generar reporte?'):
            self.controller.save_raw_stride()
            self.controller.make_report_pdf()
    
    def _show_general_analytics (self):
        try:
            self.controller.make_load_data_metrics()
            self.stride_view_raw_data_max_min_valor_buttom.configure(state=tk.DISABLED)
            self.stride_view_pop_win = tk.Toplevel()
            def on_closing():
                self.stride_view_raw_data_max_min_valor_buttom.configure(state=tk.NORMAL)
                self.stride_view_save_buttom.configure(state=tk.NORMAL)
                self.stride_view_pop_win.destroy()
            self.stride_view_pop_win.protocol("WM_DELETE_WINDOW", on_closing)
            self.stride_view_pop_win.geometry("1000x600+100+200")
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
            raw_data_avnz_buttom = tk.Button(self.stride_view_pop_win_left_frame, bg=self.ONYX, activebackground=self.ANTI_FLASH_WHITE, fg=self.ANTI_FLASH_WHITE, activeforeground=self.ONYX, text="Graficas", font=self.BLACK_REGULAR_FONT, padx=5, width=15, command=self.generate_grafic)
            raw_data_avnz_buttom.pack(side=tk.TOP, pady=10, padx=10)
            self.stride_view_pop_win_right_frame = tk.Frame(self.stride_view_pop_win, bg=self.CELADON_GREEN) #, width=self.stride_view_pop_win.winfo_screenwidth-60, height=self.stride_view_pop_win.winfo_screenheight()-60
            self.stride_view_pop_win_right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
            self.stride_view_pop_win_rightc_frame = tk.Frame(self.stride_view_pop_win_right_frame, bg=self.CELADON_GREEN) #, width=self.stride_view_pop_win.winfo_screenwidth-60, height=self.stride_view_pop_win.winfo_screenheight()-60
            self.stride_view_pop_win_rightc_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
            left_separator = ttk.Separator(self.stride_view_pop_win_right_frame, orient='vertical', style='top.TSeparator')
            left_separator.pack(side=tk.LEFT, anchor='w', fill='y')
        except:
            self.show_error('Error', 'Parametros no adecuados para una valoración')
        
    def close(self):
        self.stride_view_raw_data_max_min_valor_buttom.configure(state=tk.NORMAL)
        self.stride_view_save_buttom.configure(state=tk.NORMAL)
        self.stride_view_pop_win.destroy()

    def generate_raw_data (self):
        try:
            self.stride_view_pop_win_left_canvas.destroy_plot()
        except:
            pass
        self.widget_grid_forget(self.stride_view_pop_win_rightc_frame)
        self.widget_pack_forget(self.stride_view_pop_win_rightc_frame)
        title_label = tk.Label(self.stride_view_pop_win_rightc_frame, text='Valores mínimos y máximos', foreground=self.ONYX, font=self.SUB_TITLE_FONT, bg=self.CELADON_GREEN, justify=tk.CENTER, padx=5)
        title_label.grid(column=0, row=0, columnspan=17, pady=5, ipady=5)
        separator1_frame = tk.Frame(self.stride_view_pop_win_rightc_frame, bg=self.CELADON_GREEN)
        separator1_frame.grid(column=0, row=1, columnspan=17, pady=5, ipady=5)
        separator1 = ttk.Separator(separator1_frame, orient='horizontal', style='top.TSeparator')
        separator1.pack(side=tk.LEFT, anchor='w', fill='y')
        
        def create_label(frame, text, font, bg, row, col, colspan=1, pady=2, justify=tk.LEFT):
            """Auxiliary function to create and place labels"""
            label = tk.Label(frame, text=text, foreground=self.ONYX, font=font, bg=bg, justify=justify)
            label.grid(row=row, column=col, columnspan=colspan, pady=pady)
            return label

        # Encabezados principales
        create_label(self.stride_view_pop_win_rightc_frame, 'Pierna Derecha Sagital', self.BLACK_REGULAR_FONT, self.CELADON_GREEN, row=2, col=1, colspan=8, justify=tk.CENTER)
        # Sub-encabezados
        create_label(self.stride_view_pop_win_rightc_frame, 'Rodilla', self.BLACK_REGULAR_FONT, self.CELADON_GREEN, row=3, col=1, colspan=4, justify=tk.CENTER)
        create_label(self.stride_view_pop_win_rightc_frame, 'Cadera', self.BLACK_REGULAR_FONT, self.CELADON_GREEN, row=3, col=5, colspan=4, justify=tk.CENTER)

        # Etiquetas de filas para datos mínimos y máximos
        create_label(self.stride_view_pop_win_rightc_frame, 'Mínimos:', self.BLACK_REGULAR_FONT, self.CELADON_GREEN, row=4, col=0, justify=tk.RIGHT)
        create_label(self.stride_view_pop_win_rightc_frame, 'Máximos:', self.BLACK_REGULAR_FONT, self.CELADON_GREEN, row=5, col=0, justify=tk.RIGHT)
        
        separator2_frame = tk.Frame(self.stride_view_pop_win_rightc_frame, bg=self.CELADON_GREEN)
        separator2_frame.grid(column=0, row=6, columnspan=17, pady=5, ipady=5)
        separator2 = ttk.Separator(separator1_frame, orient='horizontal', style='top.TSeparator')
        separator2.pack(side=tk.LEFT, anchor='w', fill='y')
        
        create_label(self.stride_view_pop_win_rightc_frame, 'Pierna Izquierda Sagital', self.BLACK_REGULAR_FONT, self.CELADON_GREEN, row=7, col=1, colspan=8, justify=tk.CENTER)
        
        create_label(self.stride_view_pop_win_rightc_frame, 'Rodilla', self.BLACK_REGULAR_FONT, self.CELADON_GREEN, row=8, col=1, colspan=4, justify=tk.CENTER)
        create_label(self.stride_view_pop_win_rightc_frame, 'Cadera', self.BLACK_REGULAR_FONT, self.CELADON_GREEN, row=8, col=5, colspan=4, justify=tk.CENTER)
        
        create_label(self.stride_view_pop_win_rightc_frame, 'Mínimos:', self.BLACK_REGULAR_FONT, self.CELADON_GREEN, row=9, col=0, justify=tk.RIGHT)
        create_label(self.stride_view_pop_win_rightc_frame, 'Máximos:', self.BLACK_REGULAR_FONT, self.CELADON_GREEN, row=10, col=0, justify=tk.RIGHT)

        # Datos mínimos y máximos organizados
        data_keys = {
            'Mínimos': {
                'RD': ['MinRD', 'MinCD'],
                'RI': ['MinRI', 'MinCI'],
                'CD': ['MinRD', 'MinCD'],
                'CI': ['MinRI', 'MinCI']
            },
            'Máximos': {
                'RD': ['MaxRD', 'MaxCD'],
                'RI': ['MaxRI', 'MaxCI'],
                'CD': ['MinRD', 'MinCD'],
                'CI': ['MinRI', 'MinCI']
            }
        }

        # Posiciones columna de datos
        col_mapping = {
            'MinRD': 1, 'MaxRD': 1,
            'MinCD': 5, 'MaxCD': 5,
            'MinRI': 1, 'MaxRI': 1,
            'MinCI': 5, 'MaxCI': 5
        }
        row_mapping = {
            'MinRD': 4, 'MaxRD': 5,
            'MinCD': 4, 'MaxCD': 5,
            'MinRI': 9, 'MaxRI': 10,
            'MinCI': 9, 'MaxCI': 10
        }

        # Insertar datos mínimos
        for _, data in data_keys['Mínimos'].items():
            for sensor, _ in zip(data, [1, 5, 9, 13]):
                value = self.controller.data.stride_angle[sensor]
                create_label(self.stride_view_pop_win_rightc_frame, str(value), self.REGULAR_FONT, self.CELADON_GREEN, row=row_mapping[sensor], col=col_mapping[sensor], colspan=4, justify=tk.CENTER)

        # Insertar datos máximos
        for _, data in data_keys['Máximos'].items():
            for sensor, _ in zip(data, [1, 5, 9, 13]):
                value = self.controller.data.stride_angle[sensor]
                create_label(self.stride_view_pop_win_rightc_frame, str(value), self.REGULAR_FONT, self.CELADON_GREEN, row=row_mapping[sensor], col=col_mapping[sensor], colspan=4, justify=tk.CENTER)
    
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
        cadence = tk.Label(self.stride_view_pop_win_rightc_frame, text=cadence_text, foreground=self.ONYX, font=self.REGULAR_FONT, bg=self.CELADON_GREEN, justify=tk.LEFT)
        cadence.grid(column=0, row=2, pady=2, sticky='w', padx=10)
        
        velocity_text = f'Velocidad Media: {self.controller.patient.speed} metros/segundos'
        velocity = tk.Label(self.stride_view_pop_win_rightc_frame, text=velocity_text, foreground=self.ONYX, font=self.REGULAR_FONT, bg=self.CELADON_GREEN, justify=tk.LEFT)
        velocity.grid(column=0, row=3, pady=2, sticky='w', padx=10)
        
        rtime_text = f'Tiempo Promedio Zancasa Derecha: {self.controller.patient.right_time} segundos'
        rtime = tk.Label(self.stride_view_pop_win_rightc_frame, text=rtime_text, foreground=self.ONYX, font=self.REGULAR_FONT, bg=self.CELADON_GREEN, justify=tk.LEFT)
        rtime.grid(column=0, row=4, pady=2, sticky='w', padx=10)
        
        ltime_text = f'Tiempo Promedio Zancasa Izquierda: {self.controller.patient.left_time} segundos'
        ltime = tk.Label(self.stride_view_pop_win_rightc_frame, text=ltime_text, foreground=self.ONYX, font=self.REGULAR_FONT, bg=self.CELADON_GREEN, justify=tk.LEFT)
        ltime.grid(column=0, row=5, pady=2, sticky='w', padx=10)
        
        rtime_text = f'Promedio Zancasa Derecha: {self.controller.patient.mean_distancer} metros'
        rtime = tk.Label(self.stride_view_pop_win_rightc_frame, text=rtime_text, foreground=self.ONYX, font=self.REGULAR_FONT, bg=self.CELADON_GREEN, justify=tk.LEFT)
        rtime.grid(column=0, row=6, pady=2, sticky='w', padx=10)
        
        ltime_text = f'Promedio Zancasa Izquierda: {self.controller.patient.mean_distancel} metros'
        ltime = tk.Label(self.stride_view_pop_win_rightc_frame, text=ltime_text, foreground=self.ONYX, font=self.REGULAR_FONT, bg=self.CELADON_GREEN, justify=tk.LEFT)
        ltime.grid(column=0, row=7, pady=2, sticky='w', padx=10)
    
    def generate_grafic (self):
        try:
            self.stride_view_pop_win_left_canvas.destroy_plot()
        except:
            pass
        self.widget_grid_forget(self.stride_view_pop_win_rightc_frame)
        self.widget_pack_forget(self.stride_view_pop_win_rightc_frame)
        self.stride_view_pop_win_left_canvas = PlotFrame(self.stride_view_pop_win_rightc_frame)
        self.controller.plot_peaks()