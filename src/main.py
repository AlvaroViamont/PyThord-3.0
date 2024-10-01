from views.user_view import User_View
from views.patient_view import Patient_View
from views.analytics_view import Analytic_View
from controllers.controller import AppController
from models.database_core import BBDD
from models.user import User
from models.patient import Patient
from models.stride import Stride
from models.report import PDF
import tkinter as tk


if __name__ == "__main__":
    root = tk.Tk ()
    con = BBDD()
    user_model = User (con)
    patient_model = Patient(con)
    stride_model = Stride(con)
    app_controller = AppController (user_model=user_model, patient_model=patient_model, stride_model=stride_model)
    user_view = User_View (root, app_controller)
    patient_view = Patient_View(root, app_controller)
    stride_view = Analytic_View(root, app_controller)
    app_controller.user_view = user_view
    app_controller.patient_view = patient_view
    app_controller.stride_view = stride_view
    con.conection()
    root.mainloop()