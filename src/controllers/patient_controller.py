class PatientController:
    def __init__(self) -> None:
        self.ci:int|None = None
        self.name:str|None = None
        self.birthday:str|None = None
        self.age:str|None = None
        self.gender:str|None = None
        self.phone:str|None = None
        self.mail:str|None = None
        self.right_leg_size:float = 0
        self.left_leg_size:float = 0
        self.folder_path:str|None = None
        self.cadence:float = 0
        self.average_time:float = 0
        self.speed:float = 0
        self.mean_distancel:float = 0
        self.mean_distancer:float = 0
        self.left_time:float = 0
        self.right_time:float = 0
    
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
        self.right_leg_size = 0
        self.left_leg_size = 0
        self.folder_path = 0
        self.cadence = 0
        self.average_time = 0
        self.speed = 0
        self.mean_distancel = 0
        self.mean_distancer = 0
        self.left_time = 0
        self.right_time = 0
    
    def __str__(self) -> str:
        return f'Paciente: {self.name} CI: {self.ci}'
                

