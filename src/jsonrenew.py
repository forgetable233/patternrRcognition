import json
import os
import argparse
from copy import deepcopy

def rename_json(json_path):
    '''
    json 文件重命名,这里可根据需求将json文件名编号
    '''
    for _, _, filenames in os.walk(json_path):
        for img in filenames:
            new_name = img.replace(" ", "")                       # 删除空格
            new_name = os.path.join(json_path, new_name)
            old_name = os.path.join(json_path, img)
            os.rename(old_name, new_name)                         # json文件重命名

def fause_json(json_path, fause_json_list, isDDH):
    '''
    筛选有问题的 json 文件
    '''
    jsonfilelist = os.listdir(json_path)
    for i in jsonfilelist:
        circle = 0
        point = 0
        rectangle = 0
        with open(json_path + i, 'r', encoding='utf-8') as f:
            jsonfile = json.loads(f.read())
        label_set = set()
        for j in jsonfile['shapes']:
            point_list = j['points']
            label_set.add(j['label'])
            if len(point_list) == 2 and j['shape_type'] == "circle":
                circle = circle + 1
            if len(point_list) == 1 and (j['shape_type'] == "point" or j['shape_type'] == "polygon"):
                point = point + 1
            if len(point_list) == 2 and j['shape_type'] == "rectangle":
                rectangle = rectangle + 1
        if(isDDH):
            if(circle!=2 or point!=8):
                fause_json_list.append(i)
            if(len(label_set)!=10):
                fause_json_list.append(i)
        else:
            if(circle!=2 or point!=8):
                if(circle!=0 or point!=10):
                    fause_json_list.append(i)
            if(len(label_set)!=11):
                fause_json_list.append(i)
    return fause_json_list

def renew_json(json_path_old, json_path_new):
    '''
    更新 json 文件
    '''
    if not os.path.exists(json_path_new):
        os.makedirs(json_path_new)
    jsonfilelist = os.listdir(json_path_old)
    for i in jsonfilelist:
        with open(json_path_old + i, 'r', encoding='utf-8') as f:
            jsonfile = json.loads(f.read())
        for j in jsonfile['shapes']:
            point_list = j['points']
            if j['shape_type'] == "polygon" and len(point_list) == 1:
                j['shape_type'] = "point"
            if len(point_list) == 2 and j['shape_type'] == "circle":
                j['shape_type'] = "point"
                j['points'].pop(1)
        shapes = deepcopy(jsonfile['shapes'])
        for t in shapes:
            if t['shape_type'] == "rectangle":
                jsonfile['shapes'].remove(t)
        with open(json_path_new + i, 'w', encoding='utf-8') as f:
            json.dump(jsonfile, f)

def remove_json(json_path_new, fause_json_list):
    '''
    删除有误的 json 文件
    '''
    for i in fause_json_list:
        path = json_path_new + i
        os.remove(path)

def json_renew(json_path1, json_path2, json_path1_new, json_path2_new):
    '''
    更正json文件
    '''
    str = '\n'
    rename_json(json_path1)                         # 重命名json文件
    rename_json(json_path2)
    if not os.path.exists("falsejson/"):
        os.makedirs("falsejson/")
    fause_json_list1 = []
    fause_json_list1 = fause_json(json_path1, fause_json_list1, True)
    f=open("falsejson/false_DDH.txt","w")
    f.write(str.join(fause_json_list1))
    f.close()
    renew_json(json_path1, json_path1_new)          # 更改json文件
    remove_json(json_path1_new, fause_json_list1)   # 移除有误的json文件
    
    
    fause_json_list2 = []
    fause_json_list2 = fause_json(json_path2, fause_json_list2, False)
    f=open("falsejson/false_normal.txt","w")
    f.write(str.join(fause_json_list2))
    f.close()
    renew_json(json_path2, json_path2_new)
    remove_json(json_path2_new, fause_json_list2)

def GetArgs():
    parser = argparse.ArgumentParser(description='将labelme标注后的json文件进行更正')
    parser.add_argument('--json_path1', '-j1', default='dataset/DDH/labels/', required=False, help='DDH的labels文件目录')
    parser.add_argument('--json_path2', '-j2', default='dataset/normal/labels/', required=False, help='normal的labels文件目录')
    parser.add_argument('--json_path1_new', '-jn1', default='dataset/DDH/labels_new/', required=False, help='DDH的labels_new文件目录')
    parser.add_argument('--json_path2_new', '-jn2', default='dataset/normal/labels_new/', required=False, help='normal的labels_new文件目录')
    return parser.parse_args()

if __name__ == '__main__':
    args = GetArgs()
    json_renew(args.json_path1, args.json_path2, args.json_path1_new, args.json_path2_new)