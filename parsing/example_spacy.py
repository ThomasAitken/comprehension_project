import spacy

nlp = spacy.load("en_core_web_sm")
# doc = nlp("Apple is looking at buying U.K. startup for $1 billion")

# for token in doc:
#     print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
#             token.shape_, token.is_alpha, token.is_stop)
# for ent in doc.ents:
#     print(ent.label_)

# doc = nlp("Bob went to the supermarket to buy what he needed for Christmas. He was in a rush and missed some things - most importantly, the passionfruit that his aunt wanted for the pavlova.")
# for token in doc:
#     print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_)

'''Bob Bob PROPN NNP nsubj
went go VERB VBD ROOT
to to ADP IN prep
the the DET DT det
supermarket supermarket NOUN NN pobj
to to PART TO aux
buy buy VERB VB advcl
what what PRON WP dobj
he -PRON- PRON PRP nsubj
needed need VERB VBD ccomp
for for ADP IN prep
Christmas Christmas PROPN NNP pobj
. . PUNCT . punct
He -PRON- PRON PRP nsubj
was be AUX VBD ROOT
in in ADP IN prep
a a DET DT det
rush rush NOUN NN pobj
and and CCONJ CC cc
missed miss VERB VBD conj
some some DET DT det
things thing NOUN NNS dobj
- - PUNCT : punct
most most ADV RBS advmod
importantly importantly ADV RB advmod
, , PUNCT , punct
the the DET DT det
passionfruit passionfruit NOUN NN dobj
that that SCONJ IN dobj
his -PRON- DET PRP$ poss
aunt aunt NOUN NN nsubj
wanted want VERB VBD relcl
for for ADP IN prep
the the DET DT det
pavlova pavlova NOUN NN pobj
. . PUNCT . punct'''

# for ent in doc.ents:
#     print(ent.text)
#     print(ent.label_)

#only picks up Bob = PERSON, Christmas = DATE (but really Christmas here is an *event*, and the event in question needn't even occur on the 25th of December)

# doc = nlp("I am not particularly impressed by the capabilities of the parser and labeller hitherto. I mean, it's probably better than what I could do in any reasonable timeframe, but it's clearly not perfect. I know that I have work to do in enriching the ontology.")

# for ent in doc.ents:
#     print(ent.text, ent.label_)
#     #absolutely zilch


from benepar.spacy_plugin import BeneparComponent
nlp.add_pipe(BeneparComponent("benepar_en2"))
doc = nlp(u"The time for action is now. It's never too late to do something. Bob went to the supermarket to buy what he needed for Christmas. He was in a rush and missed some things - most importantly, the passionfruit that his aunt wanted for the pavlova. I am not particularly impressed by the capabilities of the parser and labeller hitherto. I mean, it's probably better than what I could do in any reasonable timeframe, but it's clearly not perfect. I know that I have work to do in enriching the ontology.")
for sent in list(doc.sents):
    print(sent._.parse_string)
    #(S (NP (NP (DT The) (NN time)) (PP (IN for) (NP (NN action)))) (VP (VBZ is) (ADVP (RB now))) (. .))
    print(sent._.labels)
    #('S',)
    print(list(sent._.children)[0])
    #The time for action