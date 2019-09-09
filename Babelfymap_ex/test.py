import json
import os
from nltk.corpus import wordnet as wn


words = []
entity = []
dbpedia = []
finalwords = []
finaldbpedia = []
number = 2
files = os.listdir()
jsonfiles = []
for i in files:
	if os.path.splitext(i)[1] == '.json':
		#print(i)
		jsonfiles.append(i)
		
print(len(jsonfiles))