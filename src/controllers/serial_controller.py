import serial
import serial.tools.list_ports as port_lst

class SerialController:
    def __init__(self) -> None:
        self.speed:str = '115200'
        self.data_size:int = 300
        self.port:str|None = None
        self.connection:serial.Serial|None = None
    
    def get_connection (self) -> None:
        for port in port_lst.comports():
            try:
                self.port = port.device
                self.connection = serial.Serial(self.port, self.speed, timeout=1)
            except:
                pass
    
    def reset_connection (self):
        self.connection.reset_input_buffer()
        self.connection.reset_output_buffer()
        self.connection.close()
        self.connection.open()
    
    def disconect (self):
        self.connection.reset_input_buffer()
        self.connection.reset_output_buffer()
        self.connection.close()
        self.port = None
        self.connection = None