import pandas as pd
import numpy as np
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import RandomForestClassifier

import matplotlib.pyplot as plt

class featureselection:
    def calc():
        df = pd.read_csv("dataset.csv")
        
        y = df["Disorder"]  
        del df["Disorder"]
        X=df
        data_top = df.columns
        print(data_top)

        model = RandomForestClassifier()
        model.fit(X,y)
        print(model.feature_importances_) #use inbuilt class feature_importances of tree based classifiers
        #plot graph of feature importances for better visualization
        feat_importances = pd.Series(model.feature_importances_, index=X.columns)
        print(feat_importances)
        feat_importances.nlargest(9).plot(kind='barh')
        d=dict(feat_importances.nlargest(9))
        l=[]
        for ll in d:
            #print(ll)
            l.append(ll)

        return l



if __name__=="__main__":
    print(featureselection.calc())
