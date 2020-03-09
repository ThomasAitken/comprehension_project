#Move through some text "blah blah".... Track agents.. Track events. Track changes to the world. Isolate and articulate the changes to the world
#Paraphrasing <---> thorough atomic decomposition. Paraphrasing = translation into simpler concepts
#"The lion chased the gazelle"  = "Animal goes towards other animal with purpose = food"



#Example problem is that of sentences describing movement.... 
#Task: (i) Identify two locations or direction of movement with respect to some marker... 
#             Marker can be non-living or living (as in above)
#
from parsing.constituency_parsing import dialogue_determine, neaten_sentences
import sys
# print(sys.path)  
from database.sqlite import *
# from database.lists import *
import os
from parsing.utils import category_tokens
import spacy
import math
import json

def parse_sentences(sentences: list):
    nouns = []
    verbs = []
    for sentence in sentences:
        #
        # sub_sentences = break_up_sentence(sentence)
        # for sub_sentence in sub_sentences:
        for token in sentence:
            chunk = sentence
            if len(sentence) > 25:
                chunk = grab_local_chunk(token, sentence)
            name = token.text
            part_of_speech = token.pos_
            label = token.ent_type_
            print(name, part_of_speech, label)
            if part_of_speech == "NOUN":
                similarity_vec_a = compute_similarity_vector(token)
                similarity_vec_b = compute_similarity_vector(chunk)
                loc_label = get_top_cat(similarity_vec_a)
                gen_label = get_top_cat(similarity_vec_b)

                sum_vec = get_vec_average(similarity_vec_a, similarity_vec_b)
                average_label = get_top_cat(sum_vec)

                prev_entry = find_entry((name, label), "nouns")[0]
                if prev_entry:
                    print(prev_entry)
                else:
                    if validate_entry(name, label, similarity_vector) == 'ACCEPT':
                        add_entry((name, label, similarity_vector), "nouns")

                            
                    # else: 
                    #     add_entry(name, label, json.dumps(similarity_vector))


            else:
                # similarity_scores = []
                # if part_of_speech == "Noun":
                #     token1.similarity(token2)
                pass

            
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
        pass

#not used
def break_up_sentence(sentence):
    num_sentences = math.ceil(len(sentence)/30)
    if num_sentences == 1:
        return [sentence]
    else:
        return chunks(sentence, 30)


def grab_local_chunk(token, sentence, chunk_param=25):
    token_index = -1
    for i in range(0, len(sentence)):
        if sentence[i] == token:
            token_index = i

    halfway_idx = chunk_param//2
    if token_index <= halfway_idx:
        chunk = sentence[0:chunk_param]
    else:
        chunk = sentence[token_index-halfway_idx:token_index+halfway_idx+1]
    return chunk

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def get_top_cat(sim_vec):
    return max(similarity_vec.keys(), key=lambda x: similarity_vec[x])

def get_vec_average(sim_vec_a, sim_vec_b):
    sum_vec = {}
    for cat_key in sim_vec_a:
        sum_vec[cat_key] = (sim_vec_a[cat_key] + sim_vec_b[cat_key])/2
    return sum_vec

def determine_count_mass(noun):
    if token.pos:
        pass

def compute_similarity_vector(token) -> dict:
    similarity_vector = {}
    for cat_token in category_tokens:
        similarity_vector[cat_token] = token.similarity(cat_token)
    return similarity_vector

def average_similarity_vector(token) -> dict:
    pass
    

def find_category(token, similarity_vector: dict):
    pass



        