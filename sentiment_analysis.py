from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import tokenize
import pickle


with open('results.txt','rb') as fp:
    database = pickle.load(fp)

sid = SentimentIntensityAnalyzer()

def analyse(sentences):
#Accepts list of sentences and performs sentiment intensity analysis
    for i in sentences:
        #print(i)
        ss = sid.polarity_scores(i)
        print(ss['neg'])
        for k in sorted(ss):
            #print('{0}: {1},'.format(k, ss[k]), end='\n')
            pass


#print(len(database))
analyse(database[20000:])
