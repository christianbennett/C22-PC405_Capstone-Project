# Features

## How to Use

1. Open App.
2. Wait till Splash Screen duration is over.
3. Press "Select Image" Button to select an image from the Gallery.
4. Select the desired image from the Gallery.
5. The application will tell you what it classifies the image into.
6. Press "Speak" to speak out the image label.

## Splash Screen

Our app features a Splash Screen in which the duration can be modified. Currently it's at 2.5 seconds.

![Splash Screen](https://github.com/christianbennett/C22-PC405_Capstone-Project/blob/main/Assets/splash.png)

## Inputting image

You can input image to be predicted from your Image Gallery.

![Input Image Screen](https://github.com/christianbennett/C22-PC405_Capstone-Project/blob/main/Assets/image.png)

## Predicting image

The model will predict the inputted image and return a label output on a TextView.

![Prediction Screen](https://github.com/christianbennett/C22-PC405_Capstone-Project/blob/main/Assets/predict.png)

## Speaking image classification labels

We use TextToSpeech so that the app can speak out the label output.

# Adding custom .tflite model

To run, add `model.tflite` file to `Trashifier/app/src/main/ml`, or input via Android Studio with with File -> New -> Other -> Tensorflow Lite Model -> input `model.tflite` path -> Finish

# App Demo

https://github.com/christianbennett/C22-PC405_Capstone-Project/blob/main/Assets/demo.gif
