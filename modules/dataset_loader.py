import os
import random
import shutil
from os import sys 
from keras.preprocessing.image import ImageDataGenerator
# from create_dataset import create_separate_dataset

import create_dataset

# train = create_dataset.create_separate_dataset('train')
# print(train)
def load_dataset():
    
    targetx = 224
    targety = 224
    batch_size = 16
    input_shape = {'x': targetx, 'y': targety}

    datagen = ImageDataGenerator(
                                rescale=1. / 255,
                                rotation_range=20,
                                horizontal_flip=True,
                                width_shift_range = 0.2,
                                height_shift_range = 0.2,
                                shear_range = 0.2)
    
    generator_functions = {
        'train': datagen.flow_from_directory(
                                            directory = create_dataset.create_separate_dataset('train'),
                                            target_size=(targetx, targety),
                                            batch_size=batch_size,
                                            shuffle=True,
                                            class_mode='sparse'),
        'val': datagen.flow_from_directory(
                                            directory = create_dataset.create_separate_dataset('val'),
                                            target_size=(targetx, targety),
                                            batch_size=batch_size,
                                            class_mode='sparse',
                                            shuffle=True),
        'test': datagen.flow_from_directory(
                                            directory = create_dataset.create_separate_dataset('test'),
                                            target_size=(targetx, targety),
                                            batch_size=batch_size,
                                            shuffle=True,
                                            class_mode='sparse'),
        'input_shape':  input_shape                                  

    }

    return generator_functions

def get_generator_functions():
    return load_dataset()

def get_generator(dataset_type):
    generator_functions = get_generator_functions()
    try:
        generator = generator_functions[dataset_type]
    except KeyError:
        raise ValueError(f"Invalid dataset type: {dataset_type}. Must be 'train', 'val' or 'test'")
    return  generator

