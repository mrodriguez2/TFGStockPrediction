import csv
import ast
import spacy
import sys

nlp = spacy.load('en_core_web_sm')

bag_of_words = []

with open('datasets/news_dataset.csv') as news_dataset:
	csv_reader = csv.reader(news_dataset, delimiter=';')
	for row in csv_reader:
		for new in ast.literal_eval(row[1]):
			analyzed_string = nlp(new)
			for entity in analyzed_string.ents:
				if entity.label_ in ['NORP', 'PERSON', 'ORG', 'GPE'] and entity.text not in bag_of_words:
					bag_of_words.append(entity.text)

with open("bag_of_words.txt", "w") as bow:
	for word in bag_of_words:
		bow.write("%s\n" % word)