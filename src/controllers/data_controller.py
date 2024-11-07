import re
import numpy as np
import math
import scipy.signal as signal
# from scipy.signal import find_peaks
class DataController:
    def __init__(self) -> None:
        self.stride_raw_data:dict[str, list[int]] = {
                'RDIndex':[], 'RDTime(ms)':[], 'RDSagital':[], 'RDFrontal':[],
                'CDIndex':[], 'CDTime(ms)':[], 'CDSagital':[], 'CDFrontal':[],
                'RIIndex':[], 'RITime(ms)':[], 'RISagital':[], 'RIFrontal':[],
                'CIIndex':[], 'CITime(ms)':[], 'CISagital':[], 'CIFrontal':[]
                                }
        self.stride_transform_data:dict[str, list[int]] = {
                'RDIndex':[], 'RDTime(ms)':[], 'RDSagital':[], 'RDFrontal':[],
                'CDIndex':[], 'CDTime(ms)':[], 'CDSagital':[], 'CDFrontal':[],
                'RIIndex':[], 'RITime(ms)':[], 'RISagital':[], 'RIFrontal':[],
                'CIIndex':[], 'CITime(ms)':[], 'CISagital':[], 'CIFrontal':[]
                                }
        self.stride_angle:dict[str, int] = {
            'MaxRD':0, 'MinRD':0,
            'MaxCD':0, 'MinCD':0,
            'MaxRI':0, 'MinRI':0,
            'MaxCI':0, 'MinCI':0,
            'TMaxRD':0, 'TMinRD':0,
            'TMaxCD':0, 'TMinCD':0,
            'TMaxRI':0, 'TMinRI':0,
            'TMaxCI':0, 'TMinCI':0
        }
        self.bases:tuple[str] = ('RDSagital', 'RISagital')
        self.data_size:int = 300
        self.data_time:int = 3
        self.ldata_ipeaks:np.array|None = None
        self.rdata_ipeaks:np.array|None = None
        self.ldata_peaks:np.array|None = None
        self.rdata_peaks:np.array|None = None
        self.mean_distancer:float|int|None = None
        self.mean_distancel:float|int|None = None
        self.timel:float|None = None
        self.timer:float|None = None
    
    def set_distance_time (self, time_teked:int):
        self.data_size = time_teked*100
        self.data_time = time_teked
    
    def clear (self):
        self.stride_raw_data = {
                'RDIndex':[], 'RDTime(ms)':[], 'RDSagital':[], 'RDFrontal':[],
                'CDIndex':[], 'CDTime(ms)':[], 'CDSagital':[], 'CDFrontal':[],
                'RIIndex':[], 'RITime(ms)':[], 'RISagital':[], 'RIFrontal':[],
                'CIIndex':[], 'CITime(ms)':[], 'CISagital':[], 'CIFrontal':[]
                                }
        self.stride_transform_data = {
                'RDIndex':[], 'RDTime(ms)':[], 'RDSagital':[], 'RDFrontal':[],
                'CDIndex':[], 'CDTime(ms)':[], 'CDSagital':[], 'CDFrontal':[],
                'RIIndex':[], 'RITime(ms)':[], 'RISagital':[], 'RIFrontal':[],
                'CIIndex':[], 'CITime(ms)':[], 'CISagital':[], 'CIFrontal':[]
                                }
        self.stride_angle = {
            'MaxRD':0, 'MinRD':0,
            'MaxCD':0, 'MinCD':0,
            'MaxRI':0, 'MinRI':0,
            'MaxCI':0, 'MinCI':0,
            'TMaxRD':0, 'TMinRD':0,
            'TMaxCD':0, 'TMinCD':0,
            'TMaxRI':0, 'TMinRI':0,
            'TMaxCI':0, 'TMinCI':0
        }
        self.data_size = 300
        self.data_time = 3
        self.ldata_ipeaks = None
        self.rdata_ipeaks = None
        self.ldata_peaks = None
        self.rdata_peaks = None
        self.mean_distancer = None
        self.mean_distancel = None
        self.timel = None
        self.timer = None
        
    def control_data_rows(self):
        for keys in self.stride_raw_data.keys():
            if 'Index' in keys:
                if self.stride_raw_data[keys][-1] < self.data_size:
                    self._insert_component(-1, keys[:2])
                for control in range(1, self.data_size):
                    if self.stride_raw_data[keys][control-1] != control:
                        self._insert_component(control, keys[:2])
    
    def _insert_component(self, index:int, key:str):
        real_index = index-1
        index_key = ''.join((key, 'Index'))
        time_key = ''.join((key, 'Time(ms)'))
        x_key = ''.join((key, 'Sagital'))
        y_key = ''.join((key, 'Frontal'))
        if index == 1:
            self.stride_raw_data[index_key].insert(real_index, index)
            time = 10
            self.stride_raw_data[time_key].insert(real_index, time)
            x = self.stride_raw_data[x_key][0]
            self.stride_raw_data[x_key].insert(real_index, x)
            y = self.stride_raw_data[y_key][0]
            self.stride_raw_data[y_key].insert(real_index, y)
        elif index == -1:
            self.stride_raw_data[index_key].append(self.data_size)
            time = self.data_size*10
            self.stride_raw_data[time_key].append(time)
            x = self.stride_raw_data[x_key][-1]
            self.stride_raw_data[x_key].append(x)
            y = self.stride_raw_data[y_key][-1]
            self.stride_raw_data[y_key].append(y)
        else:
            self.stride_raw_data[index_key].insert(real_index, index)
            time = self.stride_raw_data[time_key][real_index]
            self.stride_raw_data[time_key].insert(real_index, time)
            x = self.stride_raw_data[x_key][real_index]
            self.stride_raw_data[x_key].insert(real_index, x)
            y = self.stride_raw_data[y_key][real_index]
            self.stride_raw_data[y_key].insert(real_index, y)
    
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
    
    def _hip_transform_frontal (self, hip_angle):
        if hip_angle < 0:
            return 180 - abs(hip_angle)
        else:
            return 180 + abs(hip_angle)
    
    def _knee_transform_frontal (self, knee_angle):
        if knee_angle < 0:
            return 180 - abs(knee_angle)
        else:
            return 180 + abs(knee_angle)

    def _split_on_uppercase(self, s):
        return re.findall(r'[A-Z][a-z]*', s)
    
    def transform_data (self):
        for key in self.stride_raw_data.keys():
            words = self._split_on_uppercase(key)
            if words[-1] == 'Sagital':
                if words[0] == 'C':
                    self.stride_transform_data[key] = list(map(lambda hip: self._hip_transform_sagital(hip), self.stride_raw_data[key]))
                elif words[0] == 'R':
                    hip_key = 'C'+''.join(words[1:])
                    self.stride_transform_data[key] = list(map(lambda hip, knee: self._knee_transform_sagital(hip, knee), self.stride_raw_data[hip_key], self.stride_raw_data[key]))
            elif words[-1] == 'Frontal':
                if words[0] == 'C':
                    # hip_transform_frontal
                    self.stride_transform_data[key] = list(map(lambda hip: self._hip_transform_sagital(hip), self.stride_raw_data[key]))
                elif words[0] == 'R':
                    # knee_transform_frontal
                    self.stride_transform_data[key] = list(map(lambda knee: self._hip_transform_sagital(knee), self.stride_raw_data[key]))
            else:
                self.stride_transform_data[key] = self.stride_raw_data[key]
    
    def get_min_and_max (self):
        self.stride_angle['MaxRD'] = max(self.stride_raw_data['RDSagital'])
        self.stride_angle['MinRD'] = min(self.stride_raw_data['RDSagital'])
        self.stride_angle['MaxCD'] = max(self.stride_raw_data['CDSagital'])
        self.stride_angle['MinCD'] = min(self.stride_raw_data['CDSagital'])
        self.stride_angle['MaxRI'] = max(self.stride_raw_data['RISagital'])
        self.stride_angle['MinRI'] = min(self.stride_raw_data['RISagital'])
        self.stride_angle['MaxCI'] = max(self.stride_raw_data['CISagital'])
        self.stride_angle['MinCI'] = min(self.stride_raw_data['CISagital'])
        
        self.stride_angle['TMaxRD'] = max(self.stride_transform_data['RDSagital'])
        self.stride_angle['TMinRD'] = min(self.stride_transform_data['RDSagital'])
        self.stride_angle['TMaxCD'] = max(self.stride_transform_data['CDSagital'])
        self.stride_angle['TMinCD'] = min(self.stride_transform_data['CDSagital'])
        self.stride_angle['TMaxRI'] = max(self.stride_transform_data['RISagital'])
        self.stride_angle['TMinRI'] = min(self.stride_transform_data['RISagital'])
        self.stride_angle['TMaxCI'] = max(self.stride_transform_data['CISagital'])
        self.stride_angle['TMinCI'] = min(self.stride_transform_data['CISagital'])
    
    def get_peaks (self):
        max_value_d = np.mean(self.stride_raw_data['RDSagital'])
        max_value_i = np.mean(self.stride_raw_data['RISagital'])
        self.rdata_ipeaks, _ = signal.find_peaks(self.stride_raw_data['RDSagital'], height=max_value_d, distance=80)
        self.ldata_ipeaks, _ = signal.find_peaks(self.stride_raw_data['RISagital'], height=max_value_i, distance=80)
        self.nrdata_ipeaks, _ = signal.find_peaks(-np.array(self.stride_raw_data['RDSagital']), height=max_value_d, distance=80)
        self.nldata_ipeaks, _ = signal.find_peaks(-np.array(self.stride_raw_data['RISagital']), height=max_value_i, distance=80)
        self.rdata_peaks = np.array(self.stride_raw_data['RDSagital'])[self.rdata_ipeaks]
        self.ldata_peaks = np.array(self.stride_raw_data['RISagital'])[self.ldata_ipeaks]
        self.nrdata_peaks = np.array(self.stride_raw_data['RDSagital'])[self.nrdata_ipeaks]
        self.nldata_peaks = np.array(self.stride_raw_data['RISagital'])[self.nldata_ipeaks]
    
    def get_cadence (self):
        return ((len(self.rdata_ipeaks) + len(self.ldata_ipeaks))*60)/self.data_time
    
    def get_average_time(self): 
        rtimer = [self.stride_raw_data['RDTime(ms)'][self.rdata_ipeaks[i+1]] - self.stride_raw_data['RDTime(ms)'][self.rdata_ipeaks[i]] for i in range(len(self.rdata_ipeaks)-1)]
        self.timer = round((sum(rtimer)/len(rtimer))/1000, 2)
        ltimel = [self.stride_raw_data['RITime(ms)'][self.ldata_ipeaks[i+1]] - self.stride_raw_data['RITime(ms)'][self.ldata_ipeaks[i]] for i in range(len(self.ldata_ipeaks)-1)]
        self.timel = round((sum(ltimel)/len(ltimel))/1000, 2)

    def set_distance (self, size):
        ldistance = []
        rdistance = []
        if self.rdata_ipeaks[0] > self.nrdata_ipeaks[0]:
            for i in range(min(len(self.rdata_ipeaks), len(self.nrdata_ipeaks))):
                A = self._get_real_angle(A=self.nrdata_peaks[i])
                B = self._get_real_angle(A=self.rdata_peaks[i])
                C = self._get_real_angle(A=A, B=B)
                rdistance.append(self._get_segment_distance(A=A, C=C, a=size))
        else:
            for i in range(1, min(len(self.rdata_ipeaks), len(self.nrdata_ipeaks))):
                A = self._get_real_angle(A=self.nrdata_peaks[i])
                B = self._get_real_angle(A=self.rdata_peaks[i])
                C = self._get_real_angle(A=A, B=B)
                rdistance.append(self._get_segment_distance(A=A, C=C, a=size))
        if self.ldata_ipeaks[0] > self.nldata_ipeaks[0]:
            for i in range(min(len(self.ldata_ipeaks), len(self.nldata_ipeaks))):
                A = self._get_real_angle(A=self.nldata_peaks[i])
                B = self._get_real_angle(A=self.ldata_peaks[i])
                C = self._get_real_angle(A=A, B=B)
                ldistance.append(self._get_segment_distance(A=A, C=C, a=size))
        else:
            for i in range(1, min(len(self.ldata_ipeaks), len(self.nldata_ipeaks))):
                A = self._get_real_angle(A=self.nldata_peaks[i])
                B = self._get_real_angle(A=self.ldata_peaks[i])
                C = self._get_real_angle(A=A, B=B)
                ldistance.append(self._get_segment_distance(A=A, C=C, a=size))
        self.mean_distancel = round(sum(ldistance)/len(ldistance)*1.85, 2)
        self.mean_distancer = round(sum(rdistance)/len(rdistance)*1.85, 2)
    
    def _get_real_angle (self, A=0, B=90):
        return 180 - abs(A) - abs(B)
    
    def _get_segment_distance (self, A, C, a):
        return (a * math.sin(math.radians(C))) / math.sin(math.radians(A))
    
    def get_velocity (self):
        lvelocity = round(self.mean_distancel/self.timel)
        rvelocity = round(self.mean_distancer/self.timer)
        return round((lvelocity + rvelocity) / 2, 2)