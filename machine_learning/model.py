from database.connection import client
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

db = client.heart_disease_api.heart_condition.find({},
   { '_id': 0, "id": 0, "name":0 })

heart_data = pd.DataFrame(list(db))


X = heart_data.drop(columns='target', axis=1)
Y = heart_data['target'].astype('bool')

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)

model = LogisticRegression()

model = model.fit(X_train, Y_train)

import pickle

with open('.\models\heart_disease_prediction.pickle', 'wb') as f:
    pickle.dump(model, f)

