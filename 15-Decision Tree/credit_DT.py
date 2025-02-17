# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 08:35:55 2024

@author:  Lenovo
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
data=pd.read_csv('c:/10-ML/DecisionTree/credit.csv')
data.head()

data.isnull().sum()
data.dropna()
data.columns
data=data.drop(['phone'],axis=1)

#converting into binary
lb=LabelEncoder()
data['checking_balance']=lb.fit_transform(data['checking_balance'])
data['credit_history']=lb.fit_transform(data['credit_history'])
data['purpose']=lb.fit_transform(data['purpose'])
data['savings_balance']=lb.fit_transform(data['savings_balance'])
data['employment_duration']=lb.fit_transform(data['employment_duration'])
data['other_credit']=lb.fit_transform(data['other_credit'])
data['housing']=lb.fit_transform(data['housing'])
data['job']=lb.fit_transform(data['job'])
#inputs=data.drop(['checking_balance','credit_history','purpose','savings_balance','employment_duration'],axis='columns')
#inputs

#important
data['default'].unique()
data['default'].value_counts()
colnames=list(data.columns)

predictors=colnames[:15]
target=colnames[15]


#splitting data into training and trsting data set
from sklearn.model_selection import train_test_split
train,test=train_test_split(data,test_size=0.3)

from sklearn.tree import DecisionTreeClassifier as DT
#help(DT)
model=DT(criterion='entropy')
model.fit(train[predictors],train[target])
preds=model.predict(test[predictors])
preds
pd.crosstab(test[target],preds,rownames=['Actual'],colnames=['prediction'])
np.mean(preds==test[target])

#Now let us check accuracy on training dataset
preds_train=model.predict(train[predictors])
pd.crosstab(train[target],preds_train,rownames=['Actual'],colnames=['prediction'])
np.mean(preds_train==train[target])

#Accuracy of train data is greater than test data then model is overfit
#accuracy of test data is greater than train data then model is underfit










