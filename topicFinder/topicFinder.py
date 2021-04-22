

#python code
import spacy
spacy.load('en_core_web_sm')#changed from en to en_core_web_sm because of OS error E941
from spacy.lang.en import English
parser = English()
import random
from gensim import corpora
import pickle
import gensim

def tokenize(text):
    lda_tokens = []
    tokens = parser(text)
    for token in tokens:
        if token.orth_.isspace():
            continue
        elif token.like_url:
            lda_tokens.append('URL')
        elif token.orth_.startswith('@'):
            lda_tokens.append('SCREEN_NAME')
        else:
            lda_tokens.append(token.lower_)
    return lda_tokens


import nltk

nltk.download('wordnet')
from nltk.corpus import wordnet as wn


def get_lemma(word):
    lemma = wn.morphy(word)
    if lemma is None:
        return word
    else:
        return lemma


from nltk.stem.wordnet import WordNetLemmatizer


def get_lemma2(word):
    return WordNetLemmatizer().lemmatize(word)

nltk.download('stopwords')

#add stop words (unable to differentiate topics from) ex.things, bitcoin

def prepare_text_for_lda(text, en_stop):
    tokens = tokenize(text)
    tokens = [token for token in tokens if len(token) > 4]
    tokens = [token for token in tokens if token not in en_stop]
    tokens = [get_lemma(token) for token in tokens]
    return tokens




#path="C:\\PycharmOut\\comments2.csv" used for all coments
#num_words

def top_ten_topics(path,numTopics,numWords,modelFileName, newStopWords):
    stop_words = nltk.corpus.stopwords.words('english')
    stop_words.extend(newStopWords)
    en_stop = set(stop_words)

    text_data = []
    with open(path, encoding="utf8") as f: #uf8 is necessary for the line to read excel csv or else UnicodeDecodeError: 'charmap'
        for line in f:
            #print(line)
            tokens = prepare_text_for_lda(line,en_stop)
#            print(tokens)
            if random.random() > .99:
                #print(tokens)
                text_data.append(tokens)

    dictionary = corpora.Dictionary(text_data)
    corpus = [dictionary.doc2bow(text) for text in text_data]

    pickle.dump(corpus, open('corpus.pkl', 'wb'))
    dictionary.save('dictionary.gensim')

    ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics = numTopics, id2word=dictionary, passes=15)
    ldamodel.save(modelFileName)
    topics = ldamodel.print_topics(num_words=numWords)
    for topic in topics:
        print(topic)

from getWords import labelList

pathBase = "comments"
label=labelList[0]
path = pathBase + label + ".csv"

newStopWordsBitIS = ["things", "bitcoin", "thing", "could", "though", "value", "whether", "would", "probably",
                   "please", "using", "thanks", "likely", "rather", "think","anything","previous","something","presumably","anyway","maybe","might","need","meantime","otherwise"
                   ,"actual","seem","still","underlie","sometimes","enough","instead","never","really","possibility","actually","frequently","especially","since","strongly",
                   "already","first","generally","always"]

#top_ten_topics(path,10,10,label,newStopWordsBit)
newStopWordsBitSC=[]
#iteratre with two indexes with zip(). One list for labels, one list for associated stopwords
for label in labelList: #For each label category in a file (ex.bitcoin), finds topics
    path=pathBase+label+".csv"

    print("FILE:", path)
    top_ten_topics(path,10,10,label,newStopWordsBitIS)
