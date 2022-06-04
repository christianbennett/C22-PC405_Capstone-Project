# Write Flask App

- Codes needed to test are in the `test/` directory.
- Load the `.h5` model in `main.py`

# Setup Google Cloud

- Create new project (Trashifier)
- Enable Cloud Run API and Cloud Build API

# Install and init Google Cloud SDK

- https://cloud.google.com/sdk/docs/install

# Dockerfile, requirements.txt, .dockerignore

- https://cloud.google.com/run/docs/quickstarts/build-and-deploy#containerizing

# Cloud build & deploy

- Build the application and upload it to Google Cloud with this code:

```
gcloud builds submit --tag gcr.io/trashifier-350110/index
```

- Deploy the application with this code:

```
gcloud run deploy --image gcr.io/trashifier-350110/index --platform managed
```

# Testing

- Copy the URL to `test/test.py` to connect with the deployed app.
- Test the code with `test/test.py` with images to test the model.

# Testing (via Postman)

- Copy the URL to Postman
- Choose POST as the method
- Choose Body->form-data
- Find the File dropdown and choose 'File'
- Click 'Choose File' and input your image
- The server will return a `.json` with the prediction number and label

![Postman](https://github.com/christianbennett/C22-PC405_Capstone-Project/blob/main/Cloud%20Computing/postman.png)

Services are deployed at https://trashify-tklllz773q-et.a.run.app
