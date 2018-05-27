from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.stem.snowball import SnowballStemmer
from nltk.tag import pos_tag
import pickle
stemmer = SnowballStemmer("english")
tokenizer = RegexpTokenizer(r'\w+')
stop_words = set (stopwords.words( 'english' ))

with open("word_data.txt", "rb") as myFile:
    dataset = pickle.load(myFile)

def preprocess(text):
	tagged_sent = pos_tag(text.split())
	print(tagged_sent)
	filtered_sentence=[w for w,pos in tagged_sent if pos =='JJ' or pos=='RB']
	return filtered_sentence
def get_tuple(text):
	pos_count=0
	neg_count=0
	pos_score=0
	neg_score=0
	tokens=tokenizer.tokenize(text)
	filtered_sentence = [w for w in tokens if not w in stop_words]
	
	for index in range(len(filtered_sentence)):
		word=filtered_sentence[index]
		stem=stemmer.stem(word)
		#print(stem)
		if stem in dataset:
			print(stem,dataset[stem])
			scores=dataset[stem]
			pos=float(scores['pos_score'])
			neg=float(scores['neg_score'])
			if 'very' in filtered_sentence[index-1]:
				pos*=2
				neg*=2
			if 'not' in filtered_sentence[index-1]:
				temp=pos
				pos=neg
				neg=temp
			pos_score+=pos
			neg_score+=neg
			pos_count+=1 if pos>neg else 0 
			neg_count+=1 if pos<neg else 0
	ratio=0
	if neg_count==0:
		ratio=5			# assume that a only positive sentence is equallivant to using 5 times more positive than negative words
	else:
		ratio=float(1.0*pos_count/neg_count)
	return(round(pos_score,2),round(neg_score,2),round(ratio,2))