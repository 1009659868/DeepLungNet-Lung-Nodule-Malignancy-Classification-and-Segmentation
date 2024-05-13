import matplotlib.pyplot as plt
import numpy as np
import cv2
import os
import keras

from tensorflow.python.keras.preprocessing.image import img_to_array
from tensorflow.python.keras.utils import to_categorical, plot_model

# label_path = r'D:\Develop\my_env\机算计设计大赛\Test\data\train\label.txt'
# data_path  = r'D:\Develop\my_env\机算计设计大赛\Test\data\train'
def show_data(label_path, data_path):
    for Pathimg in os.listdir(os.path.join(data_path, 'x')):
        Path = os.path.join(os.path.join(data_path, 'x'), Pathimg)
        # print(Path)
        print(type(Path),Path)
        image = cv2.imread(Path)
        # 将 BGR 格式转换为 RGB 格式
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # 画出图像
        plt.imshow(image_rgb)
        plt.axis('off')  # 关闭坐标轴
        plt.show()

        # image=img_to_array(image)
    return 0

def load_data(label_path, data_path):
    data_x = []
    labels = []
    f = open(label_path)
    label = f.readlines()
    for Pathimg in os.listdir(os.path.join(data_path, 'x')):
        # print(Pathimg)
        # print(Path)
        Path = os.path.join(os.path.join(data_path, 'x'), Pathimg)

        image = cv2.imread(Path)

        image = img_to_array(image)
        data_x.append(image)

        # 处理label
        index_num = int(Pathimg.split('.')[0])
        # print(labels)#用索隐处理，
        a = label[index_num]
        label_ = int(a[-3:-2])
        label_1 = 1 if label_ > 3 else 0
        labels.append(label_1)
        # print(labels)
    #print(data)
    # guiyihua
    data_x = np.array(data_x, dtype='float') / 255.0
    labels = np.array(labels)
    # 转化标签为张量
    labels = to_categorical(labels)

    # 载入data——y
    data_y = []
    for Pathimg in os.listdir(os.path.join(data_path, 'y')):
        Path = os.path.join(os.path.join(data_path, 'y'), Pathimg)
        # print(Path)
        image = cv2.imread(Path)
        image = img_to_array(image)
        data_y.append(image)
    # guiyihua
    data_y = np.array(data_y, dtype='float') / 255.0

    # 处理Z
    data_z = []
    for Pathimg in os.listdir(os.path.join(data_path, 'z')):
        Path = os.path.join(os.path.join(data_path, 'z'), Pathimg)
        # print(Path)
        image = cv2.imread(Path)
        image = img_to_array(image)
        data_z.append(image)
    # guiyihua
    data_z = np.array(data_y, dtype='float') / 255.0
    return labels, data_x, data_y, data_z
