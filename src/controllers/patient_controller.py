class PatientController:
    def __init__(self) -> None:
        self.ci:int|None = None
        self.name:str|None = None
        self.birthday:str|None = None
        self.age:str|None = None
        self.gender:str|None = None
        self.phone:str|None = None
        self.mail:str|None = None
        self.right_leg_size:float|None = None
        self.left_leg_size:float|None = None
        self.folder_path:str|None = None
    
    def update_patient(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
    
    def clear_patient (self):
        self.ci = None
        self.name = None
        self.birthday = None
        self.age = None
        self.gender = None
        self.phone = None
        self.mail = None
        self.right_leg_size = None
        self.left_leg_size = None
        self.folder_path = None
    
    def __str__(self) -> str:
        return f'Paciente: {self.name} CI: {self.ci}'
                

