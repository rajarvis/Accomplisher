import random
import wikipedia
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import PunktSentenceTokenizer, word_tokenize, sent_tokenize
from nltk.stem import WordNetLemmatizer

print("imported everything")
stop_words = set(stopwords.words("english"))


"""

user_input ==>>  NLP  ==>>  internet  ==>>  NLP  ==>>  ConciseData
user_input = '''creating a project report'''
"""
class UserInput(object):
    def __init__(self,text, expiry_date, context, context_type = ''):
        self.text = text
        self.expiry_date = expiry_date
        self.context = context
        self.context_type = context_type


UI = UserInput('creating a project report', "2018-03-06", 'professional')
##print(UI.text, UI.expiry_date, UI.context, UI.context_type)
words = word_tokenize(UI.text)
filtered_sentence = []



for w in words:
    if w not in stop_words:
        filtered_sentence.append(w)

##print(filtered_sentence)
##print(wikipedia.summary("how to "+UI.text))
print("############################################################")
##print(wikipedia.summary(str(filtered_sentence)))
print(wikipedia.summary(UI.text))
