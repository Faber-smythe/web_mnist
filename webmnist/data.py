from dataclasses import dataclass
from torch.utils.data import DataLoader
from torchvision.datasets.mnist import MNIST

import torchvision.transforms as T


train_transform = T.Compose([T.RandomRotation(25), T.ToTensor()])
test_transform = T.ToTensor()

@dataclass
class MNISTDataset():
    train = MNIST(
        root="./data", 
        train=True, 
        transform=train_transform,
        download=True
    )   
    test = MNIST(
        root="./data", 
        train=False, 
        transform=test_transform, 
        download=True
    )


@dataclass
class MNISTLoader():
    train = DataLoader(
        MNISTDataset.train,
        batch_size=32,
        shuffle=True,
        num_workers=4,
        pin_memory=True
    )
    test = DataLoader(
        MNISTDataset.test,
        batch_size=32,
        shuffle=False,
        num_workers=4,
        pin_memory=True
    )