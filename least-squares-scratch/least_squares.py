import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (12.0, 9.0)

# Read and plot data
data = pd.read_csv('data.csv')
X = data.iloc[:, 0]
Y = data.iloc[:, 1]
#plt.show()

# Building the model
X_mean = np.mean(X)
Y_mean = np.mean(Y)

print(X_mean)
print(Y_mean)

num = 0
den = 0

for i in range(len(X)):
    num += (X[i] - X_mean) * (Y[i] - Y_mean)
    den += (X[i] - X_mean)**2

m = num / den
c = Y_mean - m * X_mean

print(m, c)

# Making predicitons
Y_pred = m * X + c

plt.scatter(X, Y)
plt.plot([min(X), max(X)], [min(Y_pred), max(Y_pred)], color='red')
plt.show()
