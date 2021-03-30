from torch.optim import AdamW
from torch.utils.data import DataLoader
from torchvision.datasets.mnist import MNIST
from typing import NamedTuple
from tqdm import tqdm
#from webmnist.model import LeNet5

import torch
import torch.nn as nn
import torchvision.transforms as T

MIRROR = "https://ossci-datasets.s3.amazonaws.com/mnist"
MNIST.resources = [
    ("/".join([MIRROR, url.split("/")[-1]]), md5)
    for url, md5 in MNIST.resources
]
