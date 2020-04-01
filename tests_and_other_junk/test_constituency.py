import sys
sys.path.insert(0, '/home/crastollgorton/comprehension_project')
from itertools import chain
from parsing.constituency import neaten_sentence
import spacy
nlp = spacy.load("en_core_web_lg")
from benepar.spacy_plugin import BeneparComponent
nlp.add_pipe(BeneparComponent("benepar_en2"))


strange_sentence = nlp("One Sunday morning the warm sun came up... and POP, out of the egg came a tiny, very hungry caterpillar.")
for sent in strange_sentence.sents:
    constituent_groups = []
    parsed_sent_obj = neaten_sentence(sent)
    for constit_group in parsed_sent_obj:
        constituent_groups.append(constit_group)
    print(constituent_groups)

'''OUTPUT: 
    [{'NP': One Sunday morning, 'NP_1': the warm sun, 'VP': came up}, {'PP': out of the egg, 'VP': came, 'NP': a tiny, very hungry caterpillar}, {'ADVP': POP}, {'CC': and}]
'''
#for the moment going to ignore aberrant constituents 'POP' and AND, and all other constituents like them (this class defined by inscrutability to the Berkeley parser - irreconcilability with the larger sentence-level structures) 
