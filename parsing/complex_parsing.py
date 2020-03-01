import spacy
nlp = spacy.load("en_core_web_lg")
from benepar.spacy_plugin import BeneparComponent
nlp.add_pipe(BeneparComponent("benepar_en2"))
import re
import logging

'''VB	VERB	VerbForm=inf	verb, base form
VBD	VERB	VerbForm=fin Tense=past	verb, past tense
VBG	VERB	VerbForm=part Tense=pres Aspect=prog	verb, gerund or present participle
VBN	VERB	VerbForm=part Tense=past Aspect=perf	verb, past participle
VBP	VERB	VerbForm=fin Tense=pres	verb, non-3rd person singular present
VBZ	VERB	VerbForm=fin Tense=pres Number=sing Person=three	verb, 3rd person singular present'''

#verb_phrase = tuple with (noun_phrase, verb +- negation, {key}:{noun_phrase/prepositional_phrase})

class StandardSentence(object):
    def __init__(self, subject:str, verb: str, object_: dict, subordinates: list):
        self.subject = subject
        self.verb = verb
        self.object_ = object_
        self.subordinates = subordinates


#need to implement a deep learning model to identify predication (description of stable properties)
def identify_stable_attribution(sentence, verb_phrase)->bool:

    label = token.ent_type_
    if len(sentence.ents) > 0:
        time_entities = [ent for ent in sentence.ents if ent.label_ in ("TIME", "DATE")]
        if time_entities:
            boolean = identify_routines(time_entity)
            if boolean == True:
                stable_description = 'x'



    pass

def map_parsestring_to_constituents(parse_string, sentence)->dict:
    constituent_labels = re.findall(r'\(([A-Z]*?)\s', parse_string)
    print(constituent_labels)
    sentence = list(sentence.sents)[0]
    constituents = list(sentence._.constituents)
    if len(constituent_labels) != len(constituents):
        logging.error("What the fuck happened!!!! WHAT THE FUCK!!!! WHAT THE FUCK!!! *******AG*UGFOBFAEO")
        return {}
    output = {}
    label_instance_counts = {}
    for idx,label in enumerate(constituent_labels):
        if label not in output:
            output[label] = constituents[idx]
            label_instance_counts[label] = 1
        else:
            key = label + "_%d" % label_instance_counts[label]
            output[key] = constituents[idx]
            label_instance_counts[label] += 1
    return output
parse_string = '(S (NP (DT The) (JJ alpine) (NNS wildflowers)) (VP (VBP are) (PP (IN in) (NP (NN bloom))) (PP (DT all) (IN around) (NP (PRP us)))) (. .))'
print(map_parsestring_to_constituents(parse_string, nlp(u"The alpine wildflowers are in bloom all around us.")))
'''(S (NP (DT The) (JJ alpine) (NNS wildflowers)) (VP (VBP are) (PP (IN in) (NP (NN bloom))) (PP (DT all) (IN around) (NP (PRP us)))) (. .))
('S',)
[The alpine wildflowers are in bloom all around us., The alpine wildflowers, The, alpine, wildflowers, are in bloom all around us, are, in bloom, in, bloom, all around us, all, around, us, .]'''



def identify_routines(time_entity)->bool:
    if time_entity.similarity(nlp(u"routine")) > 0.35:
        return True
    else:
        return False


import re
#returns primary verb phrase in sentence
def grab_standard_sentences(parse_string)->str:
    sentences_within_sentence = re.findall(r'^\(S.*?(\().*?\((S')

    first_token = re.search(r'^S\s\((.*?)\s', parse_string).group(1)
    if first_token == "NP":
        pass
    if first_token != "NP":
        if first_token == "PP":
            pass

def ditinguish_purpose_or_location(prepositional_phrase)->str:
    pass



'''(S (NP (NP (DT The) (NN time)) (PP (IN for) (NP (NN action)))) (VP (VBZ is) (ADVP (RB now))) (. .))
('S',)
The time for action
(S (NP (PRP It)) (VP (VBZ 's) (ADVP (RB never)) (ADJP (RB too) (JJ late) (S (VP (TO to) (VP (VB do) (NP (NN something))))))) (. .))
('S',)
It
(S (NP (NNP Bob)) (VP (VBD went) (PP (TO to) (NP (DT the) (NN supermarket))) (S (VP (TO to) (VP (VB buy) (SBAR (WHNP (WP what)) (S (NP (PRP he)) (VP (VBD needed) (PP (IN for) (NP (NNP Christmas)))))))))) (. .))
('S',)
Bob
(S (NP (PRP He)) (VP (VP (VBD was) (PP (IN in) (NP (DT a) (NN rush)))) (CC and) (VP (VBD missed) (NP (NP (DT some) (NNS things)) (: -) (ADVP (RBS most) (RB importantly)) (, ,) (NP (NP (DT the) (NN passionfruit)) (SBAR (WHNP (IN that)) (S (NP (PRP$ his) (NN aunt)) (VP (VBD wanted) (PP (IN for) (NP (DT the) (NNP pavlova)))))))))) (. .))
('S',)
He
(S (NP (PRP I)) (VP (VBP am) (RB not) (VP (ADVP (RB particularly)) (VBN impressed) (PP (IN by) (NP (NP (DT the) (NNS capabilities)) (PP (IN of) (NP (DT the) (NN parser) (CC and) (NNP labeller))) (ADVP (RB hitherto)))))) (. .))
('S',)
I
(S (S (NP (PRP I)) (VP (VBP mean) (, ,) (SBAR (S (NP (PRP it)) (VP (VBZ 's) (ADVP (RB probably)) (ADJP (ADJP (JJR better)) (PP (IN than) (SBAR (WHNP (WP what)) (S (NP (PRP I)) (VP (MD could) (VP (VB do) (PP (IN in) (NP (DT any) (JJ reasonable) (NN timeframe)))))))))))))) (, ,) (CC but) (S (NP (PRP it)) (VP (VBZ 's) (ADVP (RB clearly)) (RB not) (ADJP (JJ perfect)))) (. .))
('S',)
I mean, it's probably better than what I could do in any reasonable timeframe
(S (NP (PRP I)) (VP (VBP know) (SBAR (IN that) (S (NP (PRP I)) (VP (VBP have) (NP (NP (NN work)) (SBAR (S (VP (TO to) (VP (VB do) (PP (IN in) (S (VP (VBG enriching) (NP (DT the) (NN ontology)))))))))))))) (. .))'''

'''(S (S (NP (PRP I)) (VP (VBP mean) (, ,) (SBAR (S (NP (PRP it)) (VP (VBZ 's) (ADVP (RB probably)) (ADJP (ADJP (JJR better)) (PP (IN than) (SBAR (WHNP (WP what)) (S (NP (PRP I)) (VP (MD could) (VP (VB do) (PP (IN in) (NP (DT any) (JJ reasonable) (NN timeframe))))))))))))))'''

def identify_freeindirectstyle(sentence):
    pass