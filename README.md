# Trashifier - C22-PC405

<!-- PROJECT INFORMATION -->
<br />
<p align="center">
  <a href="https://github.com/christianbennett/C22-PC405_Capstone-Project">
    <img src="https://cdn.discordapp.com/attachments/297540129596243969/974302036860489738/TrashifierLogo.png" width='400dp' alt="Logo" >
  </a>

  <h3 align="center">Trashifier</h3>

  <p align="center">
    An application to classify trash easily and efficiently to ease trash reprocessing or recycling. This is a project to fulfill the <a href="https://grow.google/intl/id_id/bangkit/"><strong>Bangkit Academy led by Google, Tokopedia, Gojek, & Traveloka</strong></a> Program.

  </p>
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#machine-learning-documentation">Machine Learning Documentation</a></li>
        <li><a href="#mobile-development-documentation">Mobile Development Documentation</a></li>
        <li><a href="#cloud-computing-documentation">Cloud Computing Documentation</a></li>
      </ul>
    </li>
    <li><a href="#contributors">Contributors</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About the Project

Our project, Trashifier, is a simple application that can sort trash using Image Classification. It can classify a trash image into 9 categories, which are: Alumunium, Carton, Glass, Organic Waste, Other Plastics, Paper and Cardboard, Plastic, Textiles and Wood. We are trying to attempt to solve one of Indonesia’s biggest problems, which is sorting wastes. How can we classify and sort wastes efficiently?

A 2019 report from the World Bank estimated that Indonesia generates about 175,000 tonnes of waste everyday. That is equivalent to about 8.9 million tonnes of plastic waste each year. Such a large amount of unsorted waste would require a lot of resources for sorting and segregation before the trash can be reprocessed or recycled.

From this information, a question comes into mind: How can we help Indonesian citizens sort trash easily? Sometimes it’s hard to distinguish what trash belongs to what type. Our project is one way to solve this problem. We can help the Indonesian people to easily classify and sort trash by using Image Classification.

In the future, the Internet of Things concept could be implemented on this project so that something like a garbage bin can automatically classify trash, but for now we’re just trying to develop a mobile application.

## Machine Learning Documentation

### Importing Libraries

All the libraries needed to run this notebook are imported here.

### Data Preprocessing

The dataset used on this project can be accessed <a href="https://console.cloud.google.com/storage/browser/trashifier-bucket-1/TrashData?walkthrough_id=assistant_generic_index&project=trashifier-350110&pageState=(%22StorageObjectListTable%22:(%22f%22:%22%255B%255D%22))&prefix=&forceOnObjectsSortingFiltering=false">here</a>.
Google Drive and Google Cloud Platform is mounted here to access and upload datas. We also split the dataset into training and validation sets with 80:20 split. The data is then augmented with ImageDataGenerator to reduce overfitting.

References for our dataset:

https://github.com/cardstdani/WasteClassificationNeuralNetwork/tree/main/WasteImagesDataset

https://github.com/garythung/trashnet

https://github.com/AgaMiko/waste-datasets-review

### Creating & Training the Model

Our model will be consisting of Convolutional Neural Network (CNN), Max Pooling, Dropout, Flatten, and Dense Layers. We are using CNN followed by MaxPooling to extract important features from each class of images. We are also using Dropout to reduce overfitting from the dataset. The model is then Flattened and after that Densed into 9 classes with the Softmax activation function.

Our model is compiled with Adam optimizer with 0.001 learning rate, it also uses Categorical Crossentropy as the loss function and accuracy as metric. It is also trained with 30 epochs and uses a ModelCheckpoint callback function to save and load the best model.

### Predicting the Model

Here we can input images to test our own image against the model. Currently our best model has 84.26% training accuracy and 70.17% validation accuracy. Not great, but still decent.

### Saving the Model

Lastly, we save our model in `.h5` format so that it can be used again later on without retraining the model since it takes quite a lot of time (~2 minutes per epoch with 40 epochs). We also convert the saved model into `.tflite` format so that it can be used in Mobile Development.

## Mobile Development Documentation

### Features

#### Splash Screen

Our app features a Splash Screen in which the duration can be modified. Currently it's at 2.5 seconds.

![Splash Screen](https://github.com/christianbennett/C22-PC405_Capstone-Project/blob/main/Assets/splash.png)

#### Inputting image

You can input image to be predicted from your Image Gallery.

![Input Image Screen](https://github.com/christianbennett/C22-PC405_Capstone-Project/blob/main/Assets/image.png)

#### Predicting image

The model will predict the inputted image and return a label output on a TextView.

![Prediction Screen](https://github.com/christianbennett/C22-PC405_Capstone-Project/blob/main/Assets/predict.png)

#### Speaking image classification labels

We use TextToSpeech so that the app can speak out the label output.

#### Adding custom .tflite model

To run, add `model.tflite` file to `Trashifier/app/src/main/ml`, or input via Android Studio with with File -> New -> Other -> Tensorflow Lite Model -> input `model.tflite` path -> Finish

### App Demo

https://github.com/christianbennett/C22-PC405_Capstone-Project/blob/main/Assets/demo.gif

## Cloud Computing Documentation

### Write Flask App

- Codes needed to test are in the `test/` directory.
- Load the `.h5` model in `main.py`

### Setup Google Cloud

- Create new project (Trashifier)
- Enable Cloud Run API and Cloud Build API

### Install and init Google Cloud SDK

- https://cloud.google.com/sdk/docs/install

### Dockerfile, requirements.txt, .dockerignore

- https://cloud.google.com/run/docs/quickstarts/build-and-deploy#containerizing

### Cloud build & deploy

- Build the application and upload it to Google Cloud with this code:

```
gcloud builds submit --tag gcr.io/trashifier-350110/index
```

- Deploy the application with this code:

```
gcloud run deploy --image gcr.io/trashifier-350110/index --platform managed
```

### 6. Testing

- Copy the URL to `test/test.py` to connect with the deployed app.
- Test the code with `test/test.py` with images to test the model.

### 7. Testing (via Postman)

- Copy the URL to Postman
- Choose POST as the method
- Choose Body->form-data
- Find the File dropdown and choose 'File'
- Click 'Choose File' and input your image
- The server will return a `.json` with the prediction number and label

Services are deployed at https://trashify-tklllz773q-et.a.run.app

## Contributors

### C22-PC405

- (ML) M2004F0310 - Christian Bennett Robin - Institut Teknologi Sepuluh Nopember
- (ML) M2283F2437 - Melisa Kartika Sari - Universitas Negeri Semarang
- (ML) M2381G2931 - Ade Ridwan Nugraha - Universitas Jenderal Achmad Yani
- (CC) C2441W3044 - Naufal Hayyu Triwardana - Universitas Islam Negeri Maulana Malik Ibrahim Malang
- (CC) C7004F0162 - Agustin Umul Hasanah - Institut Teknologi Sepuluh Nopember
