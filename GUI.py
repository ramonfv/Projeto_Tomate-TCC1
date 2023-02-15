from modules.dataset_loader import get_generator

# train_generator = get_generator('train')
# val_generator = get_generator('val')
# test_generator = get_generator('test')

input_shape = get_generator('input_shape')
targetx = input_shape['x']
targety = input_shape['y']

print(targetx)