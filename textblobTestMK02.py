from __future__ import print_function, unicode_literals
import spacy

nlp = spacy.load('de')
doc = nlp(u'Ich bin ein Berliner.')

# show universal pos tags
# print(' '.join('{word}/{tag}'.format(word=t.orth_, tag=t.pos_) for t in doc))
# output: Ich/PRON bin/AUX ein/DET Berliner/NOUN ./PUNCT

# show German specific pos tags (STTS)
# print(' '.join('{word}/{tag}'.format(word.orth_, tag.tag_) for t in doc))
# output: Ich/PPER bin/VAFIN ein/ART Berliner/NN ./$.

# show dependency arcs
# print('\n'.join('{child:<8} <{label:-^7} {head}'.format(child=t.orth_, label=t.dep_, head=t.head.orth_) for t in doc))
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
# Berliner
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
# Use word vectors
de = spacy.load('de')
doc = de(u'Der Apfel und die Orange sind ähnlich')
assert len(doc.vector) == len(doc[0].vector)
der_apfel = doc[:2]
die_orange = doc[3:5]
der_apfel.similarity(die_orange)
# output:
# 0.63665210991205579
der, apfel = der_apfel
der.similarity(apfel)
# output:
# 0.24995991403916812