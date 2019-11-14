import numpy as numpy

class waveform:
    dt = 1
    t0 = 0
    data = np.array([])

    def __init__(self, dt=1, t0=0, data=np.array([])):
        '''create a waveform'''
        self.dt   = dt
        self.t0   = t0
        self.data = data

    def rms(self):
        '''returns the root mean square (RMS) of all values'''
        return np.sqrt(np.mean(self.data**2))

    def mean(self):
        '''returns the mean value of the values'''
        return np.mean(self.data)
    
    def ppm(self):
        '''returns the all values in ppm with the mean value of the values as reference'''
        return (self.data - np.mean(self.data)) / np.mean(self.data) * 1e6

    def std(self):
        '''returns the standard deviation of the values'''
        return np.std(self.data, ddof=1)
    


    
