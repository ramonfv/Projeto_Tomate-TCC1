import os
import random
import shutil
from os import sys
import glob



# def resource_path(relative_path):
#     # try:
#     #     base_path = sys._MEIPASS
#     # except Exception:
#     #     base_path = os.path.abspath(".")

#     # return os.path.abspath(relative_path)
#     return os.path.abspath(os.path.join(os.getcwd(), '..'))

def resource_path(resource_path):
    current_dir = os.path.abspath(os.getcwd())
    parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
    return os.path.join(parent_dir, resource_path)

def create_separate_dataset(directory_name):

    # Set the source directory
    src_dir = resource_path("PlantVillage_Tomate\\")


    # Set the destination directories for training, test, and validation sets
    train_dir = resource_path('train')
    test_dir = resource_path('test')
    val_dir =  resource_path('val')

    # Check if the destination directories already exist
    if os.path.exists(train_dir) and os.path.exists(test_dir) and os.path.exists(val_dir):
        # print("Destination directories already exist:")
        if directory_name == 'train':
            return train_dir 
        elif directory_name == 'test':           
            return  test_dir
        elif directory_name == 'val':  
            return val_dir
            
        raise ValueError("Invalid directory name. Allowed values are 'train', 'test', and 'val'.")
        # print("Train directory:", train_dir)
        # print("Test directory:", test_dir)
        # print("Validation directory:", val_dir)

    else:
        # Set the split ratios for training, test, and validation sets
        train_split = 0.6
        test_split = 0.2
        val_split = 0.2

        # Loop over each folder in the source directory
        for folder in os.listdir(src_dir):
            src_folder_path = os.path.join(src_dir, folder)
            train_folder_path = os.path.join(train_dir, folder)
            test_folder_path = os.path.join(test_dir, folder)
            val_folder_path = os.path.join(val_dir, folder)

            # Create the destination folder for each set if it doesn't exist
            if not os.path.exists(train_folder_path):
                os.makedirs(train_folder_path)
            if not os.path.exists(test_folder_path):
                os.makedirs(test_folder_path)
            if not os.path.exists(val_folder_path):
                os.makedirs(val_folder_path)

            # Get the list of images in the source folder
            images = glob.glob(os.path.join(src_folder_path, '**/*.jpg'), recursive=True)
            num_images = len(images)

            random.shuffle(images)

        # Calculate the number of images to move to each set
            num_train_images = int(train_split * len(images))
            num_test_images = int(test_split * len(images))
            num_val_images = len(images) - num_train_images - num_test_images
            # print(num_train_images, num_test_images, num_val_images)  

            # Split the images into train, test, and validation sets
            train_images = images[:num_train_images]
            test_images = images[num_train_images:num_train_images + num_test_images]
            val_images = images[-num_val_images:]


            for i in range(len(train_images)):
                src = os.path.join(src_folder_path, train_images[i])
                dst = os.path.join(train_folder_path, "train_" + str(i) + ".jpg")
                shutil.copy(src, dst)
                # print(dst)

            for i in range(len(test_images)):
                src = os.path.join(src_folder_path, test_images[i])
                dst = os.path.join(test_folder_path, "test_" + str(i) + ".jpg")
                shutil.copy(src, dst)
                # print(dst)    
            
            for i in range(len(val_images)):
                src = os.path.join(src_folder_path, val_images[i])
                dst = os.path.join(val_folder_path, "val_" + str(i) + ".jpg")
                shutil.copy(src, dst)

    
    if directory_name == 'train':
        return train_dir 
    elif directory_name == 'test':           
        return  test_dir
    elif directory_name == 'val':  
        return val_dir
        
    raise ValueError("Invalid directory name. Allowed values are 'train', 'test', and 'val'.")


# treino = create_separate_dataset('train')

# # print(type(create_separate_dataset()))
# print(treino)

