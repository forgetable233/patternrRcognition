import os
import shutil
import argparse

# 调用labelme库中原有的 labelme_json_to_dataset 为核心
# 批量将文件夹中的json文件转换，并抽取对应图片至各自文件夹
def GetArgs():
    parser = argparse.ArgumentParser(description='将labelme标注后的json文件批量转换为图片')
    parser.add_argument('--input', '-i', default='../dataset/', required=False, help='json文件目录')
    parser.add_argument('--mask', '-m', default='../dataset/', required=False, help='mask图存储目录')
    parser.add_argument('--viz', '-v', default='../dataset/', required=False, help='mask与原图合并viz图存储目录')
    return parser.parse_args()

if __name__ == '__main__':
    args = GetArgs()
    jsonFolder1 = args.input + "DDH/labels/"
    out_mask1 = args.mask + "DDH/mask/"
    out_viz1 = args.viz + "DDH/viz/"
    for root, dirs, filenames in os.walk(jsonFolder1):
        for img_one in filenames:
            # old_name = img_one.split('/')[-1]
            new_name = img_one.replace(" ", "")             #此处可以自行修改变成去除空格or去除逗号等等
            new_name = os.path.join(jsonFolder1, new_name)
            old_name = os.path.join(jsonFolder1, img_one)
            os.rename(old_name, new_name)
    for root, dirs, input_files1 in os.walk(jsonFolder1):
        continue
    for sfn1 in input_files1:                                        # single file name
        print(sfn1)
        if (os.path.splitext(sfn1)[1] == ".json"):                   # 是否为json文件
            # 调用labelme_json_to_dataset执行转换,输出到 temp1 文件夹
            os.system("labelme_json_to_dataset %s -o temp1" % (jsonFolder1 + sfn1))
            # 复制mask图到存储目录
            if args.mask:
                if not os.path.exists(out_mask1):                   # 文件夹是否存在
                    os.makedirs(out_mask1)
                src_mask = "temp1/label.png"
                dst_mask = out_mask1 + os.path.splitext(sfn1)[0] + ".png"
                shutil.copyfile(src_mask, dst_mask)
 
            # 复制viz图到存储目录
            if args.viz:
                if not os.path.exists(out_viz1):           # 文件夹是否存在
                    os.makedirs(out_viz1)
                src_viz = "temp1/label_viz.png"
                dst_viz = out_viz1 + os.path.splitext(sfn1)[0] + ".png"
                shutil.copyfile(src_viz, dst_viz)
                
    jsonFolder2 = args.input + "normal/labels/"
    out_mask2 = args.mask + "normal/mask/"
    out_viz2 = args.viz + "normal/viz/"
    for root, dirs, filenames in os.walk(jsonFolder2):
        for img_one in filenames:
            # old_name = img_one.split('/')[-1]
            new_name = img_one.replace(" ", "")             #此处可以自行修改变成去除空格or去除逗号等等
            new_name = os.path.join(jsonFolder2, new_name)
            old_name = os.path.join(jsonFolder2, img_one)
            os.rename(old_name, new_name)
    for root, dirs, input_files2 in os.walk(jsonFolder2):
        continue
                
    for sfn2 in input_files2:                                        # single file name
        print(sfn2)
        if (os.path.splitext(sfn2)[1] == ".json"):                   # 是否为json文件
            # 调用labelme_json_to_dataset执行转换,输出到 temp2 文件夹
            os.system("labelme_json_to_dataset %s -o temp2" % (jsonFolder2 + sfn2))
            # 复制mask图到存储目录
            if args.mask:
                if not os.path.exists(out_mask2):                   # 文件夹是否存在
                    os.makedirs(out_mask2)
                src_mask = "temp2/label.png"
                dst_mask = out_mask2 + os.path.splitext(sfn2)[0] + ".png"
                shutil.copyfile(src_mask, dst_mask)
 
            # 复制viz图到存储目录
            if args.viz:
                if not os.path.exists(out_viz2):           # 文件夹是否存在
                    os.makedirs(out_viz2)
                src_viz = "temp2/label_viz.png"
                dst_viz = out_viz2 + os.path.splitext(sfn2)[0] + ".png"
                shutil.copyfile(src_viz, dst_viz)
 