import torch
import numpy as np

np_data = np.arange(6).reshape([2, 3])
torch_data = torch.from_numpy(np_data)
tensor2array = torch_data.numpy()
print(
    "\nnumpy", np_data,
    "\ntorch", torch_data,
    "\ntensor2array", tensor2array
)

# abs
data = [[-3, -1], [5, -9]]
tensor = torch.FloatTensor(data)
print("\nabs"
      "\nnumpy:", np.abs(data),
      "\ntorch:", torch.abs(tensor)
      )

print(
    "\nnumpy:", np.matmul(data, data),
    "\ntorch:", torch.mm(tensor, tensor)
)
