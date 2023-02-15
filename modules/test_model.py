import os
from dataset_loader import get_generator
from keras.models import load_model
import tensorflow as tf



def resource_path(resource_path):
    current_dir = os.path.abspath(os.getcwd())
    parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
    return os.path.join(parent_dir, resource_path)

# def predictionsTest():

test_generator = get_generator('test')
saved_model_path = resource_path("trained_model\\saved_model")
trained_model = tf.saved_model.load(saved_model_path)

model = load_model(saved_model_path)

print(model.summary())

test_evaluate = model.evaluate(test_generator)
print(test_evaluate)



