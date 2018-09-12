import torch
import numpy as np

a = torch.ones(5)
print(a)
b = a.numpy()
print(b)

a.add_(1)
print(a)
print(b)

c = np.ones(5)
d = torch.from_numpy(c)
np.add(c, 1, out=c)
print(c)
print(d)

