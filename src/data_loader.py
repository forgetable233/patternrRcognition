import numpy as np
import struct
import matplotlib.pyplot as plt
import json
import os
import cv2
import argparse


def get_args():
    parser = argparse.ArgumentParser(description='load json and bmp image')
    parser.add_argument('--ddh_path', default='dataset/DDH/')
    parser.add_argument('--normal_path', default='dataset/normal')
    parser.add_argument('--json_path', default='labels_new')
    parser.add_argument('--img_path', default='images')
    return parser.parse_args()


class LoadData:
    def __init__(self):
        self.ddh_imgs = []
        self.ddh_labels = []

        self.normal_imgs = []
        self.normal_labels = []

        self.test_bmp = []
        self.test_json = []

    def load_data(self):
        print('begin to load data\n')
        args = get_args()
        label_path = os.path.join(args.ddh_path, args.json_path)
        img_path = os.path.join(args.ddh_path, args.img_path)
        for root, dirs, files in os.walk(label_path):
            for file in files:
                with open(os.path.join(label_path, file)) as f:
                    data = json.load(f)
                    self.ddh_labels.append(data)
                    tar_img = os.path.join(img_path, data.get('imagePath'))
                    img = cv2.imread(tar_img)
                    self.ddh_imgs.append(img)
        normal_path = os.path.join(args.normal_path, args.json_path)

        for root, dirs, files in os.walk(normal_path):
            for file in files:
                with open(os.path.join(normal_path, file)) as f:
                    data = json.load(f)
                    self.normal_labels.append(data)
                    tar_img = os.path.join(normal_path, data.get('imagePath'))
                    img = cv2.imread(tar_img)
                    self.normal_imgs.append(img)
        assert len(self.ddh_imgs) != 0 and len(self.normal_imgs) != 0
        assert len(self.ddh_labels) == len(self.ddh_imgs)
        assert len(self.normal_imgs) == len(self.normal_labels)
        ddh_len = len(self.ddh_labels)
        normal_len = len(self.normal_labels)
        print('have successfully loaded ' + str(ddh_len) + ' ddh ')
        print('have successfully loaded ' + str(normal_len) + ' normal ')
