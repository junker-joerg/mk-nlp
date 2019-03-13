from __future__ import print_function, unicode_literals
import spacy
import de_core_news_sm

nlp = spacy.load('de_core_news_sm')
doc = nlp(u'Ich bin ein Berliner.')

# show universal pos tags
print(' '.join('{word}/{tag}'.format(word=t.orth_, tag=t.pos_) for t in doc))
# output: Ich/PRON bin/AUX ein/DET Berliner/NOUN ./PUNCT

# show German specific pos tags (STTS)
#print(' '.join('{word}/{tag}'.format(word.orth_, tag.tag_) for t in doc)) ! hier kommt noch ein Fehler 
# output: Ich/PPER bin/VAFIN ein/ART Berliner/NN ./$.

# show dependency arcs
print('\n'.join('{child:<8} <{label:-^7} {head}'.format(child=t.orth_, label=t.dep_, head=t.head.orth_) for t in doc))
# output: (sb: subject, nk: noun kernel, pd: predicate)
# Ich      <--sb--- bin
# bin      <-ROOT-- bin
# ein      <--nk--- Berliner
# Berliner <--pd--- bin
# .        <-punct- bin

# show named entities
for ent in doc.ents:
    print(ent.text)
# output:
# Berliner - nein!

# show noun chunks
for chunk in doc.noun_chunks:
    print(chunk.text)
# output:
# ein Berliner

# noun chunks include so-called measure constructions ...
doc = de(u'Ich möchte gern zum Essen eine Tasse Kaffee bestellen.')
print([ chunk for chunk in doc.noun_chunks ])
# output:
# [Essen, eine Tasse Kaffee]

# ... and close appositions
doc = de(u'Der Senator vermeidet das Thema Flughafen.')
print([ chunk for chunk in doc.noun_chunks ])
# output:
# [Der Senator, das Thema Flughafen]