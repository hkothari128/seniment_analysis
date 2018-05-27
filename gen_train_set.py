import pickle,csv,pprint
import word_score

attributes=[('pos_score','neg_score','ratio(pos/neg)')]
with open("word_data.txt", "rb") as myFile:
    dataset = pickle.load(myFile)


		

'''texts=[
'I bought it rs522. . I am using it with my honor 6x Bass is good but sound is little low. I have also used it with my lenovo k6 power and samsung ace 1 and the sound and bass was amazing. If smone buy it for honor phn for them (suggestion) sound is little low compare to samsung and lenovo. But most important thing... Sound clarity is very good.',
'Good placements. Don\'t have worry about if you have a decent CGPA. Average package for ECE is about 7 LPA. Most of ECE students from ECE get placed in software companies. Very good placements for CS students with the highest package around 30lpa and average around 10 LPA.',
'Dr. John is a patient, intervening and vastly knowledge person. I can’t thank him enough for all the help that he give me, with he’s help I was able to take my work to a next level. I will definitely recommend him as a tutor.!',
'I have just started from a very basic understanding and Arash quickly adapts the level to meet yours, while at the same time demands your full focus and intensity to learn as much as possible during the lessons. Fantastic so far, would recommend to anyone.',
'not too complicated to set the time ( just tap 10 times then hold down once it starts blinking you can set the hour then repeat step 1 by tapping 10 times again and skipping the set hour and set the minutes ) note: when you have it in the set mode you can move the hour and the minutes forward each time you touch it',
'Nice watch little hard to program but nice',
'Gave it to my son as a girt it became too difficult to read and set, He gave up it is now somewhere in his room a waste of my money.',
'Unique!',
'Don\'t buy. Very cheap and band falls apart.',
'Cheap but I gave it away to some kids .',
'Its an addicting when your on the run or bored'
]
#print(get_tuple(text.lower()))
for text in texts:
	#filtered_text=preprocess(text)
	attributes.append(get_tuple(text))
print(attributes)'''
texts=[]
with open("kmeans_train.csv") as csv_file:
	reader=csv.reader(csv_file)
	next(reader)
	for row in reader:
		texts.append(row[1])
for text in texts:
	print(text,word_score.get_tuple(text))
	#filtered_text=preprocess(text)
	attributes.append(word_score.get_tuple(text))
pprint.pprint(attributes)
import pickle

with open("train_data.txt", "wb") as myFile:
	pickle.dump(attributes, myFile,protocol=2)