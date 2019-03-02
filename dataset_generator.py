import csv
import ast
import sys
import spacy
import pandas as pd
import numpy

max_positions = 10

nlp = spacy.load('en_core_web_sm')

bow = open("bag_of_words.txt", 'r')
columns = bow.read().splitlines() 
bow.close()

index = pd.date_range(start='24/2/2014', end='30/12/2018')

df = pd.DataFrame(index=index, columns=columns)
df = df.fillna(0)

with open('datasets/news_dataset.csv') as news_dataset:
	csv_reader = csv.reader(news_dataset, delimiter=';')
	for row in csv_reader:
		position = 1
		to_add = []
		for new in ast.literal_eval(row[1]):
			analyzed_string = nlp(new)
			for entity in analyzed_string.ents:
				if entity.label_ in ['NORP', 'PERSON', 'ORG', 'GPE'] and entity.text in columns:
					to_add.append((entity.text, max_positions/position))
			position += 1
		for toadd in to_add:
			df.at[pd.Timestamp(row[0]), toadd[0]] = df.at[pd.Timestamp(row[0]), toadd[0]] + toadd[1]

df.to_csv("dataset_1.csv", sep=';', encoding='utf-8') 
