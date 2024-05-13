from keras.models import load_model
import cv2
import numpy as np
from IDNS import inputs

class Pre:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if not self._initialized:
            self._initialized = True
            self.model = None
            self.x_input = None
            self.y_input = None
            self.z_input = None
            self.load_data()

    # 在 pre 类中添加一个方法来设置 TensorFlow 图
    def set_session(self, session):
        self.session = session

    def run(self, imgPath):
        # 如果模型和数据尚未加载，则调用 load_data 方法加载
        if self.model is None :
            self.load_data()

        # self.slice_img(Path=imgPath)
        self.x_input = inputs.preprocess_image(imgPath)
        self.y_input = inputs.preprocess_image(imgPath)
        self.z_input = inputs.preprocess_image(imgPath)
        # 使用已加载的模型和数据进行预测
        if self.x_input is not None and self.y_input is not None and self.z_input is not None:

            predictions = self.model.predict([self.x_input, self.y_input, self.z_input])

            # 将预测结果转换为列表
            result = predictions.tolist()
            print(result)
            self.x_input,self.y_input,self.z_input=None,None,None

            return result
        else:
            predictions=None
            return predictions

    def load_data(self):
        # 加载模型，如果模型尚未加载
        if self.model is None:
            model_path = 'IDNS/result/model_45.h5'
            self.model = load_model(model_path)

    def slice_img(self,Path):
        # 输入图像进行切片
        if (Path == '' or Path == None):
            image_path = 'IDNS/inputData/1-1.dcm.jpg'
        else:
            image_path = Path
        # 指定待预测的图像路径和保存切片图像的文件夹路径
        save_dir = 'IDNS/inputData'
        x_path = 'IDNS/inputData/x.jpg'
        y_path = 'IDNS/inputData/y.jpg'
        z_path = 'IDNS/inputData/z.jpg'
        # 将图片切片处理
        inputs.slice_and_save(image_path, save_dir)
        # print('slice over...')
        # 预处理切片图像
        self.x_input = inputs.preprocess_image(x_path)
        self.y_input = inputs.preprocess_image(y_path)
        self.z_input = inputs.preprocess_image(z_path)


# if __name__=='__main__':
#     pre_instance1 = Pre()
#     pre_instance1.run('')




#
# class pre:
#     # 类属性，用于存储已加载的模型和数据
#     model = None
#     x_input = None
#     y_input = None
#     z_input = None
#
#     @classmethod
#     def run(imgPath):
#         x_input, y_input, z_input, model = this.load_data(imgPath)
#         predictions = model.predict([x_input, y_input, z_input])
#         # 输出预测结果
#         # print("Predictions:", predictions)
#         # print("type:",type(predictions))
#         # 返回预测结果
#         reslut = predictions.tolist()
#         return reslut
#
#     @classmethod
#     def load_data(imgPath):
#         # 加载模型
#         model_path = 'IDNS/result/model_44.h5'
#         model = load_model(model_path)
#
#         # 输入图像进行切片
#         # 指定待预测的图像路径和保存切片图像的文件夹路径
#         # image_path = 'inputData/ISIC_0027865_original.jpg'
#         if imgPath == '' or imgPath == None:
#             image_path = 'IDNS/inputData/1-1.dcm.jpg'
#         else:
#             image_path = imgPath
#         # 将图片切片处理
#         save_dir = 'IDNS/inputData'
#         inputs.slice_and_save(image_path, save_dir)
#         print('slice over...')
#         # 构造输入数组
#         x_path = 'IDNS/inputData/x.jpg'
#         y_path = 'IDNS/inputData/y.jpg'
#         z_path = 'IDNS/inputData/z.jpg'
#         # 预处理切片图像
#         x_input = inputs.preprocess_image(x_path)
#         y_input = inputs.preprocess_image(y_path)
#         z_input = inputs.preprocess_image(z_path)
#         return x_input, y_input, z_input, model
#

# if __name__=='__main__':
#     run('')
