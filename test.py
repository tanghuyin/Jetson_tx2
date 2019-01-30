import torch
import torchvision
from torchvision import datasets, tranforms


data_train = datasets.MNIST(root="./data/", transform=transform, train=True, download=True)

data_test = datasets.MNIST(root="./data/", transform=transform, train=True, download=False)


