from  tensorflow.python.keras.utils import np_utils
from  tensorflow.keras import backend as K
from  tensorflow.keras.optimizers import Adam
from  model import simpleCNNRMCA
from  tensorflow.keras.datasets import fashion_mnist
from tensorflow.keras.preprocessing.image  import ImageDataGenerator
from  tensorflow.keras.models import load_model 

#needed to downgrade numpy to have it running (otherwise numpy array argument error) !

path="/home/franck/tensorflow_rmca/biobois_smartwoodid/scans_avec_trames_rearrange_grey_14"
BATCH_S=5
SIZE_I=(200,800)
NB_EPOCHS=15

print("test")
model=simpleCNNRMCA.simplecnnrmca()
model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=['accuracy'])

datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2)

train_generator= datagen.flow_from_directory(path, target_size=SIZE_I, batch_size=BATCH_S, class_mode="categorical", subset="training")
validation_generator= datagen.flow_from_directory(path, target_size=SIZE_I, batch_size=BATCH_S, class_mode="categorical", subset="validation")



model.fit_generator(    train_generator, validation_data= validation_generator, steps_per_epoch = train_generator.samples // BATCH_S,     validation_steps = validation_generator.samples // BATCH_S, epochs=NB_EPOCHS)


#preprocessing.processing_image_dataset_from_directory(directory=path, labels="inferred")
model.save("rmca_model.h5")
print("done")
