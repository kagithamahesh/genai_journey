import numpy as np


x= np.array([[1,2,3],[4,5,6]])

std = x.std(axis=0)

mean =x.mean(axis=0)

x_norm = (x-mean)/std

print(x_norm)
# Dot product — used in every linear layer
W = np.random.randn(3, 2)  # weights (3 in, 2 out)
out = x @ W               # matrix multiply → (2, 2)
print(out)
# Shape inspection
# print(x.shape)

# print(x.reshape(3,2))
 
# mean =x.mean(axis=0)

# print(mean)

# std = x.std(axis=0)
# print(std)