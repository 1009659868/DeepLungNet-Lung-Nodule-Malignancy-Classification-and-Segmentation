# 模型预测的相关功能

from Segmentation.Unet import get_unet
import glob
import cv2
import numpy as np
from scipy import ndimage
from scipy.ndimage.measurements import center_of_mass
from skimage import morphology
import os

CHANNEL_COUNT = 1
UNET_WEIGHTS = 'Segmentation/model/unet.hd5'
THRESHOLD = 2
BATCH_SIZE = 1
CUBE_SIZE = 32  # 预测模型所处理的三维图像大小：32x32x32

class Seg:
    _instance=None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if not self._initialized:
            self.model = None
            self.input = None
            self.mask_path=r'Segmentation\data\results'  # 保存mask的路径
            self.detect_path = r'img/'  #保存预测标记结果
            self.load_data()

    # 在 pre 类中添加一个方法来设置 TensorFlow 图
    def set_session(self, session):
        self.session = session

    def run(self,imgPath):
        # 如果模型和数据尚未加载，则调用 load_data 方法加载
        if self.model is None:
            self.load_data()
        #进行分割预测
        return self.unet_predict(imagepath=imgPath,maskpath=self.mask_path,model=self.model)

    # unet模型的预测代码
    def unet_predict(self,imagepath, maskpath, model):
        # read png and ready for predict
        img = cv2.imread(imagepath, cv2.IMREAD_GRAYSCALE)
        # print("1", type(img))
        img = prepare_image_for_net(img)
        y_pred = model.predict(img, batch_size=BATCH_SIZE)
        y_pred *= 255.
        y_pred = y_pred.reshape((y_pred.shape[1], y_pred.shape[2])).astype(np.uint8)

        # 保存预测结果
        filename = os.path.basename(imagepath)
        filename=filename.replace('_before', '_after')
        prediction_save_path = os.path.join(maskpath, filename)
        # print(prediction_save_path)
        cv2.imwrite(prediction_save_path, y_pred)  # 将分割结果保存

        centers = unet_candidate_dicom(prediction_save_path)  # 获得mask的结节中心坐标
        print('y, x', centers)
        img_ori = cv2.imread(imagepath)  # 读取原始图片
        for i in range(len(centers)):
            box = [centers[i][1] - 5.5, centers[i][0] - 5.5, centers[i][1] + 5.5, centers[i][0] + 5.5]
            img_ori = plot_one_box(img_ori, box)  # 得到标注后的图片
        seg_path = os.path.join(self.detect_path, filename)
        cv2.imwrite(seg_path, img_ori)
        # print(seg_path)
        # print("over")
        return os.path.basename(seg_path)

    def load_data(self):
        # 加载模型，如果模型尚未加载
        if self.model is None:
            model = get_unet()
            model.load_weights(UNET_WEIGHTS)
            self.model = model


def imgShape(path):
    # 读取图像文件
    image = cv2.imread(path)
    print(path)
    print("--------")
    # 调整图像大小
    resized_image = cv2.resize(image, (320, 320))

    # 保存调整后的图像
    cv2.imwrite('data/Test_images/test0.png', resized_image)

    # 获取调整后图像的形状
    resized_height, resized_width, resized_channels = resized_image.shape

    print("调整后图像宽度:", resized_width)
    print("调整后图像高度:", resized_height)
    print("调整后图像通道数:", resized_channels)


# 获取unet预测结果的中心点坐标(x,y)
def unet_candidate_dicom(unet_result_path):
    centers = []
    image_t = cv2.imread(unet_result_path, cv2.IMREAD_GRAYSCALE)
    # Thresholding(阈值化)
    image_t[image_t < THRESHOLD] = 0
    image_t[image_t > 0] = 1
    # dilation（扩张）
    selem = morphology.disk(1)
    image_eroded = morphology.binary_dilation(image_t, footprint=selem)
    label_im, nb_labels = ndimage.label(image_eroded)

    for i in range(1, nb_labels + 1):
        blob_i = np.where(label_im == i, 1, 0)
        mass = center_of_mass(blob_i)
        y_px = int(round(mass[0]))
        x_px = int(round(mass[1]))
        centers.append([y_px, x_px])
    return centers


# 数据输入网络之前先进行预处理
def prepare_image_for_net(img):
    img = img.astype(float)
    img /= 255.
    if len(img.shape) == 3:
        img = img.reshape(img.shape[-3], img.shape[-2], img.shape[-1])
    else:
        img = img.reshape(1, img.shape[-2], img.shape[-1], 1)
    return img




def plot_one_box(img, coord, label=None, line_thickness=None):
    """
    coord: [x_min, y_min, x_max, y_max] format coordinates.
    img: img to plot on.
    label: str. The label name.
    color: int. color index.
    line_thickness: int. rectangle line thickness.矩形线条粗细
    """
    tl = line_thickness or int(round(0.002 * max(img.shape[0:2])))  # line thickness
    color = [0, 0, 255]
    c1, c2 = (int(coord[0]), int(coord[1])), (int(coord[2]), int(coord[3]))  # 中心点，宽高
    # cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)画出矩形
    # img是原图（x，y）是矩阵的左上点坐标（x+w，y+h）是矩阵的右下点坐标
    # （0,255,0）是画线对应的rgb颜色2是所画的线的宽度
    img = cv2.rectangle(img, c1, c2, color, thickness=tl)
    # 在矩形框上显示出类别
    # if label:
    #     tf = max(tl - 1, 1)  # font thickness
    #     t_size = cv2.getTextSize(label, 0, fontScale=float(tl) / 3, thickness=tf)[0]
    #     c2 = c1[0] + t_size[0], c1[1] - t_size[1] - 3
    #     cv2.rectangle(img, c1, c2, color, -1)  # filled
    #     cv2.putText(img, label, (c1[0], c1[1] - 2), 0, float(tl) / 3, [0, 0, 0], thickness=tf, lineType=cv2.LINE_AA)
    return img


# if __name__ == "__main__":
#     seg=Seg()
#     seg.run(r'.\data\Test_images\test0.png')
#     pass
    # test_img_path = r'.\data\Test_images\test0.png'
    # # test_img_path = r'.\data\Test_images'
    # mask_path = r'.\data\results'  # 保存mask的路径
    # detect_path = r'.\data\detect'
    # unet_predict(test_img_path, mask_path)


#     """ 将原图和分割得到的结节坐标结合，框出结节位置 """
#     for files in os.listdir(mask_path):
#         centers = unet_candidate_dicom(os.path.join(mask_path, files))  # 获得mask的结节中心坐标
#         # print('y, x', centers)
#         img_ori = cv2.imread(os.path.join(test_img_path, files))  # 读取原始图片
#         for i in range(len(centers)):
#             box = [centers[i][1] - 5.5, centers[i][0] - 5.5, centers[i][1] + 5.5, centers[i][0] + 5.5]
#             img_ori = plot_one_box(img_ori, box)  # 得到标注后的图片
#         cv2.imwrite(os.path.join(detect_path, files), img_ori)


