import numpy as np
import struct
import matplotlib.pyplot as plt
import json

class DataLoader:
    def __init__(self):
        self.bmp_path = 'data/bmp/'
        self.json_path = 'data/json/'

        self.bmp = None
        self.json = None

        self.test_bmp = None
        self.test_json = None
