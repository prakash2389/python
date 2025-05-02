
import numpy as np

class statistics:
    def __init__(self, data):
        self.data = data
    
    # def add(self, x):
    #     self.data.append(x)
    
    def mean(self):
        return np.mean(self.data)
    
    def max(self):
        return np.max(self.data)


tool = statistics([2,4,3,7,9,22])
print(tool.mean())
print(tool.max())
