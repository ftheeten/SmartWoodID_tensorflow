from  tensorflow.keras.models import Sequential
from  tensorflow.python.keras.layers.normalization import BatchNormalization
from  tensorflow.python.keras.layers.convolutional import Conv2D
from tensorflow.python.keras.layers.convolutional import MaxPooling2D
from tensorflow.python.keras.layers.core import Activation
from tensorflow.python.keras.layers.core import Flatten
from tensorflow.python.keras.layers.core import Dropout
from tensorflow.python.keras.layers.core import Dense
from tensorflow.python.keras.layers.core import Reshape
from tensorflow.keras import backend as K


def simplecnnrmca():
    model=Sequential()
    model.add(Conv2D(filters=32, kernel_size=(5,5), padding="same",input_shape=(200,800,3), activation="relu"))
    model.add(Conv2D(filters=32, kernel_size=(5,5), padding="same", activation="relu"))
    model.add(MaxPooling2D(pool_size=(2,2)))
    model.add(Dropout(0.2))
    model.add(Conv2D(filters=64, kernel_size=(5,5), padding="same", activation="relu"))
    model.add(Conv2D(filters=64, kernel_size=(5,5), padding="same", activation="relu"))
    model.add(MaxPooling2D(pool_size=(2,2)))
    model.add(Dropout(0.2))
    model.add(Flatten())
    model.add(Dense(120, activation='relu'))
    model.add(Dense(84, activation='relu'))
    #dimensionner en fonction des espèces dans app biologie du bois
    model.add(Dense(14))
    return model        
