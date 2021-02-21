import scipy.io
from matplotlib import pyplot as plt
from scipy.io import wavfile
import numpy as np
F=250
Fs=500
m=np.arange(1,500)
x=np.cos(2*np.pi*(F/Fs)*m)
w=np.arange(-np.pi,np.pi,0.1*np.pi)
l=len(x)
y=[]
for i in range(0,len(w)):
        s=0
        for n in range(0,l):
                s=s+x[n]*np.exp(-1*1j*w[i]*n);
        y.append(s)
plt.subplot(211)
plt.stem(w,np.abs(y))
plt.subplot(212)
plt.stem(w,np.angle(y))
plt.show()
