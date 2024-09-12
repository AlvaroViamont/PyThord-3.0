import json
from paths import get_file
import re
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

class Example:
    def __init__(self, data:dict):
        self.dict_data = data
        self.old_data = None
        self.new_data = None
    
    def _hip_transform_sagital (self, hip_angle):
        if hip_angle < 0:
            return 180 - abs(hip_angle)
        else:
            return 180 + abs(hip_angle)
    
    def _knee_transform_sagital (self, hip_angle, knee_angle):
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
        self.old_data = self.dict_data.copy()
        self.new_data = self.dict_data.copy()
        for key in self.old_data.keys():
            words = self._split_on_uppercase(key)
            if words[-1] == 'Sagital':
                if words[0] == 'C':
                    self.new_data[key] = list(map(lambda hip: self._hip_transform_sagital(hip), self.old_data[key]))
                elif words[0] == 'R':
                    hip_key = 'C'+''.join(words[1:])
                    self.new_data[key] = list(map(lambda hip, knee: self._knee_transform_sagital(hip, knee), self.old_data[hip_key], self.old_data[key]))
            elif words[-1] == 'Frontal':
                if words[0] == 'C':
                    # hip_transform_frontal
                    self.new_data[key] = self.old_data[key]
                elif words[0] == 'R':
                    # knee_transform_frontal
                    self.new_data[key] = self.old_data[key]
            else:
                self.new_data[key] = self.old_data[key]

j_file = get_file("4382916", "08092024195428.json")

with open(j_file, 'r') as file:
    data = json.load(file)

my_data = Example(data)
my_data.transform_data()
for nlist in my_data.new_data.keys():
    if 'Index' in nlist:
        klist = my_data.new_data[nlist]
        c = 1
        for i in klist:
            if i != c:
                print(nlist, c)
                c = c + 1
            c = c + 1
fig, ax = plt.subplots()

'''def plot_data(x_data, y_data, label):
        ax.plot(x_data, y_data, label=label)
        plt.ylim(min(y_data)-20, max(y_data)+20)
        plt.xlim(0, 5250)
        plt.xlabel('Tiempo (ms)')
        plt.ylabel('Angulo (grados)')
        y_min, y_max = plt.ylim()
        x_min, x_max = plt.xlim()
        y_ticks = np.arange(y_min, y_max + 20, 20)
        x_ticks = np.arange(x_min, x_max +20, 100)
        plt.yticks(y_ticks)
        plt.xticks(x_ticks)
        
my_data.new_data['RITime(ms)'].append(my_data.new_data['RITime(ms)'][-1]+15)
my_data.new_data['RISagital'].append(my_data.new_data['RISagital'][-1])

plot_data(my_data.new_data['RDTime(ms)'], my_data.new_data['RDSagital'], "Rodilla Derecha Sagital")
plot_data(my_data.new_data['RITime(ms)'][:-1], my_data.new_data['RISagital'], "Rodilla Izquierda Sagital")
ax.grid(True)
ax.legend()
plt.show()'''
