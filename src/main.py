import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader

from data_loader import LoadData
from cnn import CNN_NET, DataSet
import numpy as np
import argparse


def get_args():
    parser = argparse.ArgumentParser(description='cnn train params')
    parser.add_argument('--batch_size', type=int, default=32)
    parser.add_argument('--learning_rate', type=float, default=0.001)
    parser.add_argument('--num_epochs', type=int, default=10)
    return parser.parse_args()


def train_cnn(input_data):
    args = get_args()
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    train_data = DataSet(input_data)
    print('the size of the input data is ' + str(len(train_data)))
    data_loader = DataLoader(train_data, batch_size=args.batch_size, shuffle=True)
    print('finish data loader')
    cnn = CNN_NET()

    model = cnn.to(device)
    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=args.learning_rate)

    total_steps = len(data_loader)
    # for epoch in range(args.num_epochs):
    #     for i, (image, labels) in enumerate(data_loader):
    #         image = image.to(device)
    #         label = image.to(device)
    #
    #         output = model(image)
    #         loss = criterion(output, label)
    #         optimizer.zero_grad()
    #         loss.backward()
    #         optimizer.step()
    #
    #         if (i + 1) % 100 == 0:
    #             print(f"Epoch [{epoch + 1}/{args.num_epochs}], Step [{i + 1}/{total_steps}], Loss: {loss.item():.4f}")


if __name__ == '__main__':
    print('hello world')
    data = LoadData()
    data.load_data()
    train_cnn(input_data=data)
