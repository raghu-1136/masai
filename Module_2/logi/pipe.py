import math
from math import e, log

def compute_z(weights, features):
    # TODO: compute Z = w1*x1 + w2*x2 + ... + wD*xD
    result = [a * b for a, b in zip(weights, features)]
    z = 0
    for i in result:
        z = z+i
    return z

def sigmoid(z):
    # TODO: apply the sigmoid formula 1 / (1 + e^(-z))
    sig = 1/(1+e**(-z))
    return sig
    

def predict_class(probability, threshold=0.5):
    # TODO: apply the 0.5 decision rule and return 0 or 1
   if probability > threshold:
       return 1 
   else:
       return 0

def log_loss(y_actual, y_predicted):
    # TODO: apply Loss = -y*log(y_predicted) - (1-y)*log(1-y_predicted)
    Loss = -y_actual*log(y_predicted) - (1-y_actual)*log(1-y_predicted)
    return(round(Loss,3))


def one_vs_rest_predict(class_probabilities):
    # TODO: return the class label with the maximum probability
    res = max(class_probabilities, key=lambda k: class_probabilities[k])
    return res
    

if __name__ == "__main__":
    weights = [10, 5, 7]
    features = [5, 3, 2]
    z = compute_z(weights, features)
    prob = sigmoid(z)
    print(predict_class(prob))
    print(log_loss(1, 0.9))
    print(log_loss(1, 0.1))
    print(one_vs_rest_predict({"A": 0.9, "B": 0.92, "C": 0.7}))
