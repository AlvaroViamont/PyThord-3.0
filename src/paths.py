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

PATIENT_FOLDER = os.path.join(os.path.dirname(SRC_FOLDER), "patients")

def create_patient_structure (ci):
    analysis_folder = os.path.join(PATIENT_FOLDER, ci, 'data')
    os.makedirs(analysis_folder)

def save_dict_to_json(data_dict, ci, filename):
    folder_path = os.path.join(PATIENT_FOLDER, ci, 'data')
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    file_path = os.path.join(folder_path, f"{filename}.json")
    with open(file_path, 'w') as json_file:
        json.dump(data_dict, json_file, indent=4)
    print('json guardado')

def delete_patient_structure (ci):
    folder_path = os.path.join(PATIENT_FOLDER, ci, 'data')
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
