import json
import os
import numpy as np

def fause_json(jsonfilelist, json_path, fause_json_list):
    '''
    筛选因为形状问题无法转化的 json 文件
    '''
    for i in jsonfilelist:
        circle = 0
        point = 0
        f = open(json_path + i, "r")
        jsonfile = json.loads(f.read())
        label_set = set()
        for j in jsonfile['shapes']:
            point_list = j['points']
            label_set.add(j['label'])
            if len(point_list) == 2:
                circle = circle + 1
            if len(point_list) == 1:
                point = point + 1
        if(circle!=3 or point!=8):
            fause_json_list.append(i)
        if(len(label_set)!=11):
            fause_json_list.append(i)
    return fause_json_list

if __name__ == '__main__':
    json_path = "../dataset/normal/labels/"  # 存储 json 文件的路径，用自己的路径
    jsonfilelist = os.listdir(json_path)
    fause_json_list = []
    fause_json_list = fause_json(jsonfilelist, json_path, fause_json_list)
    str = '\n'
    f=open("false.txt","a")
    f.write(str.join(fause_json_list))
    f.write(str)
    f.close()