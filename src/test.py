from controllers.serial_controller import SerialController
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import threading
import time

serial = SerialController()
data_size = 300
timedata = data_size//100

# Diccionarios para almacenar los datos recibidos
RI = {
    'Time': [],
    'Sagital': [],
    'Frontal': []
}

RD = {
    'Time': [],
    'Sagital': [],
    'Frontal': []
}

CI = {
    'Time': [],
    'Sagital': [],
    'Frontal': []
}

CD = {
    'Time': [],
    'Sagital': [],
    'Frontal': []
}

data_dicts = (RI, RD, CI, CD)
hot_list1 = []
hot_list2 = []
hot_count = 0
ani = None
thread = None  # Variable global para el hilo de datos

root = tk.Tk()
root.title("Gráfico en tiempo real")

fig, ax = plt.subplots()

# Crear el canvas de Matplotlib en Tkinter
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

def take_data():
    serial.connection.reset_output_buffer()
    serial.connection.reset_input_buffer()
    serial.connection.write(f'{data_size}'.encode('utf-8'))
    start_time = time.time()
    while True:
        try:
            line = serial.connection.readline().decode('utf-8')
            decoder, cont, x, y = line.strip().split(',')
            cont = int(cont)
            x = float(x)
            y = float(y)
            
            # Almacenar datos según el controlador
            if decoder == 'M': 
                RI['Time'].append(cont * 10)
                RI['Sagital'].append(x*-1)
                RI['Frontal'].append(y)
            elif decoder == 'N': 
                RD['Time'].append(cont * 10)
                RD['Sagital'].append(x)
                RD['Frontal'].append(y)
            elif decoder == 'O': 
                CI['Time'].append(cont * 10)
                CI['Sagital'].append(x*-1)
                CI['Frontal'].append(y)
            elif decoder == 'P': 
                CD['Time'].append(cont * 10)
                CD['Sagital'].append(x)
                CD['Frontal'].append(y)
        except Exception as e:
            print(f"Error: {e}")
        if time.time() - start_time >= 6:
            break
    return True

def clear_data():
    for controllers in data_dicts:
        for list_controller in controllers.values():
            list_controller.clear()

def update_graph(frame):
    ax.clear()
    if RI['Time'] and RI['Sagital']:
        ax.plot(RI['Time'], RI['Sagital'], label='Rodilla Izquierda')
    if RD['Time'] and RD['Sagital']:
        ax.plot(RD['Time'], RD['Sagital'], label='Rodilla Derecha')
    plt.xlabel('Tiempo (ms)')
    plt.ylabel('Angulo (grados)')

def build_hot_list (frame):
    global hot_count, ani
    hot_list1.append(hot_count*10)
    hot_list2.append(5)
    hot_count += 1
    ax.clear()
    ax.plot(hot_list1, hot_list2)
    ax.set_xlabel('Tiempo (s)')
    ax.set_ylabel('Valor del dato')
    ax.set_title('Gráfico en tiempo real')
    if hot_count >= 50:
        ani.event_source.stop()

def conectar():
    global ani
    serial.get_connection()
    ani = animation.FuncAnimation(fig, build_hot_list, interval=10, cache_frame_data=False)
    canvas.draw()

def iniciar():
    global thread, ani
    if thread is None or not thread.is_alive():
        clear_data()
        thread = threading.Thread(target=take_data, daemon=True)
        thread.start()
        ani = animation.FuncAnimation(fig, update_graph, interval=10, cache_frame_data=False)
        canvas.draw()

def reset():
    ax.clear()
    clear_data()
    if thread.is_alive():
        thread.join(timeout=1)
    serial.reset_connection()
    canvas.draw()

def cerrar():
    try:
        if thread is not None and thread.is_alive():
            thread.join(timeout=1)
        serial.disconect()
        root.quit()
        plt.close('all')
    except:
        root.quit()
        plt.close('all')

aux_frame = tk.Frame(root)
aux_frame.pack(side=tk.BOTTOM, fill=tk.X)

# Crear botones para la interfaz de usuario
button = tk.Button(aux_frame, text="Cerrar", command=cerrar)
button.pack(side=tk.LEFT)
buttonR = tk.Button(aux_frame, text="Reset", command=reset)
buttonR.pack(side=tk.LEFT)
buttonI = tk.Button(aux_frame, text="Iniciar", command=iniciar)
buttonI.pack(side=tk.LEFT)
buttonC = tk.Button(aux_frame, text="Conectar", command=conectar)
buttonC.pack(side=tk.LEFT)

root.protocol("WM_DELETE_WINDOW", cerrar)
root.mainloop()
