import spacy

nlp = spacy.load("en_core_web_lg")

doc=nlp(u"Every day, Bob would run to the supermarket. Each morning, I collect groceries. Back when she used to work for Google, Stacy used to prepare her lunch every day; now, she bought it from the kiosk. I like pie. John enjoys playing golf. Boulders are large rocks. He always loved to dance")

for sent in list(doc.sents):
    for ent in sent.ents:
        print(ent.text, ent.label_)
    for token in sent:
        print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_)


'''Every day DATE
Bob PERSON

Every every DET DT det
day day NOUN NN npadvmod
, , PUNCT , punct
Bob Bob PROPN NNP nsubj
would would VERB MD aux
run run VERB VB ROOT
to to ADP IN prep
the the DET DT det
supermarket supermarket NOUN NN pobj
. . PUNCT . punct

Each morning TIME
Each each DET DT det
morning morning NOUN NN npadvmod
, , PUNCT , punct
I -PRON- PRON PRP nsubj
collect collect VERB VBP ROOT
groceries grocery NOUN NNS dobj
. . PUNCT . punct

Google ORG
Stacy PERSON
every day DATE

Back back ADV RB advmod
when when ADV WRB advmod
she -PRON- PRON PRP nsubj
used use VERB VBD advcl
to to PART TO aux
work work VERB VB xcomp
for for ADP IN prep
Google Google PROPN NNP pobj
, , PUNCT , punct
Stacy Stacy PROPN NNP nsubj
used use VERB VBD ccomp
to to PART TO aux
prepare prepare VERB VB xcomp
her -PRON- DET PRP$ poss
lunch lunch NOUN NN dobj
every every DET DT det
day day NOUN NN npadvmod
; ; PUNCT : punct
now now ADV RB advmod
, , PUNCT , punct
she -PRON- PRON PRP nsubj
bought buy VERB VBD ROOT
it -PRON- PRON PRP dobj
from from ADP IN prep
the the DET DT det
kiosk kiosk NOUN NN pobj
. . PUNCT . punct
I -PRON- PRON PRP nsubj
like like VERB VBP ROOT
pie pie NOUN NN dobj
. . PUNCT . punct

John PERSON

John John PROPN NNP nsubj
enjoys enjoy VERB VBZ ROOT
playing play VERB VBG xcomp
golf golf NOUN NN dobj
. . PUNCT . punct
Boulders boulder NOUN NNS nsubj
are be AUX VBP ROOT
large large ADJ JJ amod
rocks rock NOUN NNS attr
. . PUNCT . punct

He -PRON- PRON PRP nsubj
always always ADV RB advmod
loved love VERB VBD ROOT
to to PART TO aux
dance dance VERB VB xcomp

'''

# doc1 = nlp(u"routine")
# doc2 = nlp(u"Each day. Once a week. At 3 O'clock on Thursday.")
# for sent in doc2.sents:
#     print(sent.text)
#     print(sent.similarity(doc1))

'''Each day.
0.41314557730304713
Once a week.
0.42811542380935474
At 3 O'clock on Thursday.
0.29523106418502293'''
