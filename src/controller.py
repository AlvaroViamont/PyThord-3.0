import models.encrypt as nc
from models.patient import Patient
from models.stride import Stride
from models.user import User
from views.user_view import User_View
from views.patient_view import Patient_View
from views.analytics_view import Analytic_View
from paths import create_patient_structure, save_dict_to_json, open_patient_folder, delete_patient_structure
import tkinter as tk
from datetime import datetime
import serial
import serial.tools.list_ports as port_lst
import threading
import traceback
import re


class AppController:
    def __init__(self, user_model:User, patient_model:Patient, stride_model:Stride, user_view:User_View=None, patient_view:Patient_View=None, stride_view:Analytic_View=None):
        self.user_db = user_model
        self.patient_db = patient_model
        self.stride_db = stride_model
        self.user_view = user_view
        self.patient_view = patient_view
        self.stride_view = stride_view
        self.login_direction = -1
        self.login_user = None
        self.patient_ci = None
        self.patient_name = None
        self.patient_age = None
        
        self.speed = '115200'
        self.data_size = 300
        self.connection_status = True
        self.port = None
        self.connection = None
        self.reader = None
        self.writer = None
        self.collected_data = False
        
        self.final_data_collected = None
        
        self.data_colecteted = None
        
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
        phone = self.patient_view.patient_view_patient_phone_entry.get()
        direc = self.patient_view.patient_view_patient_direction_entry.get()
        mail = self.patient_view.patient_view_patient_mail_entry.get()
        date = '/'.join((day, month, year))
        try:
            self.patient_db.create_patient(int(ci), name, last_name, date, gender, phone, mail, direc)
            create_patient_structure(ci)
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
            direction = patient_exist[7]
            full_name = ' '.join((name, lastname))
            age = self.age_calculator(date)
            return (str(ci), full_name, date, str(age), gender, phone, mail, direction)
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
        ci = int(self.patient_view.patient_search_focus_ci_label['text'])
        result = self.patient_db.delete_patient(ci)
        if result == 's':
            delete_patient_structure(str(ci))
            return (True, 'Success', 'Patient Deleted Successfully')
        elif result == 'e1':
            return (False, 'Error', 'Could Not Deleted Patient')
        elif result == 'e2':
            return (False, 'Error', 'The Patient Does Not Exist')
    
    def update_patient (self):
        status = self.patient_db.update_patient(int(self.patient_view.patient_search_focus_ci_label['text']), PATIENT_PHONE=self.patient_view.patient_search_focus_phone_entry.get(), PATIENT_MAIL=self.patient_view.patient_search_focus_mail_entry.get(), PATIENT_ADDRESS=self.patient_view.patient_search_focus_dir_entry.get())
        if status == 's':
            return (True, 'Success', 'Patient Update Successfully')
        elif status == 'e1':
            return (False, 'Error', 'Could Not Update Patient')
        elif status == 'e2':
            return (False, 'Error', 'The Patient Does Not Exist')
    
    def open_patient_folder (self):
        ci = self.patient_view.patient_search_focus_ci_label['text']
        open_patient_folder (ci)
    
    def launch_analytics_view (self):
        self.patient_ci = int(self.patient_view.patient_search_focus_ci_label['text'])
        self.patient_name = self.patient_view.patient_search_focus_full_name_label['text']
        self.patient_age = self.patient_view.patient_search_focus_age_label['text']
        self.stride_view.stride_view_top_frame_user_name_label.configure(text=self.login_user)
        self.stride_view.stride_view_patient_full_name_label.configure(text=self.patient_name)
        self.stride_view.stride_view_patient_age_label.configure(text=self.patient_age)
        self.stride_view.build_main_stride_view()
    
    def back_to_patient_view (self):
        self.patient_ci = None
        self.patient_name = None
        self.patient_age = None
        self.patient_view.build_main_patient_view()
    
    def get_conection (self):
        if self.connection_status:
            for port in port_lst.comports():
                try:
                    self.port = port.device
                    self.connection = serial.Serial(self.port, self.speed, timeout=1)
                    self.connection_status = False
                    self.stride_view.stride_view_serial_conection_label.configure(text=f"{self.port}")
                    self.stride_view.stride_view_serial_conection_buttom.configure(text='Desconectar')
                    self.stride_view.stride_view_start_collection_buttom.configure(state='normal')
                    self.connection.reset_input_buffer()
                    self.connection.reset_output_buffer()
                    break
                except Exception as e:
                    pass
        else:
            self.stride_view.stride_view_serial_conection_label.configure(text="Sin Conexión")
            self.stride_view.stride_view_serial_conection_buttom.configure(text='Conectar')
            self.stride_view.stride_view_start_collection_buttom.configure(state='disabled')
            self.port = None
            self.connection.reset_input_buffer()
            self.connection.reset_output_buffer()
            self.connection.close()
            self.connection = None
            self.connection_status = True

    def collect_data(self):
        """
        Recibe datos de la conexión serie establecida y actualiza los datos del gráfico en tiempo real.
        """
        self.connection.reset_input_buffer()
        self.connection.reset_output_buffer()
        self.connection.write(f'{self.data_size}'.encode('utf-8'))  # Enviar señal para iniciar la recolección de datos

        def data_collection_task ():
            self.stride_view.stride_view_top_components_right_canvas.clear_list()
            self.stride_view.stride_view_save_buttom.configure(state='disabled')
            self.stride_view.stride_view_to_doc_buttom.configure(state='disabled')
            self.stride_view.plot_view_var.set(0)
            self.stride_view.stride_view_unique_plot_radiobuttom.configure(state='disabled')
            self.stride_view.stride_view_multiple_plot_radiobuttom.configure(state='disabled')
            try:
                while True:
                        # Leer la línea completa de datos
                    self.data_colecteted = self.connection.readline().decode('UTF-8')
                    if self.data_colecteted:
                        # Separar la línea en sus componentes
                        decoder, cont, x, y = self.data_colecteted.strip().split(',')
                        cont = int(cont)
                        time = cont*10
                        x = int(x)
                        y = int(y)
                        if decoder == "N":
                            if cont <= self.data_size and cont not in self.stride_view.stride_view_top_components_right_canvas.data_collected['RDIndex']:
                                self.stride_view.stride_view_top_components_right_canvas.data_collected['RDIndex'].append(cont)
                                self.stride_view.stride_view_top_components_right_canvas.data_collected['RDTime(ms)'].append(time)
                                self.stride_view.stride_view_top_components_right_canvas.data_collected['RDSagital'].append(x)
                                self.stride_view.stride_view_top_components_right_canvas.data_collected['RDFrontal'].append(y)
                        elif decoder == "P":
                            if cont <= self.data_size and cont not in self.stride_view.stride_view_top_components_right_canvas.data_collected['CDIndex']:
                                self.stride_view.stride_view_top_components_right_canvas.data_collected['CDIndex'].append(cont)
                                self.stride_view.stride_view_top_components_right_canvas.data_collected['CDTime(ms)'].append(time)
                                self.stride_view.stride_view_top_components_right_canvas.data_collected['CDSagital'].append(x)
                                self.stride_view.stride_view_top_components_right_canvas.data_collected['CDFrontal'].append(y)
                        elif decoder == "M":
                            if cont <= self.data_size and cont not in self.stride_view.stride_view_top_components_right_canvas.data_collected['RIIndex']:
                                self.stride_view.stride_view_top_components_right_canvas.data_collected['RIIndex'].append(cont)
                                self.stride_view.stride_view_top_components_right_canvas.data_collected['RITime(ms)'].append(time)
                                self.stride_view.stride_view_top_components_right_canvas.data_collected['RISagital'].append(x*-1)
                                self.stride_view.stride_view_top_components_right_canvas.data_collected['RIFrontal'].append(y*-1)
                        elif decoder == "O":
                            if cont <= self.data_size and cont not in self.stride_view.stride_view_top_components_right_canvas.data_collected['CIIndex']:
                                self.stride_view.stride_view_top_components_right_canvas.data_collected['CIIndex'].append(cont)
                                self.stride_view.stride_view_top_components_right_canvas.data_collected['CITime(ms)'].append(time)
                                self.stride_view.stride_view_top_components_right_canvas.data_collected['CISagital'].append(x*-1)
                                self.stride_view.stride_view_top_components_right_canvas.data_collected['CIFrontal'].append(y*-1)
                        
                        self.stride_view.stride_view_serial_data_taked_label.config(text=f'ID: {decoder} Contador: {cont} X: {x} Y: {y}')
                        self.stride_view.stride_view_serial_data_taked_label.update_idletasks()
                            # Graficar los datos recolectados en tiempo real
                        graph_type =self.stride_view.motion_planes_var.get()
                        joint = self.stride_view.joints_var.get()
                        laterality = self.stride_view.laterality_var.get()
                        self.stride_view.stride_view_top_components_right_canvas.update_plot(graph_type, joint, laterality)
                        try:
                            if all(self.stride_view.stride_view_top_components_right_canvas.data_collected[key][-1] == self.data_size for key in ['RDIndex', 'CDIndex', 'RIIndex', 'CIIndex']):
                                self.connection.reset_input_buffer()
                                self.connection.reset_output_buffer()
                                self.stride_view.stride_view_top_components_right_canvas.data_collected_saved = self.stride_view.stride_view_top_components_right_canvas.data_collected.copy()
                                break
                        except Exception as e:
                            pass
                self.stride_view.stride_view_serial_data_taked_label.config(text='Envio Finalizado')
                self.stride_view.stride_view_save_buttom.configure(state='normal')
                self.stride_view.stride_view_to_doc_buttom.configure(state='normal')
                self.stride_view.stride_view_unique_plot_radiobuttom.configure(state='normal')
                self.stride_view.stride_view_multiple_plot_radiobuttom.configure(state='normal')
                self.collected_data = True
            except Exception as e:
                print("Error receiving data:", e)
                print("Detalles del error:")
                traceback.print_exc()
        thread = threading.Thread(target=data_collection_task)
        thread.start()

    def _hip_transform_sagital (self, hip_angle):
        if hip_angle < 0:
            return 180 - abs(hip_angle)
        else:
            return 180 + abs(hip_angle)
    
    def _knee_transform_sagital (self, hip_angle, knee_angle):
        convert = True
        if hip_angle < 0:
            return 180 + abs(hip_angle) - abs(knee_angle)
        else:
            return 180 - abs(hip_angle) + abs(knee_angle)
    
    def _hip_transform_frontal (self):
        pass
    
    def _knee_transform_frontal (self):
        pass

    def _split_on_uppercase(self, s):
        return re.findall(r'[A-Z][a-z]*', s)
    
    def transform_data (self):
        for key in self.stride_view.stride_view_top_components_right_canvas.data_collected_saved.keys():
            words = self._split_on_uppercase(key)
            if words[-1] == 'Sagital':
                if words[0] == 'C':
                    self.stride_view.stride_view_top_components_right_canvas.data_transformed[key] = list(map(lambda hip: self._hip_transform_sagital(hip), self.stride_view.stride_view_top_components_right_canvas.data_collected_saved[key]))
                elif words[0] == 'R':
                    hip_key = 'C'+''.join(words[1:])
                    self.stride_view.stride_view_top_components_right_canvas.data_transformed[key] = list(map(lambda hip, knee: self._knee_transform_sagital(hip, knee), self.stride_view.stride_view_top_components_right_canvas.data_collected_saved[hip_key], self.stride_view.stride_view_top_components_right_canvas.data_collected_saved[key]))
            elif words[-1] == 'Frontal':
                if words[0] == 'C':
                    # hip_transform_frontal
                    self.stride_view.stride_view_top_components_right_canvas.data_transformed[key] = self.stride_view.stride_view_top_components_right_canvas.data_collected_saved[key]
                elif words[0] == 'R':
                    # knee_transform_frontal
                    self.stride_view.stride_view_top_components_right_canvas.data_transformed[key] = self.stride_view.stride_view_top_components_right_canvas.data_collected_saved[key]
            else:
                self.stride_view.stride_view_top_components_right_canvas.data_transformed[key] = self.stride_view.stride_view_top_components_right_canvas.data_collected_saved[key]
    
    def _get_current_date_and_timestamp(self):
        now = datetime.now()
        date_string = now.strftime("%d/%m/%Y")
        timestamp_string = now.strftime("%d%m%Y%H%M%S")
        return date_string, timestamp_string
    
    def save_raw_stride (self):
        stride_date, stride_id = self._get_current_date_and_timestamp()
        stride_document = ''.join((stride_id, '.json'))
        data_dict = self.stride_view.stride_view_top_components_right_canvas.data_collected_saved
        stride_description = ''
        save_dict_to_json(data_dict, str(self.patient_ci), stride_id)
        self.stride_db.create_stride(stride_id, stride_date, stride_document, stride_description, self.patient_ci)



