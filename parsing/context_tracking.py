from .utils import classify_
import logging
import spacy
nlp = spacy.load("en_core_web_lg")
logger = logging.getLogger(__name__)

#just a dummy code to stop VS Code saying ''nlp' not defined'
# nlp = lambda x : x



def generic_location(paragraph):
    generic_locations = [nlp("nature"), nlp("urban"), nlp("suburban"), nlp("park"), nlp("corporate"), nlp("party"), nlp("sport"), nlp("game"), nlp("home"), nlp("historic"), nlp("prehistoric"), nlp("galaxy space")]
    try:
        bestfit_locale = max(generic_locations, key=lambda gen_loc: paragraph.similarity(gen_loc))
    except Exception as e:
        print(e)
        logger.error("Paragraph too big for similarity comparison perhaps? Might need to account...")
        return None
    return bestfit_locale

def probe_context(noun_phrase)->dict:
    relevant_entities = ("LOC", "DATE", "TIME")
    context_data = {}
    for ent in noun_phrase.ents:
        if ent.label_ in relevant_entities:
            # context_data[ent.label_] = (ent.text, ent.text)
            context_data[ent.label_] = ent.text
    if context_data:
        return context_data
    #Notice: "One Sunday Morning" is both "DATE" and "TIME" at once.
    day_similarity = noun_phrase.similarity(nlp("day, day-time"))
    night_similarity = noun_phrase.similarity(nlp("night, night-time"))
    if day_similarity > 0.5 and day_similarity > night_similarity:
        # context_data["TIME"] = ("day", noun_phrase.text)
        context_data["TIME"] = "day-time"
        # return context_data
    if night_similarity > 0.5 and night_similarity > day_similarity:
        # context_data["TIME"] = ("night", noun_phrase.text)
        context_data["TIME"] = "night-time"
        # return context_data
    generic_locations = [nlp("nature"), nlp("urban"), nlp("suburban"), nlp("park"), nlp("corporate"), nlp("party"), nlp("sport"), nlp("game"), nlp("home"), nlp("historic"), nlp("prehistoric"), nlp("galaxy space")]
    #strange exception, as in '.. after that' where 'that' is NP
    if noun_phrase.text == "that":
        return context_data
    classification = classify_(noun_phrase, generic_locations)
    print(noun_phrase, classification)
    if classification:
        if context_data.get("LOC", None):
            logger.error("Assumption violated about location determination for noun_phrase: %s" % noun_phrase)
        # context_data ["LOC"] = (classification[0].text, noun_phrase.text)
        context_data["LOC"] = classification[0].text
        return context_data
    
    return context_data


def get_context(sentence):
    # {'NP': the light of the moon, 'prep': In})
    # [One Sunday morning, the warm sun]
    '''  def __init__(self, noun_phrases: list, verb_phrases: list, subordinates: tuple, dialogue_meta = {}, verbal_decomp=[]):
        self.noun_phrases = noun_phrases
        self.verb_phrases = verb_phrases
        self.subordinates = subordinates
        self.dialogue_meta = dialogue_meta
        self.verbal_decomp = verbal_decomp'''
    event = {}
    #grabbing context information from any prepositional-phrase auxiliary clause in sentence
    np_info = {}
    if sentence.subordinates != ('', ''):
        #prep_phrase lives in index 1
        np = sentence.subordinates[1]["NP"]
        # prep = sentence.subordinates[1]["prep"]
        np_info = probe_context(np)

    #grabbing context information from 'subordinate' noun phrase like "One
    #Sunday Morning" (essentially identical to prep-phrase auxiliary)    
    if len(sentence.noun_phrases) > 1:
        if sentence.subordinates != ('', ''):
            logger.error("Assumption violated about only one context-related subordinate clause")
        np_info = probe_context(sentence.noun_phrases[0])

    print(np_info)
    if np_info:
        if np_info.get("DATE", ()):
            event["Temporal Location (date)"] = np_info["DATE"]
        if np_info.get("TIME", ()):
            event["Temporal Location (time)"] = np_info["TIME"]
        if np_info.get("LOC", ()):
            event["Spatial Location"] = np_info["LOC"]
    return event
        



def extract_event(sent)->dict:
    event = get_context(sent)
    return event


def analyse_events(sentences, paragraph, paragraph_data):
    gen_loc = generic_location(paragraph).text
    paragraph_data["Generic Location"] = gen_loc
    for sent in sentences:
        event = extract_event(sent)
        event["Event Constituency Representation"] = str(sent)
        event["Original Sentence"] = sent.unparsed_text
        prev_events = paragraph_data.get("Events", [])
        key_keys = ("Temporal Location (date)", "Temporal Location (time)", "Spatial Location")
        if prev_events:
            last_time_place = prev_events[-1]
            for key in key_keys:
                if not event.get(key, ""):
                    #avoid multiplication of " (carried)" concatenation with replace
                    event[key] = last_time_place[key].replace(" (carried)", "") + " (carried)"
        else:
            for key in key_keys:
                if not event.get(key, ""):
                    event[key] = ""

        
        #event["Sentence Text"] = sent.original_text
        print(event)
        paragraph_data["Events"] = paragraph_data.get("Events", []) + [event]
    # print(chapter)
