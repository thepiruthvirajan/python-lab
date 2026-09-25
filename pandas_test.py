import pandas as pd

df = pd.DataFrame({
    "robot": ["R1", "R2", "R3", "R4", "R5"],
    "speed": [1.2, 2.5, 0.8, 3.1, 1.7],
    "battery": [80, 65, 92, 40, 55],
    "temperature": [35, 41, 33, 48, 39],
    "status": ["moving", "moving", "stopped", "moving", "stopped"]
})



print(df[df["speed"] > 2])