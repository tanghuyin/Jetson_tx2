import torch
import torchvision
from torch.autograd import Variable
import torch.utils.data as dataloader
import time


torch.manual_seed(1)

EPOCH = 1
BATCH_SIZE = 50
LR = 0.001

data_train = torchvision.datasets.MNIST(
	root="./data/", 
	transform=torchvision.transforms.ToTensor,
	train=True, 
	download=True)
