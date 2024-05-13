import cv2
import numpy as np
import os

def slice_and_save(image_path, save_dir):
    # 读取图像
    image = cv2.imread(image_path)

    # 中心点定位
    x_, y_, z_ = image.shape
    x_ = int(x_ / 2)
    y_ = int(y_ / 2)
    z_ = int(z_ / 2)

    # z方向切片
    z_silc_50 = image[:, :, z_]
    z_silc_50 = cv2.resize(z_silc_50, (50, 50), interpolation=cv2.INTER_LINEAR) * 255
    z_silc_50 = z_silc_50.astype(np.uint8)  # 数据类型转换
    cv2.imwrite(os.path.join(save_dir, 'z.jpg'), z_silc_50)

    # x方向切片
    x_silc_50 = image[x_, :, :]
    x_silc_50 = cv2.resize(x_silc_50, (50, 50), interpolation=cv2.INTER_LINEAR) * 255
    x_silc_50 = x_silc_50.astype(np.uint8)  # 数据类型转换
    cv2.imwrite(os.path.join(save_dir, 'x.jpg'), x_silc_50)

    # y方向切片
    y_silc_50 = image[:, y_, :]
    y_silc_50 = cv2.resize(y_silc_50, (50, 50), interpolation=cv2.INTER_LINEAR) * 255
    y_silc_50 = y_silc_50.astype(np.uint8)  # 数据类型转换
    cv2.imwrite(os.path.join(save_dir, 'y.jpg'), y_silc_50)


def load_and_prepare_input(x_path, y_path, z_path):
    # 读取并处理x、y和z方向的图片
    x_image = cv2.imread(x_path, cv2.IMREAD_GRAYSCALE)
    y_image = cv2.imread(y_path, cv2.IMREAD_GRAYSCALE)
    z_image = cv2.imread(z_path, cv2.IMREAD_GRAYSCALE)

    # 调整图片大小为模型期望的大小
    x_image = cv2.resize(x_image, (50, 50))
    y_image = cv2.resize(y_image, (50, 50))
    z_image = cv2.resize(z_image, (50, 50))

    # 将灰度图转换为彩色图
    x_image = cv2.cvtColor(x_image, cv2.COLOR_GRAY2RGB)
    y_image = cv2.cvtColor(y_image, cv2.COLOR_GRAY2RGB)
    z_image = cv2.cvtColor(z_image, cv2.COLOR_GRAY2RGB)

    # 将图片的 RGB 通道堆叠在一起
    input_data = np.stack([x_image[:, :, 0], y_image[:, :, 1], z_image[:, :, 2]], axis=-1)

    # 将输入数据形状调整为 (1, 50, 50, 3)
    input_data = np.expand_dims(input_data, axis=0)

    return input_data.astype('float32')

def preprocess_image(image_path):
    # 读取图像并调整大小为50x50像素
    img = cv2.imread(image_path)
    if img is None:
        print(f"Error: Unable to read image '{image_path}'")
        return None
    img = cv2.resize(img, (50, 50))
    # 将图像转换为模型所需的数据类型并进行归一化
    img = img.astype(np.float32) / 255.0
    # 在第0维度添加一个维度，以匹配模型的输入形状
    img = np.expand_dims(img, axis=0)
    # print(img.shape)
    return img

def predict_with_model(image_path, model):
    # 预处理图像
    input_data = preprocess_image(image_path)
    # print(input_data.shape)

    # 使用模型进行预测
    prediction = model.predict(input_data)
    return prediction