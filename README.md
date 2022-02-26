# mlops-pipeline

Tutorial for deploying a Flask machine learning API to GCP.

When a new version is pushed, CI will build an image and push it to a container registry on GCP.

A container will serve this image as a cloud run function.