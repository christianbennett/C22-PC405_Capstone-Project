### 1. Write App (Flask, TensorFlow)

- Codes needed to test are in the `test/` directory.
- Load the `.h5` model in `main.py`

### 2. Setup Google Cloud

- Create new project (Trashifier)
- Enable Cloud Run API and Cloud Build API

### 3. Install and init Google Cloud SDK

- https://cloud.google.com/sdk/docs/install

### 4. Dockerfile, requirements.txt, .dockerignore

- https://cloud.google.com/run/docs/quickstarts/build-and-deploy#containerizing

### 5. Cloud build & deploy

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

Services are deployed at https://trashify-tklllz773q-et.a.run.app
