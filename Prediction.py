
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import f1_score, precision_score, accuracy_score, recall_score,confusion_matrix
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier

def predict(labels, data):

    df = pd.read_csv("dataset.csv")
    y_train = df['Disorder']
    del df['Disorder']
    #from FeatureSelection import featureselection
    l=labels
    X = df[l]
    y = y_train

    
    clf = SVC()
    clf = MLPClassifier()
    clf.fit(X, y)

    predicted = clf.predict([data])

    print(predicted[0])
    return predicted[0]

    

if __name__ == '__main__':
    predict()

