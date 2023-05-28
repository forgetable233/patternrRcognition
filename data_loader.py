import numpy as np
import struct
import matplotlib.pyplot as plt
import json
import os
import cv2


class DataLoader:
    def __init__(self):
        self.ddH_imgs = []
        self.ddh_labels = []

        self.normal_imgs = []
        self.normal_labels = []

        self.test_bmp = []
        self.test_json = []
        
    def load_data(self):
        print('begin to load data\n')
        current_address = os.path.dirname(os.path.abspath(__file__))
        ddh_images = os.path.join(current_address, 'dataset/DDH/images')
        ddh_labels = os.path.join(current_address, 'dataset/DDH/labels')
        normal_images = os.path.join(current_address, 'dataset/normal/images')
        normal_labels = os.path.join(current_address, 'dataset/normal/labels')
        for root, dirs, files in os.walk(ddh_images):
            for file in files:
                img = cv2.imread(os.path.join(ddh_images, file))
                self.ddH_imgs.append(img)

        for root, dirs, files in os.walk(normal_images):
            for file in files:
                img = cv2.imread(os.path.join(normal_images, file))
                self.normal_imgs.append(img)

        for root, dirs, files in os.walk(ddh_labels):
            for file in files:
                with open(os.path.join(ddh_labels, file)) as f:
                    data = json.load(f)
                    self.ddh_labels.append(data)

        for root, dirs, files in os.walk(normal_labels):
            for file in files:
                with open(os.path.join(normal_labels, file)) as f:
                    data = json.load(f)
                    self.normal_labels.append(data)

        assert len(self.normal_labels) == len(self.normal_imgs)
        assert len(self.ddh_labels) == len(self.ddH_imgs)

        ddh_len = len(self.ddh_labels)
        normal_len = len(self.normal_imgs)
        print('have successfully loaded ' + str(ddh_len) + ' ddh ')
        print('have successfully loaded ' + str(normal_len) + ' normal ')

