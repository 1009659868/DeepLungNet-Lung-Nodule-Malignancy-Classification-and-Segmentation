from keras.preprocessing.image import ImageDataGenerator
from keras.optimizers import Adam
from sklearn.model_selection import train_test_split
from keras.preprocessing.image import img_to_array
from keras.utils import to_categorical, plot_model
from keras.models import Model
# from imutils import paths
import matplotlib.pyplot as plt
import numpy as np
import keras
import cv2
import os

# 定义模型
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense, Input, Concatenate


def create_model():
    model = Sequential()
    #############定义多输入
    input1 = Input(shape=(50, 50, 3), name='input1')
    input2 = Input(shape=(50, 50, 3), name='input2')
    input3 = Input(shape=(50, 50, 3), name='input3')

    #############定义多输入
    x1 = Conv2D(32, (3, 3), padding='same')(input1)  # input is height,width,deep
    x1 = Activation('relu')(x1)
    x1 = Conv2D(32, (3, 3), padding='same')(x1)
    x1 = Activation('relu')(x1)
    x1 = MaxPooling2D(pool_size=(2, 2), strides=(2, 2))(x1)
    x1 = Conv2D(48, (3, 3), padding='same')(x1)
    x1 = Activation('relu')(x1)
    x1 = Conv2D(48, (3, 3), padding='same')(x1)
    x1 = Activation('relu')(x1)
    x1 = MaxPooling2D(pool_size=(2, 2), strides=(2, 2))(x1)
    x1 = Conv2D(64, (3, 3), padding='same')(x1)
    x1 = Activation('relu')(x1)
    x1 = Conv2D(64, (3, 3), padding='same')(x1)
    x1 = Activation('relu')(x1)
    x1 = MaxPooling2D(pool_size=(2, 2), strides=(2, 2))(x1)
    # the model so far outputs 3D feature maps (height, width, features)
    # base_model.add(Flatten())  # this converts our 3D feature maps to 1D feature vectors
    x1 = Flatten()(x1)
    x1 = Dense(256)(x1)
    x1 = Activation('relu')(x1)
    x1 = Dropout(0.5)(x1)
    category_predict1 = Dense(100, activation='softmax', name='category_predict1')(x1)
    # Three loss functions#定义三个全连接层

    x2 = Conv2D(32, (3, 3), padding='same')(input2)  # input is height,width,deep
    x2 = Activation('relu')(x2)
    x2 = Conv2D(32, (3, 3), padding='same')(x2)
    x2 = Activation('relu')(x2)
    x2 = MaxPooling2D(pool_size=(2, 2), strides=(2, 2))(x2)
    x2 = Conv2D(48, (3, 3), padding='same')(x2)
    x2 = Activation('relu')(x2)
    x2 = Conv2D(48, (3, 3), padding='same')(x2)
    x2 = Activation('relu')(x2)
    x2 = MaxPooling2D(pool_size=(2, 2), strides=(2, 2))(x2)
    x2 = Conv2D(64, (3, 3), padding='same')(x2)
    x2 = Activation('relu')(x2)
    x2 = Conv2D(64, (3, 3), padding='same')(x2)
    x2 = Activation('relu')(x2)
    x2 = MaxPooling2D(pool_size=(2, 2), strides=(2, 2))(x2)
    # the model so far outputs 3D feature maps (height, width, features)
    # base_model.add(Flatten())  # this converts our 3D feature maps to 1D feature vectors
    x2 = Flatten()(x2)
    x2 = Dense(256)(x2)
    x2 = Activation('relu')(x2)
    x2 = Dropout(0.5)(x2)
    category_predict2 = Dense(100, activation='relu', name='category_predict2')(x2)

    x3 = Conv2D(32, (3, 3), padding='same')(input3)  # input is height,width,deep
    x3 = Activation('relu')(x3)
    x3 = Conv2D(32, (3, 3), padding='same')(x3)
    x3 = Activation('relu')(x3)
    x3 = MaxPooling2D(pool_size=(2, 2), strides=(2, 2))(x3)
    x3 = Conv2D(48, (3, 3), padding='same')(x3)
    x3 = Activation('relu')(x3)
    x3 = Conv2D(48, (3, 3), padding='same')(x3)
    x3 = Activation('relu')(x3)
    x3 = MaxPooling2D(pool_size=(2, 2), strides=(2, 2))(x3)
    x3 = Conv2D(64, (3, 3), padding='same')(x3)
    x3 = Activation('relu')(x3)
    x3 = Conv2D(64, (3, 3), padding='same')(x3)
    x3 = Activation('relu')(x3)
    x3 = MaxPooling2D(pool_size=(2, 2), strides=(2, 2))(x3)
    # the model so far outputs 3D feature maps (height, width, features)
    # base_model.add(Flatten())  # this converts our 3D feature maps to 1D feature vectors
    x3 = Flatten()(x3)
    x3 = Dense(256)(x3)
    x3 = Activation('relu')(x3)
    x3 = Dropout(0.5)(x3)
    category_predict3 = Dense(100, activation='relu', name='category_predict3')(x3)

    # 融合全连接层
    merge = Concatenate()([category_predict1, category_predict2, category_predict3])
    # 定义输出
    output = Dense(2, activation='sigmoid', name='output')(merge)

    model = Model(inputs=[input1, input2, input3], outputs=[output])

    callbacks = [keras.callbacks.TensorBoard(
        log_dir='my_log_dir',
    )]

    model.compile(optimizer=Adam(lr=0.001, decay=0.01),
                  loss='binary_crossentropy',
                  metrics=['accuracy'],
                  )

    return model, callbacks





