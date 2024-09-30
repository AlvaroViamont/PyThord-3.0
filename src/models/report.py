from fpdf import FPDF
import matplotlib.pyplot as plt
import io
import tempfile
import numpy as np
from PIL import Image
from datetime import datetime
from controllers.patient_controller import PatientController
from controllers.data_controller import DataController
from paths import IMG_LOGO_PATH, get_patient_doc_file, IMG_R_BBASE, IMG_R_ABASE, IMG_R_ARAW, IMG_R_ATRN, IMG_R_BRAW, IMG_R_BTRN


colors = {
    "EART_YELLOW": "#FAB860",
    "ONYX": "#32373B",
    "OUTER_SPACE": "#4A5859",
    "ANTI_FLASH_WHITE": "#F0F0F0",
    "BITTERSWEET_SHIMMER": "#C83E4D",
    "CELADON_GREEN": "#2E8B57",   
    "DEEP_CARMINE_PINK": "#EF3038",
    "SMOKY_TOPAZ": "#935A5C",
    "WHITE": "#FFFFFF",
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

custom_style_2 = {
    "axes.facecolor": colors["ANTI_FLASH_WHITE"],  
    "axes.edgecolor": colors["ONYX"],
    "axes.labelcolor": colors["ONYX"],  
    "xtick.color": colors["ONYX"],
    "ytick.color": colors["ONYX"],
    "text.color": colors["ONYX"],  
    "figure.facecolor": colors["WHITE"],
    "figure.edgecolor": colors["ONYX"],
    "grid.color": colors["OUTER_SPACE"],
    "lines.linewidth": 2.0,
    "lines.color": colors["ONYX"],  
    "patch.edgecolor": colors["SMOKY_TOPAZ"],
    "patch.facecolor": colors["BITTERSWEET_SHIMMER"],
    "axes.prop_cycle": plt.cycler('color', [
        colors["OUTER_SPACE"],           
        colors["DEEP_CARMINE_PINK"],     
        colors["SMOKY_TOPAZ"], 
        colors["BITTERSWEET_SHIMMER"], 
        colors["EART_YELLOW"]
    ])
}

class PDF(FPDF):
    def __init__(self):
        super().__init__()
        self.patient:PatientController|None = None
        self.data:DataController|None = None
        self.doctor_contact:str|None = None
        self.report_date:str|None = None
        self.cadencia:int = 0
        self.promed_time:int = 1
        self.logo_path = IMG_LOGO_PATH
        
        self.set_auto_page_break(auto=True, margin=17)
    
    def header(self):
        self.set_fill_color(74, 88, 89)
        self.rect(0, 0, 210, 20, 'F')
        self.image(self.logo_path, 10, 2, 15)
        self.set_text_color(250, 184, 96)
        self.set_font('Arial', 'B', 24)
        self.set_x(25)
        self.cell(0, 0, 'PyThord', 0, 1)
        self.set_text_color(240, 240, 240)
        self.set_font('Arial', 'B', 14)
        self.cell(0, 0, f'Fecha: {self.report_date}', 0, 1, 'R')
        self.ln(15)

    def footer(self):
        self.set_y(-15)
        self.set_fill_color(50, 55, 59)
        self.rect(0, self.get_y(), 210, 15, 'F')
        self.set_font('Arial', 'I', 8)
        self.set_text_color(240, 240, 240)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'L')
        if self.doctor_contact:
            self.cell(0, 10, f'Contact: {self.doctor_contact}', 0, 0, 'R')
    
    def _first_page(self):
        # Configura el tamaño de página Carta
        self.add_page()
        
        # Título principal
        self.set_font('Arial', 'B', 24)
        self.set_fill_color(255, 255, 255)  # Fondo blanco
        self.set_text_color(50, 55, 59)  # Color oscuro para el texto # Espacio al principio
        self.cell(190, 15, 'Análisis de Zancada', 0, 1, 'C', fill=True)
        self.ln(1)  # Espacio después del título
        # Información del paciente
        self.set_font('Arial', 'B', 12)
        self.set_text_color(50, 55, 59)  # Color oscuro para el texto
        self.cell(0, 5, f'Nombre del Paciente: {self.patient.name}', 0, 1, 'L')
        self.cell(0, 5, f'Edad del Paciente: {self.patient.age}', 0, 1, 'L')
        self.cell(0, 5, f'CI: {self.patient.ci}', 0, 1, 'L')
        self.ln(5)  # Espacio después de la información del paciente

        # Añadir primera fila de imágenes y datos de cadencia
        y1 = self.get_y()
        self.set_xy(45, y1)
        self.cell(60, 10, f'Cadencia: {self.cadencia}', 0, 1, 'L')
        self.cell(60, 10, f'Tiempo Promedio: {self.promed_time}', 0, 0, 'L')
        self.set_xy(140, y1)
        self.ln(45)  # Añade espacio después de las imágenes y datos

        # Añadir segunda fila de imágenes y datos del sensor
        y1 = self.get_y()
        self.image(IMG_R_ARAW, 10, y1, 50, 76.2)  # Ajusta el ancho de la imagen
        self.set_xy(65, y1)
        self.cell(0, 10, f'A Sensor CIS(min): {self.data.stride_angle['MinCI']}', 0, 1, 'L')
        self.set_x(65)
        self.cell(0, 10, f'A Sensor CIS(max): {self.data.stride_angle['MaxCI']}', 0, 1, 'L')
        self.set_x(65)
        self.cell(0, 10, f'A Sensor RIS(min): {self.data.stride_angle['MinRI']}', 0, 1, 'L')
        self.set_x(65)
        self.cell(0, 10, f'A Sensor RIS(max): {self.data.stride_angle['MaxRI']}', 0, 1, 'L')
        self.set_xy(90, y1)
        self.cell(0, 10, f'A Sensor CDS(min): {self.data.stride_angle['MinCD']}', 0, 1, 'L')
        self.set_x(90)
        self.cell(0, 10, f'A Sensor CDS(max): {self.data.stride_angle['MaxCD']}', 0, 1, 'L')
        self.set_x(90)
        self.cell(0, 10, f'A Sensor RDS(min): {self.data.stride_angle['MinRD']}', 0, 1, 'L')
        self.set_x(90)
        self.cell(0, 10, f'A Sensor RDS(max): {self.data.stride_angle['MaxRD']}', 0, 1, 'L')
        self.image(IMG_R_BRAW, 150, y1, 50, 76.2)  # Imagen ajustada en la misma fila
        self.ln(45)  # Espacio después de esta fila

        # Añadir tercera fila de imágenes y datos de la articulación
        y1 = self.get_y()
        self.image(IMG_R_ATRN, 10, y1, 50, 76.2)  # Imagen ajustada
        self.set_xy(65, y1)
        self.cell(0, 10, f'A Art. CIS(min): {self.data.stride_angle['TMinCI']}', 0, 1, 'L')
        self.set_x(65)
        self.cell(0, 10, f'A Art. CIS(max): {self.data.stride_angle['TMaxCI']}', 0, 1, 'L')
        self.set_x(65)
        self.cell(0, 10, f'A Art. RIS(min): {self.data.stride_angle['TMinRI']}', 0, 1, 'L')
        self.set_x(65)
        self.cell(0, 10, f'A Art. RIS(max): {self.data.stride_angle['TMaxRI']}', 0, 1, 'L')
        self.set_xy(90, y1)
        self.cell(0, 10, f'A Art. CDS(min): {self.data.stride_angle['TMinCD']}', 0, 1, 'L')
        self.set_x(90)
        self.cell(0, 10, f'A Art. CDS(max): {self.data.stride_angle['TMaxCD']}', 0, 1, 'L')
        self.set_x(90)
        self.cell(0, 10, f'A Art. RDS(min): {self.data.stride_angle['TMinRD']}', 0, 1, 'L')
        self.set_x(90)
        self.cell(0, 10, f'A Art. RDS(max): {self.data.stride_angle['TMaxRD']}', 0, 1, 'L')
        self.image(IMG_R_BTRN, 150, y1, 50, 76.2)  # Imagen ajustada
        self.ln(45)  # Espacio después de esta fila
        # Fin de la página
        self.ln(5)
    
    def _create_plot_analytic_section(self, x_column, y_column, title, xlabel, ylabel):
        plt.figure(figsize=(8, 4))
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        x_min = 0
        x_max = self.data.data_size
        x_ticks = np.arange(x_min, x_max +20, 50)
        plt.xticks(x_ticks)
        plt.grid(True)
        plt.plot(x_column, y_column)

        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        plt.close()
        buf.seek(0)

        image = Image.open(buf)
        img_buffer = io.BytesIO()
        image.save(img_buffer, format='PNG')
        img_buffer.seek(0)

        self.set_font('Arial', 'B', 16)
        self.set_text_color(50, 55, 59)
        self.ln(10)
        self.cell(0, 0, f'{title}', 0, 1, 'C', True)
        self.set_font('Arial', '', 12)
        self.ln(10)
        self.image(img_buffer, x=10, w=180, h=90)
        self.ln()
    
    def _create_comparative_plot_analytic_section(self, x_column, y1_column, y2_column, title, xlabel, ylabel, p1label, p2label):
        plt.figure(figsize=(8, 4))
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        x_min = 0
        x_max = self.data.data_size*10
        x_ticks = np.arange(x_min, x_max + 50, self.data.data_size//100)
        plt.xticks(x_ticks)
        plt.grid(True)
        plt.plot(x_column, y1_column, label=p1label)
        plt.plot(x_column, y2_column, label=p2label)
        plt.legend()

        # Crear un archivo temporal
        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as temp_file:
            # Guardar la imagen temporalmente
            plt.savefig(temp_file.name, format='png')
            plt.close()

            # Especificar el nombre del archivo temporal a FPDF
            self.set_font('Arial', 'B', 16)
            self.set_text_color(50, 55, 59)
            self.ln(10)
            self.cell(0, 0, f'{title}', 0, 1, 'C', True)
            self.set_font('Arial', '', 12)
            self.ln(10)

            # Usar el archivo temporal para agregar la imagen
            self.image(temp_file.name, x=10, w=180, h=90)
            self.ln()
    
    def _create_table_section(self, data_dict:dict, motion_planes:str):
        self.add_page()
        self.set_font('Arial', 'B', 12)
        self.set_fill_color(72, 88, 89)
        self.set_text_color(250, 184, 96)
        headers = list(data_dict.keys())
        column_width = 170 / 8
        column_header_width_a = 180 / 2 + 5
        column_header_width_b = 180 / 2 - 5
        self.cell(180, 5, motion_planes, 1, 0, 'C', fill=True)
        self.ln()
        self.set_font('Arial', 'B', 10)
        self.cell(column_header_width_a, 5, 'Sensor', 1, 0, 'C', fill=True)
        self.cell(column_header_width_b, 5, 'Transformada', 1, 0, 'C', fill=True)
        self.ln()
        self.set_font('Arial', '', 10)
        for header in headers:
            if header == 'Time(ms)':
                self.cell(10, 5, 'ms', 1, 0, 'C', fill=True)
            elif motion_planes in header:
                self.cell(column_width, 5, header, 1, 0, 'C', fill=True)
        self.ln()

        self.set_font('Arial', '', 6)
        self.set_text_color(50, 55, 59)
        num_rows = len(next(iter(data_dict.values())))
        for i in range(num_rows):
            for key in headers:
                if key == 'Time(ms)':
                    self.cell(10, 2.8, str(data_dict[key][i]), 1, align='C')
                elif motion_planes in key:
                    self.cell(column_width, 2.8, str(data_dict[key][i]), 1, align='C')
            self.ln()
    
    def _get_current_date_and_timestamp(self):
        now = datetime.now()
        timestamp_string = ''.join((now.strftime("%d%m%Y%H%M%S"), '.pdf'))
        return timestamp_string

    def build(self):
        plt.rcParams.update(custom_style_2)
        self._first_page()
        self.add_page()
        self._create_comparative_plot_analytic_section(self.data.stride_raw_data['Time(ms)'], self.data.stride_raw_data['CDSagital'], self.data.stride_raw_data['CISagital'], 'Caderas en el plano Sagital data Original', 'Tiempo (ms)', 'CD vs CI', 'CD', 'CI')
        self._create_comparative_plot_analytic_section(self.data.stride_raw_data['Time(ms)'], self.data.stride_raw_data['CDFrontal'], self.data.stride_raw_data['CIFrontal'], 'Caderas en el plano Frontal data Original', 'Tiempo (ms)', 'CD vs CI', 'CD', 'CI' )
        self.add_page()
        self._create_comparative_plot_analytic_section(self.data.stride_raw_data['Time(ms)'], self.data.stride_raw_data['RDSagital'], self.data.stride_raw_data['RISagital'], 'Rodilla en el plano Sagital data Original', 'Tiempo (ms)', 'RD vs RI', 'RD', 'RI' )
        self._create_comparative_plot_analytic_section(self.data.stride_raw_data['Time(ms)'], self.data.stride_raw_data['RDFrontal'], self.data.stride_raw_data['RIFrontal'], 'Rodilla en el plano Frontal data Original', 'Tiempo (ms)', 'RD vs RI', 'RD', 'RI' )
        '''self.add_page()
        self._create_comparative_plot_analytic_section(self.data_dict['Time(ms)'], self.data_dict['TCDSagital'], self.data_dict['TCISagital'], 'Caderas en el plano Sagital data Transformada', 'Tiempo (ms)', 'CD vs CI')
        self._create_comparative_plot_analytic_section(self.data_dict['Time(ms)'], self.data_dict['TCDFrontal'], self.data_dict['TCIFrontal'], 'Caderas en el plano Frontal data Transformada', 'Tiempo (ms)', 'CD vs CI')
        self.add_page()
        self._create_comparative_plot_analytic_section(self.data_dict['Time(ms)'], self.data_dict['TRDSagital'], self.data_dict['TRISagital'], 'Rodilla en el plano Sagital data Transformada', 'Tiempo (ms)', 'RD vs RI')
        self._create_comparative_plot_analytic_section(self.data_dict['Time(ms)'], self.data_dict['TRDFrontal'], self.data_dict['TRIFrontal'], 'Rodilla en el plano Frontal data Transformada', 'Tiempo (ms)', 'RD vs RI')
        self._create_table_section(self.data_dict, 'Sagital')
        self._create_table_section(self.data_dict, 'Frontal')'''
        plt.rcParams.update(custom_style)
        pdf_path = get_patient_doc_file(str(self.patient.ci), self._get_current_date_and_timestamp())
        self.output(pdf_path)
        return pdf_path