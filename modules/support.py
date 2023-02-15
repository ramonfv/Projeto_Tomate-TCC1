from keras.callbacks import EarlyStopping, ReduceLROnPlateau
import os
import pandas as pd
import matplotlib.pyplot as plt

def load_callbacks():
  # Early Stopper Callback
  early_stop = EarlyStopping(monitor='val_acc',
                              patience=10,
                              verbose=1,
                              min_delta=1e-4)

  # Learning Rate Scheduler
  reduce_lr = ReduceLROnPlateau(monitor='val_acc', factor=0.1, patience=4, verbose=1, min_delta=1e-4)

  callbacks_list = [early_stop, reduce_lr]
  return callbacks_list

def save_training_history(train_history, path):
    history = train_history.history
    df = pd.DataFrame(history)
    filepath = os.path.join(path, 'trained_model_history.csv')
    if os.path.exists(filepath):
        df.to_csv(filepath)
        print(
            f"[INFO] Training log is overwritten in {os.path.join(path, 'trained_model_history.csv')}")
    else:
        df.to_csv(filepath)
        print(f"[INFO] Training log is written in {os.path.join(path, 'trained_model_history.csv')}")  


def plot_training_summary(path):
    if not os.path.exists(os.path.join(path,  'trained_model_history.csv')):
        print(f"[ERROR] Log file {os.path.join(path,  'trained_model_history.csv')} doesn't exist")
    else:
        df = pd.read_csv(os.path.join(path,  'trained_model_history.csv'))
        if not os.path.exists(os.path.join(path, 'graphs')):
            os.mkdir(os.path.join(path, 'graphs'))

        # Plotting the accuracy
        fig = plt.figure(figsize=(10, 6))
        plt.plot(df['acc'], "g*-", label="Training accuracy")
        plt.plot(df['val_acc'], "r*-", label="Validation accuracy")
        plt.title('Training and Validation Accuracy Graph')
        plt.xlabel('Epoch')
        plt.ylabel('Accuracy')
        plt.grid("both")
        plt.legend()
        plt.savefig(os.path.join(path, 'graphs',
                                 "1.accuracy-comparison.pdf"))

        # Plotting the loss
        fig = plt.figure(figsize=(10, 6))
        plt.plot(df['loss'], "g*-", label="Training Loss")
        plt.plot(df['val_loss'], "r*-", label="Validation Loss")
        plt.title('Training and Validation Loss Graph')
        plt.xlabel('Epoch')
        plt.ylabel('Loss')
        plt.grid("both")
        plt.legend()
        plt.savefig(os.path.join(path, 'graphs',
                                 "2.loss-comparison.pdf"))

        # Plotting the Learning Rate
        fig = plt.figure(figsize=(10, 6))
        plt.plot(df['lr'], "b*-", label="Training Loss")
        plt.title('Training and Validation Loss Graph')
        plt.xlabel('Epoch')
        plt.ylabel('Learning Rate')
        plt.grid("both")
        plt.legend()
        plt.savefig(os.path.join(path,
                                 'graphs',
                                 "3.learning-rate.pdf"))