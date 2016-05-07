'''
sklearn.preprocessing.PolynomialFeatures

Generate polynomial and interaction features.

Generate a new feature matrix consisting of all polynomial combinations of the features 
with degree less than or equal to the specified degree. 

For example, if an input sample is two dimensional and of the form [a, b], 
the degree-2 polynomial features are [1, a, b, a^2, ab, b^2].
'''

import numpy as np
import matplotlib.pyplot as plt
import pandas as pn

from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline



# ------  Read 1st sheet data from excel file  ------------------------
xls_file = 'E:/1 - Sinusoid_points.xlsx';
xls = pn.ExcelFile(xls_file)

df = xls.parse('Sheet2')
dataSetArray =np.array(df)  #  Convert data frame into array


# -------  Create indexes of train data and test data  ---------------------
# -------  WITHOUT shuffling  ----------------------------------------------
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


print(train_indexes)
print(test_indexes)

# -------  Create X and Y for training  --------------------------------
X_train = dataSetArray[train_indexes, 0]
Y_train = dataSetArray[train_indexes, 1]
X_train = X_train[:, np.newaxis]
# X_train = X_train.reshape(train_size,1)


# -------  Create X and Y for testing  ---------------------------------
X_test = dataSetArray[test_indexes, 0]
Y_test = dataSetArray[test_indexes, 1]
X_test = X_test[:, np.newaxis]


# print('X training : ', X_train)
# print('Y training : ', Y_train)
# print('X testing : ', X_test)
print('Y testing : ', Y_test)

X_test_ = np.linspace(min(X_test), max(X_test), 10)
X_test_ = X_test_[:, np.newaxis]
# print('X_test_ : ', X_test_)


# -------  Plot true line and points  --------------------------------------
# --------------------------------------------------------------------------

plt.plot(dataSetArray[:, 0], dataSetArray[:, 1], label="ground truth")
plt.scatter(X_train, Y_train, label="training points")


# -------  Train polynomials with different degrees  -----------------------
# -------  using PolynomialFeatures
# --------------------------------------------------------------------------
for degree in [1, 2, 3, 4, 20]:
    model = make_pipeline(PolynomialFeatures(degree, include_bias=True), Ridge())
    model.fit(X_train, Y_train)
    test_prediction = model.predict(X_test)
    plt.plot(X_test, test_prediction, label="degree %d" % degree)
    plt.scatter(X_test, test_prediction)
    
#     test_prediction_ = model.predict(X_test_)
#     plt.plot(X_test_, test_prediction_, label="degree_ %d" % degree)
#     plt.scatter(X_test_, test_prediction_)
    
    print('degree = ', degree, '  =>  ', test_prediction)

plt.legend(loc='upper left')
plt.grid()
plt.show()


