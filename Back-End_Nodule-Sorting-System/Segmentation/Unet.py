import numpy

from keras.models import Model
from tensorflow import Tensor
from keras.optimizers import SGD
from keras.layers import Input, Conv2D, MaxPooling2D,\
                         UpSampling2D, merge, BatchNormalization, SpatialDropout2D
from keras.models import Model
from keras import backend as K
from keras.callbacks import ModelCheckpoint, Callback, TensorBoard
from scipy.ndimage.interpolation import map_coordinates
from scipy.ndimage.filters import gaussian_filter    # 高斯卷积核

MEAN_FRAME_COUNT = 1
CHANNEL_COUNT = 1
SEGMENTER_IMG_SIZE = 320
MODEL_DIR = './model/again/'   # 模型保存路径
BATCH_SIZE = 8
ELASTIC_INDICES = None

# 定义神经网络并训练
# unet模型损失函数
def dice_coef(y_true, y_pred):
    y_true_f = K.flatten(y_true)
    y_pred_f = K.flatten(y_pred)
    intersection = K.sum(y_true_f * y_pred_f)
    return (2. * intersection + 100) / (K.sum(y_true_f) + K.sum(y_pred_f) + 100)


# unet模型损失函数
def dice_coef_np(y_true, y_pred):
    y_true_f = y_true.flatten()
    y_pred_f = y_pred.flatten()
    intersection = numpy.sum(y_true_f * y_pred_f)
    return (2. * intersection + 100) / (numpy.sum(y_true_f) + numpy.sum(y_pred_f) + 100)


# unet模型损失函数
def dice_coef_loss(y_true, y_pred):
    return -dice_coef(y_true, y_pred)


# 实现unet的网络结构，并加载预训练好的权重
def get_unet(learn_rate=0.0001) -> Model:
    inputs = Input((SEGMENTER_IMG_SIZE, SEGMENTER_IMG_SIZE, CHANNEL_COUNT))
    filter_size = 32
    growth_step = 32
    x = BatchNormalization()(inputs)
    conv1 = Conv2D(filter_size, (3, 3), activation='relu', padding='same')(x)
    conv1 = Conv2D(filter_size, (3, 3), activation='relu', padding='same')(conv1)
    pool1 = MaxPooling2D(pool_size=(2, 2))(conv1)

    pool1 = BatchNormalization()(pool1)
    filter_size += growth_step  # 通道filter_size：64
    conv2 = Conv2D(filter_size, (3, 3), activation='relu', padding='same')(pool1)
    conv2 = Conv2D(filter_size, (3, 3), activation='relu', padding='same')(conv2)
    pool2 = MaxPooling2D(pool_size=(2, 2))(conv2)
    pool2 = BatchNormalization()(pool2)

    filter_size += growth_step  # 通道filter_size：128
    conv3 = Conv2D(filter_size, (3, 3), activation='relu', padding='same')(pool2)
    conv3 = Conv2D(filter_size, (3, 3), activation='relu', padding='same')(conv3)
    pool3 = MaxPooling2D(pool_size=(2, 2))(conv3)
    pool3 = BatchNormalization()(pool3)

    filter_size += growth_step  # 通道filter_size：256
    conv4 = Conv2D(filter_size, (3, 3), activation='relu', padding='same')(pool3)
    conv4 = Conv2D(filter_size, (3, 3), activation='relu', padding='same')(conv4)
    pool4 = MaxPooling2D(pool_size=(2, 2))(conv4)
    pool4 = BatchNormalization()(pool4)

    # 通道filter_size：256
    conv5 = Conv2D(filter_size, (3, 3), activation='relu', padding='same')(pool4)
    conv5 = Conv2D(filter_size, (3, 3), activation='relu', padding='same', name="conv5b")(conv5)
    pool5 = MaxPooling2D(pool_size=(2, 2), name="pool5")(conv5)
    pool5 = BatchNormalization()(pool5)

    conv6 = Conv2D(filter_size, (3, 3), activation='relu', padding='same')(pool5)
    conv6 = Conv2D(filter_size, (3, 3), activation='relu', padding='same', name="conv6b")(conv6)

    up6 = merge.concatenate([UpSampling2D(size=(2, 2))(conv6), conv5], axis=3)
    up6 = BatchNormalization()(up6)

    filter_size -= growth_step  # 通道filter_size：128
    conv66 = Conv2D(filter_size, (3, 3), activation='relu', padding='same')(up6)
    conv66 = Conv2D(filter_size, (3, 3), activation='relu', padding='same')(conv66)

    up7 = merge.concatenate([UpSampling2D(size=(2, 2))(conv66), conv4], axis=3)
    up7 = BatchNormalization()(up7)

    filter_size -= growth_step  # 通道filter_size：64
    conv7 = Conv2D(filter_size, (3, 3), activation='relu', padding='same')(up7)
    conv7 = Conv2D(filter_size, (3, 3), activation='relu', padding='same')(conv7)

    up8 = merge.concatenate([UpSampling2D(size=(2, 2))(conv7), conv3], axis=3)
    up8 = BatchNormalization()(up8)
    filter_size -= growth_step  # 通道filter_size：32
    conv8 = Conv2D(filter_size, (3, 3), activation='relu', padding='same')(up8)
    conv8 = Conv2D(filter_size, (3, 3), activation='relu', padding='same')(conv8)

    up9 = merge.concatenate([UpSampling2D(size=(2, 2))(conv8), conv2], axis=3)
    up9 = BatchNormalization()(up9)
    conv9 = Conv2D(filter_size, (3, 3), activation='relu', padding='same')(up9)
    conv9 = Conv2D(filter_size, (3, 3), activation='relu', padding='same')(conv9)

    up10 = UpSampling2D(size=(2, 2))(conv9)
    conv10 = Conv2D(1, (1, 1), activation='sigmoid')(up10)

    model = Model(input=inputs, output=conv10)
    model.compile(optimizer=SGD(lr=learn_rate, momentum=0.9, nesterov=True),
                  loss=dice_coef_loss, metrics=[dice_coef])
    # Adam(lr=1e-5)
    # ETA：Estimated Time of Arrival。Loss: 系统的损失。acc：Accuracy正确率。
    # model.summary()
    return model