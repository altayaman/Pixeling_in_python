'''  
Uses numpy.polyfit
fits formula:  p(x) = p[0] * x**deg + ... + p[deg]

'''

import numpy as np
import pandas as pn
import scipy.interpolate as i 
from numpy import shape
import matplotlib.pyplot as plt

# ------  Read 1st sheet data from excel file  ------------------------
xls_file = 'E:/1 - Sinusoid_points.xlsx';
xls = pn.ExcelFile(xls_file)

df = xls.parse('Sheet2')
dataSetArray =np.array(df)  #  Convert data frame into array

#  print('Excel file sheets: ', xls.sheet_names)
#  print(df['Order'][:5])


# -------  Create indexes of train data and test data  ---------------------
# -------  WITHOUT shuffling
# --------------------------------------------------------------------------
dataSetSize = len(dataSetArray)
train_size = int(dataSetSize * 0.6)

train_indexes = list(range(train_size))
test_indexes = list(range(int(dataSetSize * 0.6), dataSetSize))


# -------  Create indexes of train data and test data  ---------------------
# -------  WITH shuffling
# --------------------------------------------------------------------------
# train_indexes = list(range(dataSetSize))
# rng = np.random.RandomState(0)
# rng.shuffle(train_indexes)
# train_indexes = np.sort(train_indexes[:train_size])


print('Train indexes: ', train_indexes)
print('Test indexes: ', test_indexes)


# -------  Create X and Y for training  ------------------------------------
# --------------------------------------------------------------------------
X_train = dataSetArray[train_indexes, 0]
Y_train = dataSetArray[train_indexes, 1]
# print('X training: ', X_train)
# print('Y training: ', Y_train)


# -------  Create X and Y for testing  -------------------------------------
# --------------------------------------------------------------------------
X_test = dataSetArray[test_indexes, 0]
Y_test = dataSetArray[test_indexes, 1]
# print('X testing: ', X_test)
print('Y testing: ', Y_test)


# -------  Plot true line and points  --------------------------------------
# --------------------------------------------------------------------------

plt.plot(dataSetArray[:, 0], dataSetArray[:, 1], label="ground truth")
plt.scatter(X_train, Y_train, label="training points")


X_test_ = np.linspace(min(X_test), max(X_test), 10)


# -------  Train polynomials with different degrees  -----------------------
# -------  using numpy.polyfit
# --------------------------------------------------------------------------

for degree in [1, 2, 3, 4, 5]:
    poly_coeffs = np.polyfit(X_train, Y_train, degree)
    prediction = np.poly1d(poly_coeffs)
    test_prediction = prediction(X_test)
    plt.plot(X_test, test_prediction, label="degree  %d" % degree)
#     plt.scatter(X_test, test_prediction)
    
#     test_prediction_ = prediction(dataSetArray[:, 0])
#     plt.plot(dataSetArray[:, 0], test_prediction_, label="X_test_  %d" % degree)
#     plt.scatter(X_test_, test_prediction_)
    
    print('degree = ', degree, '  =>  ', test_prediction)


plt.legend(loc='lower left')
plt.show()