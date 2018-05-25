import csv
from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer("english")
data=[]

with open("sentiword.csv") as csv_file:
	reader=csv.reader(csv_file)
	for row in reader:
		data.append(row)
dataset={}

for row in data[1:]:
	words=row[4].split("#")
	if(len(words)==2):
		words=words[0:-1]
	else:
		for word in words:
			if len(word.split(" "))>1:
				words[words.index(word)]=word.split(" ")[1]
		   
		words=words[0:-1]
	#print(words)
	for word in words:
		#if word =="good":
		#	print(word,row[2],row[3])
		word=stemmer.stem(word.lower())
		#print(word)
		if(word not in dataset):
			dataset[word]={'pos_score':row[2],'neg_score':row[3]}
#print(dataset)

import pickle

with open("word_data.txt", "wb") as myFile:
	pickle.dump(dataset, myFile)    