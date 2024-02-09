import torch

lz = torch.load('X:\\Doc\\program_this\\model\\yolov8n.pt')

for parameter in lz.parameters():
    print(parameter)