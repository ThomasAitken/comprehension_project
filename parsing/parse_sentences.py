#Move through some text "blah blah".... Track agents.. Track events. Track changes to the world. Isolate and articulate the changes to the world
#Paraphrasing <---> thorough atomic decomposition. Paraphrasing = translation into simpler concepts
#"The lion chased the gazelle"  = "Animal goes towards other animal with purpose = food"



#Example problem is that of sentences describing movement.... 
#Task: (i) Identify two locations or direction of movement with respect to some marker... 
#             Marker can be non-living or living (as in above)
#            
from crastollgorton.comprehension_project.database import sqlite
from crastollgorton.comprehension_project.database.lists import *

def parse_sentences(sentences: list):
    nouns = []
    verbs = []
    for sentence in sentences:
        for token in sentence:
            name = token.text
            part_of_speech = token.pos_
            label = token.ent_type_
            print(name, part_of_speech, label)
            if label:
                prev_entry = sqlite.find_entry((name, part_of_speech))
                if not prev_entry:
                    sqlite.add_entry(name, label, part_of_speech)
            else:
                similarity_scores = []
                if part_of_speech == "Noun":
                    token1.similarity(token2)

            i

    