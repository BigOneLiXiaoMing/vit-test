import torch

a = torch.randn(8, 3, 224, 224)
b = torch.flatten(a, start_dim=1)
c = torch.nn.Linear(150528, 768)
d = c(b)
print(d.shape)