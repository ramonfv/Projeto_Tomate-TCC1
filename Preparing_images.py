import os
import random
import shutil
from os import sys
import glob
from setup_dataset import create_separate_dataset


# def resource_path(relative_path):
#     try:
#         base_path = sys._MEIPASS
#     except Exception:
#         base_path = os.path.abspath(".")

#     return os.path.join(base_path, relative_path)

# def load_dataset(data_dir = src_dir ):

   
#     targetx = 224
#     targety = 224
#     batch_size = 16
#     proportion_train = 0.6
#     proportion_validation = 0.2
#     proportion_test = 0.2

#     datagen = ImageDataGenerator(
#                     rescale=1. / 255,
#                     rotation_range=20,
#                     # zoom_range=0.1,
#                     horizontal_flip=True,
#                     width_shift_range = 0.2,
#                     height_shift_range = 0.2,
#                     shear_range = 0.2
#                     # validation_split=testsplit,
#                     # preprocessing_function=preprocess_input
#     )

#     train_generator = datagen.flow_from_directory(
#                     data_dir,
#                     target_size=(targetx, targety),
#                     batch_size=batch_size,
#                     shuffle=True,
#                     class_mode='sparse',
#                     subset="training",
#                     split= proportion_train
#     )

#     valid_generator = datagen.flow_from_directory(
#                     data_dir,
#                     target_size=(targetx, targety),
#                     batch_size=batch_size,
#                     class_mode='sparse',
#                     shuffle=True,
#                     subset="validation",
#                     split= proportion_validation 
#     )

#     test_generator = datagen.flow_from_directory(
#                     data_dir,
#                     target_size=(targetx, targety),
#                     batch_size=batch_size,
#                     shuffle=True,
#                     class_mode='sparse',
#                     subset="test",
#                     split= proportion_test
# )

#     return train_generator, valid_generator, test_generator

# train_generator, valid_generator, test_generator = load_dataset()
# print("\n\n______________CLASS INDICES TO NAME MAPPING_______________")
# print(train_generator.class_indices)
# print("___________________________________________________________\n\n")
