#pip install babelpy
import os

#command1 = 'babelpy -key 1d39bf76-8e13-4731-a191-fc3b43f5d9f2 -tf descriptions/2.txt -am -ex Babelfymap/test3'
#os.system(command1)


name = os.listdir('descriptions')
print(name)

i = 0
num = len(name)
while i < num:
	i +=1
	number1 = i
	number2 = i
	os.system("babelpy -key 1d39bf76-8e13-4731-a191-fc3b43f5d9f2 -tf descriptions/""%s"".txt -am -ex Babelfymap/test""%s" %(number1,number2))

# i = 0
# num = len(name)
# while i < 1:
	# i +=1
	# number1 = i
	# number2 = i
	# os.system("babelpy -key 1d39bf76-8e13-4731-a191-fc3b43f5d9f2 -tf description_ex/""%s""_ex.txt -am -ex Babelfymap_ex/ex_test""%s" %(number1,number2))