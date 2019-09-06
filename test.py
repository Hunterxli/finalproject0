import json

def find_Words():
	with open("test1.json", 'r') as f:
		temp = json.loads(f.read())
		#print(temp)
		#print(temp['all_merged_entities'])
		for item in temp['all_merged_entities'][0]:
			print(item['text'])

#find_Words()

number = 1
def open_Files():
	print(number)
	
open_Files()