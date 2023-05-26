import numpy as np
import struct
import matplotlib.pyplot as plt
import json
import os
import cv2


class DataLoader:
    def __init__(self):
        self.bmp = []
        self.json = []

        self.test_bmp = []
        self.test_json = []

    def load_data(self):
        print('begin to load data\n')
        current_address = os.path.dirname(os.path.abspath(__file__))
        json_path = '/data/json/'
        bmp_path = '/data/bmp/'
        for roots, dirs, files in os.walk(current_address + json_path):
            for file in files:
                with open(current_address + json_path + file) as json_file:
                    data = json.load(json_file)
                    self.json.append(data)

        for roots, dirs, files in os.walk(current_address + bmp_path):
            for file in files:
                img = cv2.imread(current_address + bmp_path + file)
                self.bmp.append(img)

        assert len(self.json) == len(self.bmp)
        print('have successfully loaded data')
        print('the input data size is ' + str(len(self.json)))
