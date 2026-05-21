import numpy as np

score_list =[0.9,0.7,0.8,0.6]

scores = np.array([0.9,0.7,0.8,0.6])

print(scores.shape)

print(scores[0])
print(scores[-1])

print(scores[scores>0.75])