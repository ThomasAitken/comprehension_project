import spacy
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

#Now you might ask: What is the point of these objects if you are doing fuck all therewith? 
#The answer is planning for the hypothetical future; it's called calculated redundancy, dumbass 

#Almost all of the time, a sentence will only have one noun phrase & one verb
#phrase at 'level 1' of the hierarchy, but sometimes there are multiple on the
#same level, e.g. "He killed a man, then buried the body" has two VPs. Hence
#pluralisation
class StandardSentence(object):
    def __init__(self, noun_phrases: list, verb_phrases: list, subordinates: tuple, dialogue_meta = {}, verbal_decomp=[]):
        self.noun_phrases = noun_phrases
        self.verb_phrases = verb_phrases
        self.subordinates = subordinates
        self.dialogue_meta = dialogue_meta
        self.verbal_decomp = verbal_decomp

    def __repr__(self):
        base = "NP: {}  VP: {}  SUB: {}  DIA: {}".format(self.noun_phrases, self.verb_phrases, self.subordinates, self.dialogue_meta)
        for verb_component in self.verbal_decomp:
            base += "\nVerbs: {}  Modifier: {}  NP: {}  PP: {}  ADJP: {}  ADVP: {}  Transitive: {}".format(verb_component.verbs, verb_component.modifier, verb_component.noun_phrases, verb_component.prep_phrase, verb_component.adj_phrase, verb_component.adverb_phrase, verb_component.transitive)
            if verb_component == self.verbal_decomp[-1]:
                base +=("\n")
        return base


#Modifier = prepposition that parser doesn't recognise as belonging to a
#prepositional phrase --- ideally, all prepositions forming compound verbs (e.g.
#"up" in "The sun came up." and negations like "not", "n't")
class VerbalDecomp(object):
    def __init__(self, verbs, modifier=None, noun_phrases=None, prep_phrase={}, adj_phrase=None, adverb_phrase=None, transitive=True):
        self.verbs = verbs
        self.modifier = modifier
        self.noun_phrases = noun_phrases
        self.prep_phrase = prep_phrase
        self.adj_phrase = adj_phrase
        self.adverb_phrase = adverb_phrase
        self.transitive = transitive


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
        # print(str(sentence))
        if str(level1_child) in (".", ",", ";", "...", "--", "!"):
            continue
        try:
            constituent_label = level1_child._.labels[0]
            if len(level1_child._.labels) > 1:
                print("Stop the presses, ")

        except:
            logger.error("Couldn't get label for %s" % (str(level1_child)))
            #for some reason conjunction constituents not being labelled properly here.. need to fix bug in benepar
            # print(len(level1_child._.children))
            constituent_label = list(level1_child)[0].tag_

        if constituent_label in ("S", "SINV"):
            for parsed_dict in neaten_sentence(level1_child):
                yield parsed_dict
            continue
        else:
            #no two phrases of the same kind in the flat representation
            if constituent_label in flat_representation:
                logger.warn("Assumption violated!")
                constituent_label = constituent_label+"_1"
            flat_representation[constituent_label] = level1_child
    yield flat_representation


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

def parse_prep_phrase(prep_phrase, prep0=None)->dict:
    try:
        prep = list(filter(lambda constit : list(constit)[0].tag_ == "IN", prep_phrase._.children))[0]
        noun_phrase = list(filter(lambda constit : len(constit._.labels) > 0 and constit._.labels[0] == "NP", prep_phrase._.children))[0]
    except IndexError:
        logger.warn("Default assumption violated about prepositional phrase structure. Trying recursive assumption")
        #Recursive assumption = we are dealing with a prepositional phrase that breaks down into prep + prepositional phrase
        #e.g. "out of the egg"
        prep_phrase = list(filter(lambda constit : len(constit._.labels) > 0 and constit._.labels[0] == "PP", prep_phrase._.children))[0]
        return parse_prep_phrase(prep_phrase, prep)
    
    prep_phrase = {"NP": noun_phrase, "prep": prep}
    if prep0:
        prep_phrase["prep0"] = prep0
    return prep_phrase

