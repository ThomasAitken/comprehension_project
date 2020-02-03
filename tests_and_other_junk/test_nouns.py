import spacy

nlp = spacy.load("en_core_web_md")

from benepar.spacy_plugin import BeneparComponent
nlp.add_pipe(BeneparComponent("benepar_en2"))

doc = nlp(u"The alpine wildflowers are in bloom all around us. Truly a magnificent scene. I feel very privileged to be in this place of such jaw-dropping splendour. The one quibble I have with the world in this moment of bliss is that I feel slightly fatigued -- I suppose this is clear evidence, if any more was needed, that I have become physiologically dependent on coffee. Ah, coffee... I would really very much like some coffee. Drugs, loves, doves.")

for sent in list(doc.sents):
    print(sent._.parse_string)
    print(sent._.labels)
    for token in sent:
        print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_)


'''(S (NP (DT The) (JJ alpine) (NNS wildflowers)) (VP (VBP are) (PP (IN in) (NP (NN bloom))) (PP (DT all) (IN around) (NP (PRP us)))) (. .))
('S',)
The the DET DT det
alpine alpine ADJ JJ compound
wildflowers wildflower NOUN NNS nsubj
are be AUX VBP ROOT
in in ADP IN prep
bloom bloom NOUN NN pobj
all all DET DT advmod
around around ADP IN prep
us -PRON- PRON PRP pobj
. . PUNCT . punct
(FRAG (ADVP (RB Truly)) (NP (DT a) (JJ magnificent) (NN scene)) (. .))
('FRAG',)
Truly truly ADV RB advmod
a a DET DT det
magnificent magnificent ADJ JJ amod
scene scene NOUN NN ROOT
. . PUNCT . punct
(S (NP (PRP I)) (VP (VBP feel) (ADJP (RB very) (JJ privileged) (S (VP (TO to) (VP (VB be) (PP (IN in) (NP (NP (DT this) (NN place)) (PP (IN of) (NP (JJ such) (NN jaw) (: -) (JJ dropping) (NN splendour)))))))))) (. .))
('S',)
I -PRON- PRON PRP nsubj
feel feel VERB VBP ROOT
very very ADV RB advmod
privileged privileged ADJ JJ acomp
to to PART TO aux
be be AUX VB xcomp
in in ADP IN prep
this this DET DT det
place place NOUN NN pobj
of of ADP IN prep
such such ADJ JJ amod
jaw jaw NOUN NN compound
- - PUNCT : punct
dropping dropping ADJ JJ amod
splendour splendour NOUN NN pobj
. . PUNCT . punct
(NP (NP (DT The) (CD one) (NN quibble)) (SBAR (S (NP (PRP I)) (VP (VBP have) (PP (IN with) (NP (DT the) (NN world))) (PP (IN in) (NP (NP (DT this) (NN moment)) (PP (IN of) (NP (NN bliss)))))))))
('NP',)
The the DET DT det
one one NUM CD nsubj
quibble quibble NOUN NN ROOT
I -PRON- PRON PRP nsubj
have have AUX VBP relcl
with with ADP IN prep
the the DET DT det
world world NOUN NN pobj
in in ADP IN prep
this this DET DT det
moment moment NOUN NN pobj
of of ADP IN prep
bliss bliss NOUN NN pobj
(SQ (VBZ is) (SBAR (IN that) (S (NP (PRP I)) (VP (VBP feel) (ADJP (RB slightly) (VBN fatigued))))))
('SQ',)
is be AUX VBZ ROOT
that that SCONJ IN mark
I -PRON- PRON PRP nsubj
feel feel VERB VBP ccomp
slightly slightly ADV RB advmod
fatigued fatigue VERB VBN acomp
(S (: --) (NP (PRP I)) (VP (VBP suppose) (SBAR (S (NP (DT this)) (VP (VBZ is) (NP (JJ clear) (NN evidence) (PRN (, ,) (SBAR (IN if) (S (NP (DT any) (JJR more)) (VP (VBD was) (VP (VBN needed))))) (, ,)) (SBAR (IN that) (S (NP (PRP I)) (VP (VBP have) (VP (VBN become) (ADJP (RB physiologically) (JJ dependent) (PP (IN on) (NP (NN coffee))))))))))))) (. .))
('S',)
-- -- PUNCT : punct
I -PRON- PRON PRP nsubj
suppose suppose VERB VBP ROOT
this this DET DT nsubj
is be AUX VBZ ccomp
clear clear ADJ JJ amod
evidence evidence NOUN NN attr
, , PUNCT , punct
if if SCONJ IN mark
any any DET DT det
more more ADJ JJR nsubjpass
was be AUX VBD auxpass
needed need VERB VBN advcl
, , PUNCT , punct
that that SCONJ IN mark
I -PRON- PRON PRP nsubj
have have AUX VBP aux
become become VERB VBN ccomp
physiologically physiologically ADV RB advmod
dependent dependent ADJ JJ acomp
on on ADP IN prep
coffee coffee NOUN NN pobj
. . PUNCT . punct
(FRAG (INTJ (UH Ah)) (, ,) (NP (NN coffee)) (. ...))
('FRAG',)
Ah ah INTJ UH intj
, , PUNCT , punct
coffee coffee NOUN NN ROOT
... ... PUNCT . punct
(S (NP (PRP I)) (VP (MD would) (ADVP (RB really) (RB very) (RB much)) (VP (VB like) (NP (DT some) (NN coffee)))) (. .))
('S',)
I -PRON- PRON PRP nsubj
would would VERB MD aux
really really ADV RB advmod
very very ADV RB advmod
much much ADV RB advmod
like like VERB VB ROOT
some some DET DT det
coffee coffee NOUN NN pobj
. . PUNCT . punct
(NP (NNS Drugs) (, ,) (NNS loves) (, ,) (NNS doves) (. .))
('NP',)
Drugs drug NOUN NNS ROOT
, , PUNCT , punct
loves love NOUN NNS conj
, , PUNCT , punct
doves dove NOUN NNS appos
. . PUNCT . punct
'''