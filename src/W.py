import numpy as np
import pandas as pn
import matplotlib.pyplot as plt
from math import sqrt
from PIL import Image 
from PIL import PngImagePlugin
from dotmap import DotMap
import math
from scipy.stats.stats import pearsonr  


x = np.linspace(0, 3, 4)

print(pn.DataFrame(x, np.sin(x)))
plt.plot(x, x**x)
plt.show()

def average(x):
    assert len(x) > 0
    return float(sum(x)) / len(x)

def pearson_def(x, y):
    assert len(x) == len(y)
    n = len(x)
    assert n > 0
    avg_x = average(x)
    avg_y = average(y)
    diffprod = 0
    xdiff2 = 0
    ydiff2 = 0
    for idx in range(n):
        xdiff = x[idx] - avg_x
        ydiff = y[idx] - avg_y
        diffprod += xdiff * ydiff
        xdiff2 += xdiff * xdiff
        ydiff2 += ydiff * ydiff

    return diffprod / math.sqrt(xdiff2 * ydiff2)

print(pearson_def([1,2,3], [1,5,7]))
print(pearsonr([1,2,3], [1,5,7]))
            