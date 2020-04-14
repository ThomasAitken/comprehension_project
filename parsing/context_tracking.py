import logging

logger = logging.getLogger(__name__)

generic_locations = ["nature", "urban", "suburban", "park", "corporate", "party", "sport", "game", "home", "historic", "prehistoric", "galaxy space"]

def generic_location(paragraph):
    try:
        bestfit_locale = max([paragraph.similarity(gen_loc) for gen_loc in generic_locations])
    except:
        logger.error("Paragraph too big for similarity comparison perhaps? Might need to account...")
        return None
    return bestfit_locale

def probe_context(noun_phrase):
    relevant_entities = ("LOC", "DATE", "TIME")
    if len(noun_phrase.ents) > 1:
        logger.warn("Assumption about context phrase violated!")
        return None
        
    if len(noun_phrase.ents) > 0 and list(noun_phrase.ents)[0].label_ in relevant_entities:
        ent = list(noun_phrase.ents)[0]
        context_data = {"context_type": ent.label_, "content": ent.text}
        return context_data
    else:
        return {}

#         print(ent.text, ent.label_)

def get_context(sentence):
    # {'NP': the light of the moon, 'prep': In})
    # [One Sunday morning, the warm sun]
    '''  def __init__(self, noun_phrases: list, verb_phrases: list, subordinates: tuple, dialogue_meta = {}, verbal_decomp=[]):
        self.noun_phrases = noun_phrases
        self.verb_phrases = verb_phrases
        self.subordinates = subordinates
        self.dialogue_meta = dialogue_meta
        self.verbal_decomp = verbal_decomp'''
    if sentence.subordinates != ('', ''):
        np = sentence.subordinates["NP"]
        prep = sentence.subordinates["prep"]
    if len(sentence.noun_phrases) > 1:
        np_info = probe_context(sentence.noun_phrases[0])
        if np_info:
            pass



def extract_event(sent)->dict:
    get_context(sent)

def analyse_events(sentences, paragraph, chapter):
    generic_location = generic_location(paragraph)
    chapter["Generic Location"] = generic_location
    for sent in sentences:
        event_data = extract_event(sent)
        chapter["Events"] = chapter.get("Events", []) + [event_data]
