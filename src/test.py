import json
from paths import get_file
import re
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import scipy.signal as signal

file1 = "30092024230928.json"
file2 = "30092024230250.json"
file3 = "30092024231355.json"

j_file = get_file("4382916", file3)

with open(j_file, 'r') as file:
    data = json.load(file)

max_value = np.mean(data['RDSagital'])
peaks, _ = signal.find_peaks(data['RDSagital'], height=max_value, distance=80)

peaks2, _ = signal.find_peaks(data['RISagital'], height=max_value, distance=80)

peaks3, _ = signal.find_peaks(-np.array(data['RDSagital']), height=max_value, distance=80)

peaks4, _ = signal.find_peaks(-np.array(data['RISagital']), height=max_value, distance=80)

peak_values = np.array(data['RDSagital'])[peaks]
peak_values2 = np.array(data['RISagital'])[peaks2]
peak_values3 = np.array(data['RDSagital'])[peaks3]
peak_values4 = np.array(data['RISagital'])[peaks4]

print("Índices de los picos RD:", peaks)
print("Valores de los picos RD:", peak_values)
print("Cantidad de picos RD: ", len(peaks))
print("Índices de los picos RI:", peaks2)
print("Valores de los picos RI:", peak_values2)
print("Cantidad de picos RI: ", len(peaks2))

tiempo = data['RDTime(ms)'][peaks[-1]]
print('Tiempo Ultimo pico RD: ', tiempo)

tiempo2 = data['RITime(ms)'][peaks2[-1]]
print('Tiempo Ultimo pico RI: ', tiempo2)

cadencia = ((len(peaks2) + len(peaks))*60)/3
print(f'Cadencia: {cadencia} pasos/minuto')

plt.plot(data['RDTime(ms)'], data['RDSagital'], label='RD')
plt.plot(data['RDTime(ms)'], data['RISagital'], label='RI')
plt.plot(peaks*10, peak_values, "x", label='PicosRI+')
plt.plot(peaks2*10, peak_values2, "x", label='PicosRD+')
plt.plot(peaks3*10, peak_values3, "o", label='PicosRD-')
plt.plot(peaks4*10, peak_values4, "o", label='PicosRI-')
plt.xlabel("Índice")
plt.ylabel("Valor")
plt.legend()
plt.show()
