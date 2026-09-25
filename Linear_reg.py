import numpy as np

X = np.array([1, 2, 3, 4, 5])
y = np.array([35, 43, 52, 61, 70])

w = 1
b = 0

for epoch in range(100000):

    y_pred = w * X + b

    loss = np.mean((y_pred - y) ** 2)

    dw = np.mean(2 * (y_pred - y) * X)
    db = np.mean(2 * (y_pred - y))

    w = w - 0.01 * dw
    b = b - 0.01 * db

print("Weight:", w)
print("Bias:", b)
