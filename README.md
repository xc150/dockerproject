# Example docker container for machine learning
## Train logistic regression model with scikit-learn on Iris dataset

This is the repo for 2nd individual project of ECE590  Data Analysis At Scale in the Cloud.

## Docker image
Docker image for this project can be found on docker hub [here](https://hub.docker.com/r/xc150/dockerproj).

## Running app with Cloud9
- Open a cloud 9 environment.
- Run command `docker pull xc150/dockerproj` to pull the docker image from docker hub.
- Run command `docker run -it xc150/dockerproj bash` to create a bash enviroment with the docker image.
- In the bash, run command `python app.py` to do the training.

## Video demo
[Here](https://youtu.be/FzZ90HxVWFY) is a video demo for the project.
