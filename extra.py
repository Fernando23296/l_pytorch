import numpy as np 
import torch
'''
a =[[1,2],[3,4]] 
a = np.array(a)
b = torch.Tensor(a)
print(b)
print(type(b))

c = torch.ones(3,3)
print(c)

ran = torch.randn(3,3)
print(ran)

torch.manual_seed(123)
ran2 = torch.randn(3,3)
print(ran2)

print("*"*20)
ran = torch.randn(3,3)
print(ran)

print(ran2)
'''

na = np.array([[2.0,3.0],[3.0,4.0]])
print(na)
print(type(na))
to = torch.from_numpy(na)
print(to)

to2 = torch.ones(2,2)
to3 = torch.ones(2,2)
print(to2+to3)