# Tests verschiedener NLP Tools
# ! NLTK
# ! Textblob
# TODO commit
# TODO  git push https://github.com/junker-joerg/mk-nlp
# ! git remote add origin https://github.com/junker-joerg/mk-nlp
# - eröffnet und nochmal

from textblob_de import TextBlobDE

text = '''
"Der Blob" macht in seiner unbekümmert-naiven Weise einfach nur Spass.
Er hat eben den gewissen Charme, bei dem auch die eher hölzerne Regie und
das konfuse Drehbuch nicht weiter stören.
'''

blob = TextBlobDE(text)
blob.tags           # [('Der', 'DT'), ('Blob', 'NN'), ('macht', 'VB'),
                    #  ('in', 'IN'), ('seiner', 'PRP$'), ...]

blob.noun_phrases   # WordList(['Der Blob', 'seiner unbekümmert-naiven Weise',
                    #           'den gewissen Charme', 'hölzerne Regie',
                    #           'konfuse Drehbuch'])


for sentence in blob.sentences:
    print(sentence.sentiment.polarity)
# 1.0
# 0.0

blob.translate(to="es")  # '" The Blob " hace a su manera ingenua...'