# -*- coding:utf-8 -*-
from nltk.corpus import wordnet as wn

print (wn.synsets('number'))
print (wn.morphy('mathematical equations', wn.NOUN))
print (wn.morphy('mathematical equations'))


finalwords = ['dog', 'big cat', 'polynomial rings' ]
for i in range(3):
	result = wn.morphy(finalwords[i], wn.NOUN)
	print(result)
	if result != None:
		print(wn.synsets(finalwords[i]))

#car = wn.synset('car.n.01')
# car = wn.synset('mathematical_equations.n.01')
# print ("HYPERNYMS")
# print (car.hypernyms())
# print ("HYPONYMS")
# print (car.hyponyms())

synonyms = []
antonyms = []

for syn in wn.synsets("good"):
    for l in syn.lemmas():
        synonyms.append(l.name())
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())

print(set(synonyms))
print(set(antonyms))
print (syn.lemmas())



# w1 = wn.synset('ship.n.01')
# w2 = wn.synset('cat.n.01')
# print(w1.wup_similarity(w2))

