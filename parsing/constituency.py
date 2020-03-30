import spacy
nlp = spacy.load("en_core_web_lg")
from benepar.spacy_plugin import BeneparComponent
nlp.add_pipe(BeneparComponent("benepar_en2"))
import re
import logging
logger = logging.getLogger(__name__)
import pdb

'''VB	VERB	VerbForm=inf	verb, base form
VBD	VERB	VerbForm=fin Tense=past	verb, past tense
VBG	VERB	VerbForm=part Tense=pres Aspect=prog	verb, gerund or present participle
VBN	VERB	VerbForm=part Tense=past Aspect=perf	verb, past participle
VBP	VERB	VerbForm=fin Tense=pres	verb, non-3rd person singular present
VBZ	VERB	VerbForm=fin Tense=pres Number=sing Person=three	verb, 3rd person singular present'''

#verb_phrase = tuple with (noun_phrase, verb +- negation, {key}:{noun_phrase/prepositional_phrase})

class StandardSentence(object):
    def __init__(self, noun_phrase, verb_phrase, subordinates: tuple, dialogue_meta: dict = {}):
        self.noun_phrase = noun_phrase
        self.verb_phrase = verb_phrase
        # self.object_ = object_
        self.subordinates = subordinates
        self.dialogue_meta = dialogue_meta


# #need to implement a deep learning model to identify predication (description of stable properties)
# def identify_stable_attribution(sentence, verb_phrase)->bool:

#     # label = token.ent_type_
#     if len(sentence.ents) > 0:
#         time_entities = [ent for ent in sentence.ents if ent.label_ in ("TIME", "DATE")]
#         if time_entities:
#             for time_entity in time_entities:
#                 routine = identify_routines(time_entity)
#                 if routine:
#                     stable_description = 'x'



    pass

#currently only dealing with simple case of one utterance contained within quotes
#not dealing with sentences like "That smells so bad," said James, "Like a sewer!".
def dialogue_parse(sentence)->dict:
    output = {"utterance": "", "expression_details": []}
    if sentence._.labels[0] == "SINV" and "\"" in [str(child) for child in sentence._.children]:
        skip_idx = -1
        for idx,child in enumerate(sentence._.children):
            if idx == skip_idx:
                continue
            if str(child) == "\"" and (str(list(sentence._.children)[idx+2]) == "\"" or str(list(sentence._.children)[idx+3]) == "\""):
                utterance = list(sentence._.children)[idx+1]
                output["utterance"] = utterance
                skip_idx = idx+1
                continue
            if str(child) not in ("\"", ",", ";", "."):
                output["expression_details"].append(child)
        return output
    else:
        return {}

#test passed!

# doc = nlp(u"\"A journey of a thousand miles begins with a single step,\" said Lao Tzu, as he mounted his horse.")
# for sentence in doc.sents:
#     print(dialogue_parse(sentence))


#yields sentence/sentences (can be multiple constituency-parsed sentences within single sentence as identified superficially by full-stop) in format {"NP": .., "VP": .., "SBAR": ..}
def neaten_sentence(sentence)->dict:
    # constituent_labels = re.findall(r'\(([A-Z]*?)\s', parse_string)
    # print(constituent_labels)
    # sentence = list(sentence.sents)[0]
    # constituents = list(sentence._.constituents)
    flat_representation = {}
    for level1_child in sentence._.children:
        # print(level1_child)
        print(str(sentence))
        if str(level1_child) in (".", ",", ";", "..."):
            continue
        try:
            constituent_label = level1_child._.labels[0]
        except:
            logger.error("Couldn't get label for %s" % (str(level1_child)))
            #for some reason conjunction constituents not being labelled properly here.. need to fix bug in benepar
            constituent_label = "CC"

        if constituent_label in ("S", "SINV"):
            yield neaten_sentence(level1_child)
            continue
        else:
            #no two phrases of the same kind in the flat representation
            if constituent_label in flat_representation:
                logger.warn("Assumption violated!")
                constituent_label = constituent_label+"_1"
            flat_representation[constituent_label] = level1_child
    yield flat_representation


