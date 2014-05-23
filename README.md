iFixit Spam Filter using Machine Learning

Currently predict.py utilizes sklearn's SVM implementation to train a model
based on our collected data. The model is then fed new data to predict as spam
or not spam and the validity of the guesses are checked to find accuracy.

Tools/autoLabeler.py allows you to quickly label iFixit user data for training
and testing accuracy.

Training Data/Labeled Data can be found in the TrainingData directory.

https://www.ifixit.com/api/2.0/doc/Users

Users Endpoint:
endpoint: /users/{userid}
