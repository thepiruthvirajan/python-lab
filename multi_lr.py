import numpy as np

X = np.array([
    [5, 1],
    [7, 2],
    [9, 2],
    [11, 3],
    [13, 3]
])

y = np.array([
    12,
    17,
    21,
    26,
    30
])

w = np.array([0.0, 0.0])
b = 0.0

lr = 0.01

for epoch in range(100000):
    y_pred = X @ w + b
    error = y_pred - y

    dw = (2/len(X)) * (X.T @ error)
    db = np.mean(2 * error)

    b = b - lr * db
    w = w - lr * dw

print("Weights:", w)
print("Bias:", b)