import numpy as np

X = np.array([1, 2, 3, 4, 5, 6])
y = np.array([0, 0, 0, 1, 1, 1])

w = 0.0
b = 0.0

lr = 0.1

for epoch in range(100000):
    z = w * X + b
    y_pred = 1/ (1 - np.exp(-z))

    loss = -np.mean(y * np.log(y_pred) + (1 - y) * np.log(1 - y_pred))

    dw = np.mean((y_pred - y) * X)
    db = np.mean(y_pred - y)

    w = w - lr*dw
    b = b - lr*db

