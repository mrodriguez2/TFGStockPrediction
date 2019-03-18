import sys
import math
import spacy
import numpy as np
import pandas as pd

from sklearn import preprocessing, svm, model_selection
from sklearn.linear_model import LinearRegression

nlp = spacy.load('en_core_web_sm')

def news2array(headline, df):
	global nlp

	array = np.zeros(len(list(df))-1)

	analyzed_string = nlp(headline)

	for entity in analyzed_string.ents:
		if entity.label_ in ['NORP', 'PERSON', 'ORG', 'GPE'] and entity.text in list(df):
			array[list(df).index(entity.text)] += float(10)

	return array


df = pd.read_csv("dataset_1.csv", sep=";", encoding = "utf-8")
df = df.set_index(['Date'])

stoxx50 = pd.read_csv("datasets/STOXX50E.csv", sep=";", encoding ="utf-8", decimal=',')
stoxx50 = stoxx50.set_index(['Date'])

df = df.join(stoxx50)

for index, row in df.iterrows():
	try:
		if math.isnan(row['STOXX50E']):
			df.drop(index, 'index', inplace = True)
	except:
		continue

df = df.apply(pd.to_numeric, downcast = 'float', errors='ignore')

print(df.head())

X = np.array(df.drop(['STOXX50E'], 'columns'))
y = np.array(df['STOXX50E'])

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.2)

clf = svm.SVR()
clf.fit(X_train, y_train)

confidence = clf.score(X_test, y_test)
print(confidence)

prediction_example = clf.predict([news2array("New Zealand's largest gun show canceled days after mass shooting", df)])
print(prediction_example)