def constituency_parse(sentence):
    dialogue_data = dialogue_parse(sentence)
    clean_sentences = []
    if not dialogue_data:
        parsed = neaten_sentence(sentence)
    else:
        parsed = neaten_sentence(dialogue_data["utterance"])

    for output in parsed:
        if type(output) == dict and len(output) > 1:
            clean_sentences.append(output)
    for clean_sent in clean_sentences:
        try:
            noun_phrases = [clean_sent["NP"]]
        except UnexpectedParsing:
            #If this error gets thrown, probably an infinitive verb phrase.. gets tagged as 'Sentence' by Benepar for some reason
            logger.error("No NP at level 1!")
        if "NP_1" in clean_sent:
            noun_phrases = [clean_sent["NP"], clean_sent["NP_1"]]
        try:
            verb_phrases = [clean_sent["VP"]]
        except KeyError as e:
            print(str(clean_sent))
            raise UnexpectedParsing("No VP at level 1!")
            pdb.set_trace()
        if "VP_1" in clean_sent:
            verb_phrases = [clean_sent["VP"], clean_sent["VP_1"]]
        sbar = clean_sent.get("SBAR", "")
        prep_phrase = clean_sent.get("PP", "")
        if prep_phrase:
            prep_phrase = parse_prep_phrase(prep_phrase)
        yield StandardSentence(noun_phrases=noun_phrases, verb_phrases=verb_phrases, subordinates=(sbar, prep_phrase), dialogue_meta=dialogue_data)



# I want to determine if verb is transitive/intransitive (i.e. whether verb
# directly acts on a noun phrase (e.g. "Samantha kicked the ball") or whether it
# is on its own (e.g. "The man drinks") or whether it is connected to a
# prepositional phrase (i.e. "My kindly grandma sleeps in a caravan")).. Then
# separate out these components
# 


#ADVP, ADJP
def parse_verb_phrase(clean_sent: StandardSentence)->StandardSentence:
    def get_phrase(constituents, phrase_type):
        for constit in constituents:
            if constit._.labels[0] == phrase_type:
                return constit
        return None

    verb_phrases = clean_sent.verb_phrases
    constituents_meta = []
    verbs_meta = []
    modifiers = []
    for verb_phrase in verb_phrases:
        constituents = list(filter(lambda constit: len(constit._.labels) > 0, verb_phrase._.children))
        verbs = list(filter(lambda constit : list(constit)[0].tag_.startswith("V") and list(constit)[0].tag_ != "VBG", verb_phrase._.children))
        if len(verbs) > 1:
            logger.error("Unexpected num verbs!!!")
        #e.g. 'going' in 'was going' or 'looking' in 'started looking'
        gerund_phrases = list(filter(lambda constit : list(constit)[0].tag_ == "VBG", verb_phrase._.children))
        if gerund_phrases:
            if len(gerund_phrases) > 1:
                logger.error("Unexpected num gerunds!!!")
            gerund_phrase = gerund_phrases[0]
            gerund = list(gerund_phrase._.children)[0]
            verbs = [verbs[0], gerund]
            gerund_phrase_kids = list(filter(lambda constit: len(constit._.labels) > 0, gerund_phrase._.children))
            constituents += list(gerund_phrase_kids)
        try:
            modifier = list(filter(lambda constit : list(constit)[0].tag_ == "RB", verb_phrase._.children))[0]
        except IndexError:
            modifier = None
        
        modifiers.append(modifier)
        constituents_meta.append(constituents)
        verbs_meta.append(verbs)

    clean_sent.verbal_decomp = []
    for i,constituents in enumerate(constituents_meta):
        adj_phrase = get_phrase(constituents, "ADJP")
        adverb_phrase = get_phrase(constituents, "ADVP")
        if adverb_phrase is not None and modifiers[i] == adverb_phrase:
            modifiers[i] = None
        prep_phrase = get_phrase(constituents, "PP")
        noun_phrases = list(filter(lambda constit : constit._.labels[0] == "NP", constituents))
        if prep_phrase:
            prep_phrase = parse_prep_phrase(prep_phrase)
        else:
            prep_phrase = {}

        #case: intransitive
        if not noun_phrases:
            transitive = False
            verb_data = VerbalDecomp(verbs=verbs_meta[i], modifier=modifiers[i], prep_phrase=prep_phrase, adj_phrase=adj_phrase, adverb_phrase=adverb_phrase, transitive=transitive)
            clean_sent.verbal_decomp.append(verb_data)
        #case transitive = direct object = NP (in theory)
        else:
            transitive = True
            verb_data = VerbalDecomp(verbs=verbs_meta[i], modifier=modifiers[i], noun_phrases=noun_phrases, prep_phrase=prep_phrase, adj_phrase=adj_phrase, adverb_phrase=adverb_phrase, transitive=transitive)
            clean_sent.verbal_decomp.append(verb_data)
    return clean_sent
            

    

    




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