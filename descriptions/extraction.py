#pip install rake-nltk
# -*- coding: utf-8 -*-
from rake_nltk import Rake
import os


num = 0
while num < 1:
	num += 1
	f = open("%s.txt" %(num))
	text = ''
	for line in open ("%s.txt" %(num)):
		text += line.strip()
		#print(text)

	r = Rake()

	r.extract_keywords_from_text(text)
	keyword = r.get_ranked_phrases()
	print(keyword)
	#print(r.get_ranked_phrases_with_scores())

	keywords = ",".join(keyword)
	with open("%s_ex.txt" %(num),"w") as f:
			f.write(keywords)