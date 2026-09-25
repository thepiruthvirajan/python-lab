from scipy.optimize import minimize

def function(v):
    x, y = v
    return (x - 7)**2 + (y - 4)**2

result = minimize(function, x0=[0, 0])

print("best x,y:", result.x)
print("minimum:", result.fun)
print("success:", result.success)