from models import models
from dataset_loader import get_generator
import time
import os
import pandas as pd
from support import load_callbacks
from support import save_training_history, plot_training_summary
import time
from datetime import datetime, timedelta

def resource_path(resource_path):
    current_dir = os.path.abspath(os.getcwd())
    parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
    return os.path.join(parent_dir, resource_path)


def treinaModelo():
  #   # Loading the dataloaders
  train_generator = get_generator('train')
  val_generator = get_generator('val')
  # Loading the model
  model = models()

  # Training the model
  start = time.time()
  train_history = model.fit(
      train_generator,
      epochs= 8,
      steps_per_epoch= len(train_generator),
      validation_data=val_generator,
      validation_steps=len(val_generator),
      callbacks=load_callbacks()
  )
  end = time.time()


  dir_trained_model = resource_path("trained_model")
  model.save(os.path.join(dir_trained_model, 'saved_model'))

  save_training_history(train_history, dir_trained_model)

  plot_training_summary(dir_trained_model)


  # Training Summary
  training_time_elapsed = end - start
 
  print(f"[INFO] Total Time elapsed: {training_time_elapsed} seconds")

if __name__ == "__main__":
  treinaModelo()



