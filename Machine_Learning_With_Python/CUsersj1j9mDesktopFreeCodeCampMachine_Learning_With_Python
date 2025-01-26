import tensorflow as tf
from tensorflow import keras

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt

fashion_mnist = keras.datasets.fashion_mnist  # load dataset

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()  # split into tetsing and training

train_images.shape

train_images[0,23,23]  # let's have a look at one pixel

train_labels[:10]  # let's have a look at the first 10 training labels

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', #Defining Class Names
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

plt.figure() #Visualizing an Image
plt.imshow(train_images[1])
plt.colorbar()
plt.grid(False)
plt.show()