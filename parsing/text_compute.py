#Move through some text "blah blah".... Track agents.. Track events. Track changes to the world. Isolate and articulate the changes to the world
#Paraphrasing <---> thorough atomic decomposition. Paraphrasing = translation into simpler concepts
#"The lion chased the gazelle"  = "Animal goes towards other animal with purpose = food"



#Example problem is that of sentences describing movement.... 
#Task: (i) Identify two locations or direction of movement with respect to some marker... 
#             Marker can be non-living or living (as in above)
#            
from database.sqlite import *
from database.lists import *
import os
from .utils import category_tokens

import json

def parse_sentences(sentences: list):
    nouns = []
    verbs = []
    for sentence in sentences:
        for token in sentence:
            name = token.text
            part_of_speech = token.pos_
            label = token.ent_type_
            print(name, part_of_speech, label)
            if part_of_speech == "NOUN":
                similarity_vector = compute_similarity_vector(token)
                label = max(similarity_vector.keys(), key=lambda x: similarity_vector[x])
                if validate_entry(name, label, similarity_vector) == 'ACCEPT':
                    if prev_entry:
                        if json.loads(prev_entry[1]):
                prev_entry = find_entry((concept, label), nouns)
                            
                    else: 
                        add_entry(name, label, json.dumps(similarity_vector))


            else:
                similarity_scores = []
                if part_of_speech == "Noun":
                    token1.similarity(token2)

            
def validate_entry(name: str, label: str, similarity_vector: dict):
    print('Name: %s\nLabel: %s\nSimilarity Vector: %s' % (name, label, similarity_vector))
    verdict = ''
    while verdict not in ('y', 'n'):
        verdict = input('Do you accept this new database entry? y/n')
        if verdict not in ('y', 'n'):
            print('Stop screwing with me! \'y\' or \'n\'!')
    if verdict == 'y':
        return 'ACCEPT'
    else:
        label_suggestion = 



def determine_count_mass(noun):
    if token.pos:
        pass

def compute_similarity_vector(token) -> dict:
    similarity_vector = {}
    for cat_token in category_tokens:
        similarity_vector[cat_token] = token.similarity(cat_token)
    return similarity_vector

def find_category(token, similarity_vector: dict):
    pass



        