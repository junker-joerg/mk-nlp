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

from textblob_de import TextBlobDE
import pandas as pd

f1 = open("DHB.txt", mode ="r", encoding="UTF8")

text1 = f1.read()
blob2= TextBlobDE(text1)
f1.close()
blob2.sentences
sens = pd.DataFrame(blob2.sentences)
tgs = pd.DataFrame(blob2.tags)


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
