import os
import json
import shutil

SRC_FOLDER = os.path.dirname(__file__)
ASSETS_FOLDER = os.path.join(os.path.dirname(SRC_FOLDER), "assets")
DB_PATH = os.path.join(SRC_FOLDER, 'clinic.db')

IMG_LOGO_PATH = os.path.join(ASSETS_FOLDER, "image", "LOGO.png")
IMG_F_PP_01_PATH = os.path.join(ASSETS_FOLDER, "image", "f-pp.png")
IMG_F_PP_02_PATH = os.path.join(ASSETS_FOLDER, "image", "f-pp-02.png")
IMG_F_PP_03_PATH = os.path.join(ASSETS_FOLDER, "image", "f-pp-03.png")
IMG_F_PP_04_PATH = os.path.join(ASSETS_FOLDER, "image", "f-pp-04.png")
IMG_F_PP_05_PATH = os.path.join(ASSETS_FOLDER, "image", "f-pp-05.png")
IMG_F_PP_06_PATH = os.path.join(ASSETS_FOLDER, "image", "f-pp-06.png")
IMG_F_PP_07_PATH = os.path.join(ASSETS_FOLDER, "image", "f-pp-07.png")
IMG_F_PP_08_PATH = os.path.join(ASSETS_FOLDER, "image", "f-pp-08.png")
ICON_LOGO_PATH = os.path.join(ASSETS_FOLDER, "image", "LOGO.ico")

IMG_R_ABASE = os.path.join(ASSETS_FOLDER, "image", "ra_base.png")
IMG_R_BBASE = os.path.join(ASSETS_FOLDER, "image", "rb_base.png")
IMG_R_ARAW = os.path.join(ASSETS_FOLDER, "image", "ra_raw_angle.png")
IMG_R_BRAW = os.path.join(ASSETS_FOLDER, "image", "rb_raw_angle.png")
IMG_R_ATRN = os.path.join(ASSETS_FOLDER, "image", "ra_trn_angle.png")
IMG_R_BTRN = os.path.join(ASSETS_FOLDER, "image", "rb_trn_angle.png")

PATIENT_FOLDER = os.path.join(os.path.dirname(SRC_FOLDER), "patients")

def get_patient_folder (ci):
    return os.path.join(PATIENT_FOLDER, ci)

def create_patient_structure (ci):
    analysis_folder = os.path.join(PATIENT_FOLDER, ci, 'data')
    os.makedirs(analysis_folder)
    return get_patient_folder (ci)

def save_dict_to_json(data_dict, ci, filename):
    folder_path = os.path.join(PATIENT_FOLDER, ci, 'data')
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    file_path = os.path.join(folder_path, f"{filename}.json")
    with open(file_path, 'w') as json_file:
        json.dump(data_dict, json_file, indent=4)
    print('json guardado')

def delete_patient_structure (ci):
    folder_path = os.path.join(PATIENT_FOLDER, ci)
    shutil.rmtree(folder_path)
    
def open_patient_folder (ci):
    folder_path = os.path.join(PATIENT_FOLDER, ci)
    os.startfile(folder_path)

def get_file (ci, name):
    return os.path.join(PATIENT_FOLDER, ci, 'data', name)

def get_patient_doc_file (ci, document):
    return os.path.join(PATIENT_FOLDER, ci, document)

def open_pdf_document (path):
    os.startfile(path)

def get_json_to_dict (ci, path):
    with open(get_file(ci, path), 'r') as file:
            data = json.load(file)
    return data
