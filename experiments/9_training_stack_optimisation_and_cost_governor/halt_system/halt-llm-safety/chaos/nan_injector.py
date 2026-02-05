
import torch

# Intentional NaN injection test
x = torch.tensor([1.0, 0.0])
y = x / 0
loss = y.mean()

print("Generated NaN loss:", loss)