#unfinished nonsense
'''
    # sentence_tree = {}
    # # sentence_tree[0] = {"S": sentence}
    # level_indicator = 0
    # for idx,constituent in enumerate(constituents):
    #     if level_indicator not in sentence_tree:
    #         sentence_tree[level_indicator] = [{constituent._.label: constituent}]
    #     else:
    #         sentence_tree[level_indicator].append({constituent._.label: constituent})
    #     while True:
    #         #unary chain
    #         if constituent._.label in ("NP", "VP", "PP"):
    #             child = list(constituent._.children)[0]
    #             sentence_tree[level_indicator+1] = {child._.label: child}
    #         else:
    #             break
    #     if constituent._.children:
    #         level_indicator += 1

    #     print(str(constituent))
    #     print(constituent._.labels)
    #     children = list(constituent._.children)
    #     print(children)
    #     # if level == 0:
    #     #     level0_children = children
    #     #     level += 1
    #     # if children:
    #     #     for child in children:
    #     #         if child not in level0_children:


    #     # print(list(constituent._.children))
    # # assert(len(constituent_labels)==len(constituents)+1), "Weird error in constituent parsing."

    # output = {}
    # label_instance_counts = {}
    # output[0] = {"S": sentence}
    # for idx,label in enumerate(constituent_labels):
    #     if label not in output:
    #         output[label] = constituents[idx]
    #         label_instance_counts[label] = 1
    #     else:
    #         key = label + "_%d" % label_instance_counts[label]
    #         output[key] = constituents[idx]
    #         label_instance_counts[label] += 1
    # return output
'''


# parse_string = '(S (NP (DT The) (JJ alpine) (NNS wildflowers)) (VP (VBP are) (PP (IN in) (NP (NN bloom))) (PP (DT all) (IN around) (NP (PRP us)))) (. .))'
# doc1 = nlp(u"The alpine wildflowers are in bloom all around us.")
# doc2 = nlp(u"The alpine wildflowers are in bloom all around us; their perfume fills our nostrils and lifts our spirits.")
# for sent in doc1.sents:
#     # x = neaten_sentences(sent)
#     sentences = []
#     for output in neaten_sentence(sent):
#         if type(output) == dict and output != {}:
#             sentences.append(output)
#         #output is generator
#         else:
#             for x in output:
#                 sentences.append(x)
#     # print(neaten_sentences(sent))
#     print(sentences)
# for sent in doc2.sents:
#     sentences = []
#     for output in neaten_sentence(sent):
#         if type(output) == dict:
#             sentences.append(output)
#         else:
#             for x in output:
#                 sentences.append(x)
#     print(sentences)




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
def grab_standard_sentences(constituents: dict)->str:
    pass


class UnexpectedParsing(Exception):
    pass

def constituency_parse(sentence):
    dialogue_data = dialogue_parse(sentence)
    if not dialogue_data:
        clean_sentences = []
        for output in neaten_sentence(sentence):
            if type(output) == dict and output != {}:
                clean_sentences.append(output)
            #output is generator
            else:
                for x in output:
                    clean_sentences.append(x)
        for clean_sent in clean_sentences:
            try:
                noun_phrase = clean_sent["NP"]
            except UnexpectedParsing:
                logger.error("No NP at level 1!")
            try:
                verb_phrase = clean_sent["VP"]
            except KeyError as e:
                print(str(clean_sent))
                raise UnexpectedParsing("No VP at level 1!")
                pdb.set_trace()
            sbar = clean_sent.get("SBAR", "")
            prep_phrase = clean_sent.get("PP", "")
            standard_sentence = StandardSentence(noun_phrase=noun_phrase, verb_phrase=verb_phrase, subordinates=(sbar, prep_phrase))
            return standard_sentence
    else:
        clean_sentences = []
        for output in neaten_sentence(dialogue_data["utterance"]):
            if type(output) is dict and output != {}:
                clean_sentences.append(output)
            else:
                for x in output:
                    clean_sentences.append(x)
            for clean_sent in clean_sentences:
                try:
                    noun_phrase = clean_sent["NP"]
                except UnexpectedParsing:
                    logger.error("No NP at level 1!")
                if "NP_1" in clean_sent:
                    noun_phrase = noun_phrase + " + " str(clean_sent["NP_1"])
                try:
                    verb_phrase = clean_sent["VP"]
                except UnexpectedParsing:
                    logger.error("No VP at level 1!")
                sbar = clean_sent.get("SBAR", "")
                prep_phrase = clean_sent.get("PP", "")
                standard_sentence = StandardSentence(noun_phrase=noun_phrase, verb_phrase=verb_phrase, subordinates=(sbar, prep_phrase), dialogue_meta=dialogue_data["expression_details"])
                return standard_sentence
            

            

    

    




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