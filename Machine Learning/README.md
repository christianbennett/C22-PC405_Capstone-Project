# Importing Libraries

All the libraries needed to run this notebook are imported here.

# Data Preprocessing

The dataset used on this project can be accessed <a href="https://console.cloud.google.com/storage/browser/trashifier-bucket-1/TrashData?walkthrough_id=assistant_generic_index&project=trashifier-350110&pageState=(%22StorageObjectListTable%22:(%22f%22:%22%255B%255D%22))&prefix=&forceOnObjectsSortingFiltering=false">here</a>.
Google Drive and Google Cloud Platform is mounted here to access and upload datas. We also split the dataset into training and validation sets with 80:20 split. The data is then augmented with ImageDataGenerator to reduce overfitting.

References for our dataset:

https://github.com/cardstdani/WasteClassificationNeuralNetwork/tree/main/WasteImagesDataset

https://github.com/garythung/trashnet

https://github.com/AgaMiko/waste-datasets-review

# Creating & Training the Model

Our model will be consisting of Convolutional Neural Network (CNN), Max Pooling, Dropout, Flatten, and Dense Layers. We are using CNN followed by MaxPooling to extract important features from each class of images. We are also using Dropout to reduce overfitting from the dataset. The model is then Flattened and after that Densed into 9 classes with the Softmax activation function.

Our model is compiled with Adam optimizer with 0.001 learning rate, it also uses Categorical Crossentropy as the loss function and accuracy as metric. It is also trained with 30 epochs and uses a ModelCheckpoint callback function to save and load the best model.

# Predicting the Model

Here we can input images to test our own image against the model. Currently our best model has 84.26% training accuracy and 70.17% validation accuracy. Not great, but still decent.

# Saving the Model

Lastly, we save our model in `.h5` format so that it can be used again later on without retraining the model since it takes quite a lot of time (~2 minutes per epoch with 40 epochs). We also convert the saved model into `.tflite` format so that it can be used in Mobile Development.
