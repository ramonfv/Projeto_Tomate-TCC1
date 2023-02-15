import json
import tensorflow as tf
from tensorflow import keras
# # from dataset_loader import get_generator
# from dataset_loader import get_generator_functions
from keras.models import Model, Sequential
from keras.layers import BatchNormalization, Dense, Flatten, Dropout
from keras.optimizers import Adam
from keras.applications import MobileNetV2


# input_shape = get_generator('input_shape')
# print(input_shape )

def models():

    # input_shape = get_generator_functions()
    # targetx = input_shape['x']
    # targety = input_shape['y']
    targetx = 224
    targety = 224

    # print(targetx)

    initional_learning_rate = 0.00001
    max_learning = 0.0001
    classes = 10
    optimizer = 'adam'
    neural_networks = ['MobileNetV2', 'DenseNet201']


    # Model Selection
    network = MobileNetV2(

        input_shape = (targetx, targety, 3),
        include_top=False,
        pooling = 'max',
        weights='imagenet'
    )

    #creating Sequencial model

    model = Sequential()
    model.add(network)
    model.add(BatchNormalization())
    model.add(Dense(128, activation="relu"))
    model.add(Dropout(0.5))
    model.add(Dense(64, activation='relu'))
    model.add(BatchNormalization())
    model.add(Flatten())
    model.add(Dense(classes, activation='softmax'))
    opt = Adam(learning_rate=initional_learning_rate)

    #Building model

    model.compile(loss='sparce_categorical_crossentropy',
                optimizer=opt,
                metrics=['acc', 'mse'] )

    model.summary()

    return model






        


