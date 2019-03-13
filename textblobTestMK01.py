# Tests verschiedener NLP Tools
# ! NLTK
# ! Textblob
# TODO commit
# TODO  git push https://github.com/junker-joerg/mk-nlp
# ! git remote add origin https://github.com/junker-joerg/mk-nlp
# - eröffnet und nochmal
# TODO mit https://www.clips.uantwerpen.be/pattern
# TODO mit NLTK
# TODO mit GENSIM weitermachen: https://radimrehurek.com/gensim/tutorial.html
# Todo spacy
# ! für Windows: pip install 
# für Ubuntu / Mint sudo apt-get install build-essential python-dev git 
# WIN: spacy.load('en') geht nicht - dagegen spacy.load('en_core_web_sm') geht...
# also immer nlp = spacy.load('en_core_web_sm') nehmen
# wenn keine Permissions: pip install de_core_news_sm-2.0.0.tar (muss im gleichen Verzeichnis stehen) ==> manuelle installation
# pip install .tar.gz archive from path or URL
# ! pip install /Users/you/en_core_web_sm-2.0.0.tar.gz
# import de_core_news_sm geht

import de_core_news_sm

from textblob_de import TextBlobDE
import pandas as pd

f1 = open("DHB.txt", mode ="r", encoding="UTF8")

text1 = f1.read()
blob2= TextBlobDE(text1)
f1.close()
blob2.sentences
sens = pd.DataFrame(blob2.sentences)
tgs = pd.DataFrame(blob2.tags)
print(sens)

#blob = TextBlobDE(text)

blob2.tags           # [('Der', 'DT'), ('Blob', 'NN'), ('macht', 'VB'),
                    #  ('in', 'IN'), ('seiner', 'PRP$'), ...]

blob2.noun_phrases   # WordList(['Der Blob', 'seiner unbekümmert-naiven Weise',
                    #           'den gewissen Charme', 'hölzerne Regie',
                    #           'konfuse Drehbuch'])


"""
for sentence in blob2.sentences:
    print(sentence.sentiment.polarity)

"""
