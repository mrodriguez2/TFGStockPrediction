import spacy
import sys

nlp = spacy.load('en_core_web_sm')

string = sys.argv[1]

analyzed_string = nlp(string)

for entity in analyzed_string.ents:
	if entity.label_ in ['NORP', 'PERSON', 'ORG', 'GPE']
		print(entity.text, entity.label_)