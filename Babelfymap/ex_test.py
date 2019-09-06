# -*- coding:utf-8 -*-
import json
from nltk.corpus import wordnet as wn


words = []
entity = []
dbpedia = []
finalwords = []
finaldbpedia = []
k = 2
number = 2


def find_Words():
	with open("ex_test%s.json" %(number), 'r') as f:
		temp = json.loads(f.read())
		#print(temp)
		#print(temp['all_merged_entities'])
		
		for item in temp['all_merged_entities'][0]:
			#print(item['text'])
			# words.append(item['text'])
			
			# #print(item['isEntity'])
			# entity.append(item['isEntity'])
			if item['isEntity'] == True:
				dbpedia.append(item['DBpediaURL'])
				words.append(item['text'])
				entity.append(item['isEntity'])
			#dbpedia.append(item['DBpediaURL'])
				#print(item['text'])
			
					
		print(words)
		#print(entity[0])
		print(dbpedia)
		# if entity[0] == False:
			# print("good")
		i = 0
		for i, value in enumerate(entity):
			if value == True:
				print(words[i] + ":" + str(entity[i]))
		for i, value in enumerate(dbpedia):
			if value != '':
				finaldbpedia.append(dbpedia[i])
				finalwords.append(words[i])
				print(words[i] + ":" + str(dbpedia[i]))
		print(finalwords)
		print(finaldbpedia)
		print("\n")
		

#find_Words()


def extraction_Words():
	i = 0
	print(len(finalwords))
	x = len(finalwords)
	for i in range(x):
		result = wn.morphy(finalwords[i], wn.NOUN)
		#result2 = wn.morphy(finalwords[i], wn.VERB)
		print(result)
		if result != None:
			print(wn.synsets(finalwords[i]))
			
			word = wn.synset(finalwords[i] +'.n.01')
			#word = wn.synset(finalwords[i] +'.n.01').lemma_names()
			
	
			print("hypernyms")
			print (word.hypernyms())
			print("synonyms")
			synonyms = []
			for syn in wn.synsets(finalwords[i]):
				for l in syn.lemmas():
					synonyms.append(l.name())
			print(set(synonyms))
			print("\n")
		else:
			print("\n")

#extraction_Words()


while number < 3:
	find_Words()
	extraction_Words()
	number += 1
		






