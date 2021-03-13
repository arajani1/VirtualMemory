import numpy as np

class PhysicalMemory:
    
    
    def __init__(self, line1, line2):
        self.PM = np.zeros(524288)
        self.D = [np.zeros(512) for i in range(1024)]
        self.takenFrames = []
        stValues = line1.split(" ")
        
        for i in range(len(stValues)):
            stValues[i] = int(stValues[i])
            
        for i in range(len(stValues)):
            if i % 3 == 0:
                self.PM[2*stValues[i]] = stValues[i+1]
                self.PM[(2*stValues[i])+1] =  stValues[i+2]
                if stValues[i+2] > 0:
                    self.takenFrames.append(stValues[i+2])
                    
                
        
                
        ptValues = line2.split(" ")
        for i in range(len(ptValues)):
            ptValues[i] = int(ptValues[i])
        
        for i in range(len(ptValues)):
            if i % 3 == 0:
                if (self.PM[2*(ptValues[i])+1] < 0):
                    temp = int(abs(self.PM[2*(ptValues[i])+1]))
                    self.D[temp][ptValues[i+1]] = ptValues[i+2]
                else:
                    temp = int((self.PM[int(2*(ptValues[i])+1)]*512) + (ptValues[i+1]))
                    self.PM[int(temp)] = ptValues[i+2]
                
