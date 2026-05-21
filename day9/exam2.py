import numpy as np


scores = np.array([
    [80,90],
    [70,85],
    [95,88],
])

print(scores.shape)
print(scores[0][1])  

print(scores[:,0]) #col 0, all student

print(scores.mean(axis=1))