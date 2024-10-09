from models.patient import Patient
from models.stride import Stride
from models.user import User
from models.report import PDF
from views.user_view import User_View
from views.patient_view import Patient_View
from views.analytics_view import Analytic_View
from controllers.patient_controller import PatientController
from controllers.serial_controller import SerialController
from controllers.data_controller import DataController

from paths import create_patient_structure, get_patient_folder, delete_patient_structure, open_patient_folder, save_dict_to_json, open_pdf_document, get_json_to_dict

import models.encrypt as nc
import tkinter as tk
from datetime import datetime
import threading
import time

class AppController:
    def __init__(self, user_model, patient_model, stride_model, user_view=None, patient_view=None, stride_view=None):
        self.user_db:User = user_model
        self.patient_db:Patient = patient_model
        self.stride_db:Stride = stride_model
        self.user_view:User_View|None = user_view
        self.patient_view:Patient_View|None = patient_view
        self.stride_view:Analytic_View|None = stride_view
        
        self.login_direction:int = -1
        self.login_user:str = None
        
        self.patient:PatientController = PatientController()
        self.serial:SerialController = SerialController()
        self.data:DataController = DataController()
        
        self.connection_status = True
        self.thread:threading.Thread|None = None
    
    def logup_redirection (self):
        self.login_direction = 0
        self.user_view.login_view()

    def login_redirection (self):
        self.login_direction = 1
        self.user_view.login_view()
    
    def logout_buttom (self):
        self.login_direction = -1
        self.login_user = None
        self.user_view.widget_grid_forget(self.user_view.register_user_view_search_bottom_frame)
        self.user_view.widget_pack_forget(self.user_view.register_user_view_forms_frame_b)
        self.user_view.register_user_view_create_user_buttom.configure(background=self.user_view.ANTI_FLASH_WHITE)
        self.user_view.register_user_view_create_user_buttom.configure(foreground=self.user_view.ONYX)
        self.user_view.register_user_view_search_user_buttom.configure(background=self.user_view.ANTI_FLASH_WHITE)
        self.user_view.register_user_view_search_user_buttom.configure(foreground=self.user_view.ONYX)
        self.user_view.principal_view()
    
    def redirection_login_buttom(self):
        user = self.user_view.login_view_user_entry.get()
        password = self.user_view.login_view_password_entry.get()
        user_data = self.user_db.get_user(user)
        if user_data:
            key = nc.remov_string_b(user_data[0])
            stored_password = nc.remov_string_b(user_data[2])
            decrypted_password = nc.remov_string_b(str(nc.decrypt(stored_password, key)))
            if password == decrypted_password:
                self.login_user = user_data[1]
                if self.login_direction == 0:
                    self.user_view.register_search_user_view_user_name_label.configure(text=self.login_user)
                    self.user_view.crud_user_frame()
                elif self.login_direction == 1:
                    self.patient_view.patient_view_top_frame_user_name_label.configure(text=self.login_user)
                    self.patient_view.build_main_patient_view()
            else:
                self.user_view.show_error("Login Error", "Incorrect password.")
        else:
            self.user_view.show_error("Login Error", "User not found.")
        self.user_view.login_view_user_entry.delete(0, tk.END)
        self.user_view.login_view_password_entry.delete(0, tk.END)
    
    def create_new_user_buttom (self):
        user = self.user_view.register_user_view_user_name_entry.get()
        password = self.user_view.register_user_view_new_password_entry.get()
        repear_password = self.user_view.register_user_view_repeat_password_entry.get()
        user_data = self.user_db.get_user(user)
        if user == "":
            self.user_view.show_error("Registration Error", "Empty username")
        elif password == "":
            self.user_view.show_error("Registration Error", "Empty password")
        elif repear_password == "":
            self.user_view.show_error("Registration Error", "Empty password confirmation")
        elif user_data:
            self.user_view.show_error("Registration Error", "Existing username")
        elif password != repear_password:
            self.user_view.show_error("Registration Error", "Passwords do not match")
        else:
            key, encrypt_password = nc.encrypt(password)
            self.user_db.create_user(str(key), user, str(encrypt_password))
            self.user_view.show_info("Successful registration", "A new user has registered")
        self.user_view.register_user_view_user_name_entry.delete(0, tk.END)
        self.user_view.register_user_view_new_password_entry.delete(0, tk.END)
        self.user_view.register_user_view_repeat_password_entry.delete(0, tk.END)
    
    def cancel_button_funtion (self):
        self.user_view.register_user_view_user_name_entry.delete(0, tk.END)
        self.user_view.register_user_view_new_password_entry.delete(0, tk.END)
        self.user_view.register_user_view_repeat_password_entry.delete(0, tk.END)
    
    def update_password_buttom (self):
        user = self.login_user
        password = self.user_view.register_user_view_update_password_entry.get()
        repeat = self.user_view.register_user_view_update_repeat_password_entry.get()
        if password != "" and repeat != "":
            if password == repeat:
                conf = self.user_view.ask_yes_no("Actualiza contraseña", "Esta seguro que quiere actualizar contraseña")
                if conf:
                    key, encrypt_password = nc.encrypt(password)
                    self.user_db.update_password(str(key), user, str(encrypt_password))
                    self.user_view.show_info("Registro Exitoso", "Se hizo el cambio de contraseña de forma correcta.")
            else:
                self.user_view.show_error("Error", "Campos No Coinciden")
        else:
            self.user_view.show_error("Error", "Campos en blanco")
        self.user_view.register_user_view_update_password_entry.delete(0, tk.END)
        self.user_view.register_user_view_update_repeat_password_entry.delete(0, tk.END)
    
    def delete_user_buttom (self):
        user = self.user_view.register_user_view_user_info_user_name_label['text']
        if self.user_view.ask_yes_no("Eliminar Usuario", "¿Estas seguro de eliminar este usuario?"):
            self.user_db.delete_user(user)
            self.user_view.show_info("Exito", "Usuario eliminado correctamente")
            self.user_view.widget_grid_forget(self.user_view.register_user_view_search_bottom_frame)
            if user == self.login_user:
                self.logout_buttom()
    
    def search_logout_buttom (self):
        self.login_direction = -1
        self.login_user = None
        self.patient_view.widget_grid_forget(self.patient_view.patient_view_new_patient_frame)
        self.patient_view.widget_pack_forget(self.patient_view.patient_view_search_patient_frame)
        self.patient_view.widget_pack_forget(self.patient_view.patient_view_main_buttons_frame)
        self.patient_view.patient_view_create_buttom.configure(background=self.patient_view.ANTI_FLASH_WHITE)
        self.patient_view.patient_view_create_buttom.configure(foreground=self.patient_view.ONYX)
        self.patient_view.patient_view_search_buttom.configure(background=self.patient_view.ANTI_FLASH_WHITE)
        self.patient_view.patient_view_search_buttom.configure(foreground=self.patient_view.ONYX)
        self.patient.clear_patient()
        self.patient_view.principal_view()
    
    def create_new_patient (self):
        ci = self.patient_view.patient_view_patient_ci_entry.get()
        if ci == '':
            return (False, 'Error', 'Empty CI Entry')
        patient_exist = self.patient_db.get_patient_by_id(ci)
        if patient_exist:
            return (False, 'Error', 'Existent CI')
        day = self.patient_view.patient_view_patient_birthdate_day_entry.get()
        if day == '':
            return (False, 'Error', 'Empty Day Entry')
        month = self.patient_view.patient_view_patient_birthdate_month_entry.get()
        if month == '':
            return (False, 'Error', 'Empty Month Entry')
        year = self.patient_view.patient_view_patient_birthdate_year_entry.get()
        if year == '':
            return (False, 'Error', 'Empty Year Entry')
        name = self.patient_view.patient_view_patient_name_entry.get()
        if name == '':
            return (False, 'Error', 'Empty Name Entry')
        last_name = self.patient_view.patient_view_patient_lastname_entry.get()
        if last_name == '':
            return (False, 'Error', 'Empty Lastname Entry')
        vgender = self.patient_view.patient_view_check_var.get()
        if vgender == 1:
            gender = 'M'
        elif vgender == 2:
            gender = 'F'
        else:
            return (False, 'Error', 'No Gender Selected')
        full_name = ' '.join((name, last_name))
        phone = self.patient_view.patient_view_patient_phone_entry.get()
        mail = self.patient_view.patient_view_patient_mail_entry.get()
        date = '/'.join((day, month, year))
        age = self.age_calculator(date)
        right_leg_size = self.patient_view.patient_view_patient_right_leg_size_entry.get() 
        left_leg_size = self.patient_view.patient_view_patient_left_leg_size_entry.get()
        try:
            self.patient_db.create_patient(int(ci), name, last_name, date, gender, phone, mail, right_leg_size, left_leg_size)
            folder = create_patient_structure(ci)
            self.patient.update_patient(ci=int(ci), name=full_name, birthday=date, age=age, gender=gender, phone=phone, mail=mail, right_leg_size=right_leg_size, left_leg_size=left_leg_size, folder_path=folder)
            return (True, 'Success', 'Patient Registered Successfully')
        except:
            return (True, 'Error', 'Could Not Register Patient')
    
    def age_calculator (self, date):
        birthdate = datetime.strptime(date, "%d/%m/%Y")
        today = datetime.today()
        age = today.year - birthdate.year
        if (today.month, today.day) < (birthdate.month, birthdate.day):
            age -= 1
        return age

    def search_pattient_by_ci (self):
        patient = int(self.patient_view.patient_search_view_top_entry.get())
        patient_exist = self.patient_db.get_patient_by_id(patient)
        if patient_exist:
            ci = patient_exist[0]
            name = patient_exist[1]
            lastname = patient_exist[2]
            date = patient_exist[3]
            gender = patient_exist[4]
            phone = patient_exist[5]
            mail = patient_exist[6]
            full_name = ' '.join((name, lastname))
            age = self.age_calculator(date)
            right_leg_size = patient_exist[7]
            left_leg_size = patient_exist[8]
            folder = get_patient_folder(str(ci))
            self.patient.update_patient(ci=int(ci), name=full_name, birthday=date, gender=gender, age=age, phone=phone, mail=mail, right_leg_size=right_leg_size, left_leg_size=left_leg_size, folder_path=folder)
            return self.patient
        else:
            return False
    
    def search_all_pattient (self):
        patient_list =  list(self.patient_db.get_all_patient())
        patient_correct_list = []
        for patient in patient_list:
            ci = str(patient[0])
            name = ' '.join((patient[1], patient[2]))
            age = self.age_calculator(patient[3])
            gender = patient[4]
            patient_correct_list.append((ci, name, age, gender))
        return patient_correct_list
    
    def delete_patient (self):
        result = self.patient_db.delete_patient(self.patient.ci)
        if result == 's':
            delete_patient_structure(str(self.patient.ci))
            self.patient.clear_patient()
            return (True, 'Success', 'Patient Deleted Successfully')
        elif result == 'e1':
            return (False, 'Error', 'Could Not Deleted Patient')
        elif result == 'e2':
            return (False, 'Error', 'The Patient Does Not Exist')
    
    def update_patient (self):
        phone = self.patient_view.patient_search_focus_phone_entry.get()
        mail= self.patient_view.patient_search_focus_mail_entry.get()
        rsize = self.patient_view.patient_search_focus_right_leg_size_entry.get()
        lsize = self.patient_view.patient_search_focus_left_leg_size_entry.get()
        status = self.patient_db.update_patient(self.patient.ci, PATIENT_PHONE=phone, PATIENT_MAIL=mail, PATIENT_RSIZE=rsize, PATIENT_LSIZE=lsize)
        self.patient.update_patient(phone=phone, mail=mail, right_leg_size=rsize, left_leg_size=lsize)
        if status == 's':
            return (True, 'Success', 'Patient Update Successfully')
        elif status == 'e1':
            return (False, 'Error', 'Could Not Update Patient')
        elif status == 'e2':
            return (False, 'Error', 'The Patient Does Not Exist')
    
    def open_patient_folder (self):
        open_patient_folder (str(self.patient.ci))
    
    def launch_analytics_view (self):
        self.stride_view.stride_view_top_frame_user_name_label.configure(text=self.login_user)
        self.stride_view.stride_view_patient_full_name_label.configure(text=self.patient.name)
        self.stride_view.stride_view_patient_age_label.configure(text=self.patient.age)
        self.stride_view.build_main_stride_view()
    
    def back_to_patient_view (self):
        self.patient.clear_patient()
        self.patient_view.build_main_patient_view()
    
    def get_conection (self):
        if self.connection_status:
            self.serial.get_connection()
            if self.serial.connection:          
                self.connection_status = False
                time.sleep(2)
                self.stride_view.stride_view_serial_conection_label.configure(text=f"{self.serial.port}")
                self.stride_view.stride_view_serial_conection_buttom.configure(text='Desconectar')
                self.stride_view.stride_view_start_collection_buttom.configure(state='normal')
        else:
            if self.thread is not None and self.thread.is_alive():
                self.thread.join()
            self.stride_view.stride_view_serial_conection_label.configure(text="Sin Conexión")
            self.stride_view.stride_view_serial_conection_buttom.configure(text='Conectar')
            self.stride_view.stride_view_start_collection_buttom.configure(state='disabled')
            self.serial.disconect()
            self.data.clear()
            self.connection_status = True
    
    def update_plot(self, graph_type, joint, laterality):
        try:
            self.stride_view.stride_view_top_components_right_canvas.ax.clear()
            if graph_type == 0:
                if joint == 0:
                    if laterality in [0, 1]:
                        self.stride_view.stride_view_top_components_right_canvas.plot_data(self.data.stride_raw_data['CDTime(ms)'], self.data.stride_raw_data['CDFrontal'], "Cadera Derecha Frontal")
                    if laterality in [0, 2]:
                        self.stride_view.stride_view_top_components_right_canvas.plot_data(self.data.stride_raw_data['CITime(ms)'], self.data.stride_raw_data['CIFrontal'], "Cadera Izquierda Frontal")
                if joint == 1:
                    if laterality in [0, 1]:
                        self.stride_view.stride_view_top_components_right_canvas.plot_data(self.data.stride_raw_data['RDTime(ms)'], self.data.stride_raw_data['RDFrontal'], "Rodilla Derecha Frontal")
                    if laterality in [0, 2]:
                        self.stride_view.stride_view_top_components_right_canvas.plot_data(self.data.stride_raw_data['RITime(ms)'], self.data.stride_raw_data['RIFrontal'], "Rodilla Izquierda Frontal")
            if graph_type == 1:
                if joint == 0:
                    if laterality in [0, 1]:
                        self.stride_view.stride_view_top_components_right_canvas.plot_data(self.data.stride_raw_data['CDTime(ms)'], self.data.stride_raw_data['CDSagital'], "Cadera Derecha Sagital")
                    if laterality in [0, 2]:
                        self.stride_view.stride_view_top_components_right_canvas.plot_data(self.data.stride_raw_data['CITime(ms)'], self.data.stride_raw_data['CISagital'], "Cadera Izquierda Sagital")
                if joint == 1:
                    if laterality in [0, 1]:
                        self.stride_view.stride_view_top_components_right_canvas.plot_data(self.data.stride_raw_data['RDTime(ms)'], self.data.stride_raw_data['RDSagital'], "Rodilla Derecha Sagital")
                    if laterality in [0, 2]:
                        self.stride_view.stride_view_top_components_right_canvas.plot_data(self.data.stride_raw_data['RITime(ms)'], self.data.stride_raw_data['RISagital'], "Rodilla Izquierda Sagital")
            self.stride_view.stride_view_top_components_right_canvas.ax.grid(True)
            self.stride_view.stride_view_top_components_right_canvas.ax.legend()
            self.stride_view.stride_view_top_components_right_canvas.canvas.draw()
        except:
            pass
    
    def _data_collection_task (self):
        self.serial.connection.reset_input_buffer()
        self.serial.connection.reset_output_buffer()
        self.serial.connection.write(f'{self.data.data_size}'.encode('utf-8'))
        self.stride_view.stride_view_serial_data_taked_label.config(text='Recibiendo Datos')
        try:
            while True:
                    # Leer la línea completa de datos
                line = self.serial.connection.readline().decode('utf-8')
                # Separar la línea en sus componentes
                try:
                    decoder, cont, x, y = line.strip().split(',')
                    cont = int(cont)
                    ltime = cont*10
                    x = int(x)
                    y = int(y)
                    if decoder == "M":
                        if cont <= self.data.data_size and cont not in self.data.stride_raw_data['RIIndex']:
                            self.data.stride_raw_data['RIIndex'].append(cont)
                            self.data.stride_raw_data['RITime(ms)'].append(ltime)
                            self.data.stride_raw_data['RISagital'].append(x*-1)
                            self.data.stride_raw_data['RIFrontal'].append(y)
                    elif decoder == "N":
                        if cont <= self.data.data_size and cont not in self.data.stride_raw_data['RDIndex']:
                            self.data.stride_raw_data['RDIndex'].append(cont)
                            self.data.stride_raw_data['RDTime(ms)'].append(ltime)
                            self.data.stride_raw_data['RDSagital'].append(x)
                            self.data.stride_raw_data['RDFrontal'].append(y)
                    elif decoder == "O":
                        if cont <= self.data.data_size and cont not in self.data.stride_raw_data['CIIndex']:
                            self.data.stride_raw_data['CIIndex'].append(cont)
                            self.data.stride_raw_data['CITime(ms)'].append(ltime)
                            self.data.stride_raw_data['CISagital'].append(x*-1)
                            self.data.stride_raw_data['CIFrontal'].append(y)
                    elif decoder == "P":
                        if cont <= self.data.data_size and cont not in self.data.stride_raw_data['CDIndex']:
                            self.data.stride_raw_data['CDIndex'].append(cont)
                            self.data.stride_raw_data['CDTime(ms)'].append(ltime)
                            self.data.stride_raw_data['CDSagital'].append(x)
                            self.data.stride_raw_data['CDFrontal'].append(y)
                except Exception as e:
                    print (e)
                    continue
                try:
                    if all(self.data.stride_raw_data[key][-1] == self.data.data_size for key in ['RDIndex', 'CDIndex', 'RIIndex', 'CIIndex']):
                        self.data.control_data_rows()
                        self.data.transform_data()
                        self.data.get_min_and_max()
                        self.data.get_peaks()
                        self.data.set_distance(self.patient.right_leg_size)
                        self.data.get_average_time()
                        self.patient.speed = self.data.get_velocity()
                        self.patient.cadence = self.data.get_cadence()
                        self.patient.left_time = self.data.timel
                        self.patient.right_time = self.data.timer
                        self.patient.average_time = round((self.data.timel + self.data.timer) / 2, 2)
                        self.patient.mean_distancer = self.data.mean_distancer
                        self.patient.mean_distancel = self.data.mean_distancel
                        break
                except Exception as e:
                    print(e)
                    continue
            graph_type =self.stride_view.motion_planes_var.get()
            joint = self.stride_view.joints_var.get()
            laterality = self.stride_view.laterality_var.get()
            self.update_plot(graph_type, joint, laterality)
            self.stride_view.stride_view_serial_data_taked_label.config(text='Envio Finalizado')
            self.stride_view.stride_view_raw_data_max_min_valor_buttom.configure(state='normal')
            self.stride_view.stride_view_save_buttom.configure(state='normal')
            return True
        except Exception as e:
            print(e)
            pass
    
    def collect_data(self):
        self.stride_view.stride_view_save_buttom.configure(state='disabled')
        self.stride_view.stride_view_raw_data_max_min_valor_buttom.configure(state='disabled')
        if self.stride_view.stride_view_start_collection_buttom['text'] == 'Iniciar' and self.thread is None:
            self.data.clear()
            self.stride_view.stride_view_start_collection_buttom.configure(text='Reset')
            self.thread = threading.Thread(target=self._data_collection_task, daemon=True)
            self.thread.start()
        elif self.stride_view.stride_view_start_collection_buttom['text'] == 'Reset':
            self.serial.reset_connection()
            if self.thread is not None and self.thread.is_alive():
                self.stride_view.stride_view_serial_data_taked_label.config(text='')
                self.thread.join()
            self.thread = None
            time.sleep(2)
            self.data.clear()
            self.stride_view.stride_view_top_components_right_canvas.destroy_plot()
            self.stride_view.new_canvas()
            self.stride_view.stride_view_serial_data_taked_label.config(text='')
            self.stride_view.stride_view_start_collection_buttom.configure(text='Iniciar')
    
    def _get_current_date_and_timestamp(self):
        now = datetime.now()
        date_string = now.strftime("%d/%m/%Y")
        timestamp_string = now.strftime("%d%m%Y%H%M%S")
        return date_string, timestamp_string
    
    def make_report_pdf(self):
        report_pdf:PDF = PDF()
        report_pdf.patient = self.patient
        report_pdf.data = self.data
        report_pdf.report_date, report_pdf.report_name = self._get_current_date_and_timestamp()
        pdf_path = report_pdf.build()
        open_pdf_document(pdf_path)
    
    def save_raw_stride (self):
        stride_date, stride_id = self._get_current_date_and_timestamp()
        stride_document = ''.join((stride_id, '.json'))
        stride_description = ''
        save_dict_to_json(self.data.stride_raw_data, str(self.patient.ci), stride_id)
        self.stride_db.create_stride(stride_id, stride_date, stride_document, stride_description, self.patient.ci)
    
    def get_stride_date_patient (self):
        stride = self.stride_db.get_strides_by_patient(self.patient.ci)
        if stride:
            return [strd[0]+'.pdf' for strd in stride]
        else:
            return None

    def open_pdf_patient_document (self, pdf_path):
        try:
            open_pdf_document(pdf_path)
        except:
            name = pdf_path[:-4]
            pdf_json = pdf_path[:-4]+'.json'
            date = '/'.join((pdf_path[:2], pdf_path[2:4], pdf_path[4:8]))
            self._restore_pdf(pdf_json, date, name)
    
    def _restore_pdf (self, path, date, name):        
        auxiliar_data = DataController()
        auxiliar_data.stride_raw_data = get_json_to_dict(str(self.patient.ci), path)
        auxiliar_data.data_size = len(auxiliar_data.stride_raw_data['RDSagital'])
        auxiliar_data.data_time = auxiliar_data.data_size // 100
        auxiliar_data.transform_data()
        auxiliar_data.get_min_and_max()
        auxiliar_data.get_peaks()
        auxiliar_data.get_average_time()
        auxiliar_patient = PatientController()
        auxiliar_patient.update_patient(**self.patient.__dict__)
        auxiliar_data.set_distance(auxiliar_patient.right_leg_size)
        auxiliar_patient.speed = auxiliar_data.get_velocity()
        auxiliar_patient.cadence = auxiliar_data.get_cadence()
        auxiliar_patient.left_time = auxiliar_data.timel
        auxiliar_patient.right_time = auxiliar_data.timer
        auxiliar_patient.average_time = round((auxiliar_data.timel + auxiliar_data.timer)/2, 2)
        auxiliar_patient.mean_distancer = auxiliar_data.mean_distancer
        auxiliar_patient.mean_distancel = auxiliar_data.mean_distancel
        report_pdf:PDF = PDF()
        report_pdf.patient = auxiliar_patient
        report_pdf.data = auxiliar_data
        report_pdf.report_date = date
        report_pdf.report_name = name
        pdf_path = report_pdf.build()
        open_pdf_document(pdf_path)