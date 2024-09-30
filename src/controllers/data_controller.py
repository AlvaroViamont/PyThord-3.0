import re


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
            'MaxCI':0, 'MinCI':0
        }
        self.bases:tuple[str] = ('Index', 'Time(ms)', 'Sagital', 'Frontal')
        self.data_size:int = 300
    
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
            'TMaxCI':0, 'TMinCI':0,
        }
        
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