#keyword extraction
#pip install rake-nltk
# -*- coding: utf-8 -*-
from rake_nltk import Rake
import os

name = []
name = os.listdir('descriptions')
for i in name:
	if os.path.splitext(i)[1] == '.txt':
		print(i) 
#print(name)

num = 0
print(num)
while num < len(name):
	num += 1
	f = open("descriptions/%s.txt" %(num))
	text = ''
	for line in open ("descriptions/""%s"".txt" %(num)):
		text += line.strip()
		#print(text)

	r = Rake()

	r.extract_keywords_from_text(text)
	keyword = r.get_ranked_phrases()
	print(keyword)
	#print(r.get_ranked_phrases_with_scores())

	keywords = ",".join(keyword)
	with open("description_ex/%s_ex.txt" %(num),"w") as f:
			f.write(keywords)