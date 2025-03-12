# este autocodificador se especializa en /
# poder quitarle el ruido a las imagnes 

#importar los paquetes.

import tensorflow as tf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random

#cargando set de datos

from tensorflow.keras.datasets import mnist

(X_train, y_train),(X_test, y_test) = mnist.load_data()

#visualizacion

X_test.shape

#seleccionando imagen aleatoria
i = random.randint(1, 60000)
plt.imshow(X_train[i] , cmap = 'gray')

label = y_train[i]
print(label)

#agregando ruido a las imagenes 




