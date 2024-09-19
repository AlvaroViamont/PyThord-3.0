from fpdf import FPDF
import matplotlib.pyplot as plt
import io
import tempfile
import numpy as np
from PIL import Image
from datetime import datetime
from paths import IMG_LOGO_PATH, get_patient_doc_file


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
    def __init__(self, patient_data:dict = None, doctor_contact:str = None, report_date:str = None):
        super().__init__()
        self.patient_data = patient_data
        self.doctor_contact = doctor_contact
        self.report_date = report_date
        self.data_len = 3000
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
        self.add_page()
        self.set_font('Arial', 'B', 24)
        self.set_fill_color(255, 255, 255)
        self.set_text_color(50, 55, 59)
        self.ln(35)
        self.cell(180, 10, 'Análisis de Zancada', 0, 1, 'C', fill=True)
        self.ln(10)
        self.set_font('Arial', 'B', 12)
        self.set_text_color(50, 55, 59)
        self.cell(0, 0, f'Nombre del Paciente: {self.patient_data['name']}', 0, 1, 'L', True)
        self.ln(5)
        self.cell(0, 0, f'Edad del Paciente: {self.patient_data['age']}', 0, 1, 'L', True)
    
    def _create_plot_analytic_section(self, x_column, y_column, title, xlabel, ylabel):
        plt.figure(figsize=(8, 4))
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        x_min = 0
        x_max = self.data_len
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
    
    def _create_comparative_plot_analytic_section(self, x_column, y1_column, y2_column, title, xlabel, ylabel):
        plt.figure(figsize=(8, 4))
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        x_min = 0
        x_max = self.data_len
        x_ticks = np.arange(x_min, x_max + 20, self.data_len//10)
        plt.xticks(x_ticks)
        plt.grid(True)
        plt.plot(x_column, y1_column, label='Data 1')
        plt.plot(x_column, y2_column, label='Data 2')
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

    def build(self, data:dict):
        plt.rcParams.update(custom_style_2)
        self._first_page()
        self.add_page()
        self._create_comparative_plot_analytic_section(data['Time(ms)'], data['CDSagital'], data['CISagital'], 'Caderas en el plano Sagital data Original', 'Tiempo (ms)', 'CD vs CI')
        self._create_comparative_plot_analytic_section(data['Time(ms)'], data['CDFrontal'], data['CIFrontal'], 'Caderas en el plano Frontal data Original', 'Tiempo (ms)', 'CD vs CI')
        self.add_page()
        self._create_comparative_plot_analytic_section(data['Time(ms)'], data['RDSagital'], data['RISagital'], 'Rodilla en el plano Sagital data Original', 'Tiempo (ms)', 'RD vs RI')
        self._create_comparative_plot_analytic_section(data['Time(ms)'], data['RDFrontal'], data['RIFrontal'], 'Rodilla en el plano Frontal data Original', 'Tiempo (ms)', 'RD vs RI')
        self.add_page()
        self._create_comparative_plot_analytic_section(data['Time(ms)'], data['TCDSagital'], data['TCISagital'], 'Caderas en el plano Sagital data Transformada', 'Tiempo (ms)', 'CD vs CI')
        self._create_comparative_plot_analytic_section(data['Time(ms)'], data['TCDFrontal'], data['TCIFrontal'], 'Caderas en el plano Frontal data Transformada', 'Tiempo (ms)', 'CD vs CI')
        self.add_page()
        self._create_comparative_plot_analytic_section(data['Time(ms)'], data['TRDSagital'], data['TRISagital'], 'Rodilla en el plano Sagital data Transformada', 'Tiempo (ms)', 'RD vs RI')
        self._create_comparative_plot_analytic_section(data['Time(ms)'], data['TRDFrontal'], data['TRIFrontal'], 'Rodilla en el plano Frontal data Transformada', 'Tiempo (ms)', 'RD vs RI')
        self._create_table_section(data, 'Sagital')
        self._create_table_section(data, 'Frontal')
        plt.rcParams.update(custom_style)
        pdf_path = get_patient_doc_file(self.patient_data['ci'], self._get_current_date_and_timestamp())
        self.output(pdf_path)
        return pdf_path