# ☁️ Zacks Google Cloud Toolbox 🧰
some handy dandy scripts for doing things on google cloud 

## Credential FYI
I run most of my code in either Google Cloud Workbench or Cloud Functions so I assume [default credentials](https://cloud.google.com/docs/authentication/application-default-credentials).

## Contents
- [gcs_utils.py](gcs_utils.py) - Simpler uploading and downloading of files from Google Cloud Stroage.
- [tflite_IOD_predictor.py](tflite_IOD_predictor.py) - Wrapper for running a local .tflite image object detector model in python.
- [time_and_log.py](time_and_log.py) - Simple decorator that useful in cloud function code to log and time long running functions.
