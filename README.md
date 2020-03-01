# Example docker container for machine learning
## Toy example to train logistic regression model with scikit-learn on Iris dataset

This is the repo for 2nd individual project of ECE590  Data Analysis At Scale in the Cloud.

## Docker image
Docker image for this project can be found on docker hub https://hub.docker.com/r/xc150/dockerproj.

## Running app with Cloud9
- Open a cloud 9 environment.
- Run command     docker pull xc150/dockerproj to pull the docker image from docker hub.
- Run command     docker run -it xc150/dockerproj bash_ to create a bash enviroment with the docker image.
- In the bash, run     command _python app.py to do the training.
