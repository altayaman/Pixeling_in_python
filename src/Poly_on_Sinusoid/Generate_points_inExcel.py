import numpy as np
import pandas as pn
import matplotlib.pyplot as plt


f = 10.
# w = 2. * np.pi * f
time_interval = 20

writer = pn.ExcelWriter('E:/1 - Sinusoid1.xlsx')

sheet = ''

for i, samples in enumerate((5, 10, 100)):
    t = np.linspace(0, time_interval, samples)
    y = np.sin(t)
    df = pn.DataFrame(t, y)
    sheet = 'Sheet' + str(1 + i)
    print(sheet)
    df.to_excel(writer, sheet)
    
    
    plt.plot(t, y, '.-')
    plt.show()   
writer.save()    