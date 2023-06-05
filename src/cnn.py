import torch
import torch.nn as nn
import torch.nn.functional as F
import random
import matplotlib.pyplot as plt
import copy
import argparse
import torchvision
from torch.utils.data import DataLoader, Dataset
import torch.optim as optim
import numpy as np

class DataSet(Dataset):
    def __init__(self, data):
        self.json = data.ddh_labels + data.normal_labels
        self.img = data.ddh_imgs + data.normal_imgs
        self.tear_dropR = []
        self.tear_dropL = []
        self.tiR = []
        self.tiL = []
        self.FHR = []
        self.FHL = []
        self.tonnisR1 = []
        self.tonnisR2 = []
        self.tonnisL1 = []
        self.tonnisL2 = []
        self.skeleton = []
        self.load_json_data()
        assert len(self.img) == len(self.json)

    def load_json_data(self):
        test = np.zeros(11)
        print(test)
        for temp_json in self.json:
            for json_data in temp_json.get('shapes'):
                label = json_data.get('label')
                if label == 'TeardropR':
                    self.tear_dropR.append(json_data.get('points')[0])
                    test[1] += 1
                elif label == 'TeardropL':
                    self.tear_dropL.append(json_data.get('points')[0])
                    test[2] += 1
                elif label == 'TiR':
                    self.tiR.append(json_data.get('points')[0])
                    test[3] += 1
                elif label == 'TiL':
                    self.tiL.append(json_data.get('points')[0])
                    test[4] += 1
                elif label == 'FHR':
                    self.FHR.append(json_data.get('points')[0])
                    test[5] += 1
                elif label == 'FHL':
                    self.FHL.append(json_data.get('points')[0])
                    test[6] += 1
                elif label == 'tonnisR1':
                    self.tonnisR1.append(json_data.get('points')[0])
                    test[7] += 1
                elif label == 'tonnisR2':
                    self.tonnisR2.append(json_data.get('points')[0])
                    test[8] += 1
                elif label == 'tonnisL1':
                    self.tonnisL1.append(json_data.get('points')[0])
                    test[9] += 1
                elif label == 'tonnisL2':
                    self.tonnisL2.append(json_data.get('points')[0])
                    test[10] += 1
        length = test[0]
        print(test)
        for num in test[1:]:
            assert num == length


    def __len__(self):
        return len(self.json)

    def __getitem__(self, item):
        image = self.img[item]
        json = self.json[item]
        return image, json


class CNN_NET(nn.Module):
    def __init__(self):
        super(CNN_NET, self).__init__()
        self.conv1 = nn.Sequential(nn.Conv2d(in_channels=1,
                                             out_channels=1,
                                             kernel_size=5,
                                             stride=1,
                                             padding=2),
                                   nn.ReLU(),
                                   nn.AvgPool2d(kernel_size=2))

        self.conv2 = nn.Sequential(nn.Conv2d(in_channels=1,
                                             out_channels=1,
                                             kernel_size=5,
                                             stride=1,
                                             padding=2),
                                   nn.ReLU(),
                                   nn.AvgPool2d(kernel_size=2))

    def forward(self, x):
        x = self.conv1(x)
        x = self.conv2(x)
        return x
