from torch.optim import AdamW
from torch.utils.data import DataLoader

import torch
import torch.nn as nn

from tqdm import tqdm

from webmnist.data import MNISTDataset, MNISTLoader
from webmnist.model import LeNet5

def train(path: str, epochs: int) ->  None:
    dataset = MNISTDataset()
    loader = MNISTLoader()

    model = LeNet5(n_classes=10)
    # model = LeNet5(n_classes=10).cuda()
    criterion = nn.CrossEntropyLoss()
    # criterion = nn.CrossEntropyLoss().cuda()

    optimizer = AdamW(model.parameters(), lr=1e-3)

    for epoch in range(epochs):
        model.train()
        total_loss, total_acc = 0, 0

        progress_bar = tqdm(loader.train, desc="TRAINING")
        for img, label in progress_bar:
            # img, label = img.cuda(), label.cuda()
            optimizer.zero_grad()

            preds = model(img)
            acc = (torch.argmax(torch.softmax(preds, dim=1), 
                dim=1) == label).sum()
            loss = criterion(preds, label)
            
            loss.backward()
            optimizer.step()

            total_loss += loss.item() / len(loader.train)
            total_acc += acc.item() / len(dataset.train)

            progress_bar.set_postfix(
                loss=f"{total_loss:.2e}",
                acc=f"{total_acc*100:.2f}%"
            )

        model.eval()
        total_loss, total_acc = 0, 0

        progress_bar = tqdm(loader.test, desc="TESTING")
        for img, label in progress_bar:

            preds = model(img)
            acc = (torch.argmax(torch.softmax(preds, dim=1), 
                dim=1) == label).sum()
            loss = criterion(preds, label)

            total_loss += loss.item() / len(loader.test)
            total_acc += acc.item() / len(dataset.test)

            progress_bar.set_postfix(
                loss=f"{total_loss:.2e}",
                acc=f"{total_acc*100:.2f}%"
            )
    torch.save(mode.state_dict(), path)
    
