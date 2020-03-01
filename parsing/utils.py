import spacy
import os

nlp = spacy.load("en_core_web_lg")
# from benepar.spacy_plugin import BeneparComponent
# nlp.add_pipe(BeneparComponent("benepar_en2"))


def get_category_tokens():
    categories = filter(lambda x: True if x.replace(".py","").upper() == x else False, os.listdir('jackendoff_objects/nouns'))

    tokens = []
    for cat in categories:
        tokens.append(nlp(u'%s' % cat))
    return tokens


category_tokens = [nlp(u"mammal"), nlp(u"reptile"), nlp(u"insect"), nlp(u"fish"), nlp(u"business"), nlp(u"building"), nlp(u"infrastructure"), nlp(u"event"), nlp(u"date"), nlp(u"activity"), nlp(u"game"), nlp(u"sport"), nlp(u"country"), nlp(u"city"), nlp(u"state"), nlp(u"language"), nlp(u"location"), nlp(u"person"), nlp(u"plant"), nlp(u"tree"), nlp(u"product"), nlp(u"food"), nlp(u"tool"), nlp(u"toy"), nlp(u"work of art"), nlp(u"object"), nlp(u"rock"), nlp(u"mineral"), nlp(u"appliance"), nlp(u"app"), nlp(u"happy emotion"), nlp(u"sad emotion"), nlp(u"anger"), nlp(u"surprise"), nlp(u"container")]

verbal_category_tokens = [nlp(u"physical process"), nlp(u"chemical process"), nlp(u"process"), nlp(u"injury"), nlp(u"movement"), nlp(u"gesture"), nlp(u"task"), nlp(u"chore"), nlp(u"happy emotion"), nlp(u"sad emotion"), nlp(u"anger"), nlp(u"surprise"), nlp(u"like"), nlp(u"dislike"), nlp(u"thought")]

OntoNotes_corpus = ["person", "norp", "fac", "org", "loc", "product", "event", "work_of_art", "law", "language", "date", "time", "percent", "money", "quantity", "ordinal", "cardinal"]

custom_concepts = ["animal", "insect", "plant", "business"]

#first two concrete, second two abstract
basic_concepts = ["organism", "non-organism", "process", "static_entity"]

verbal_concepts = ["injury", "entity_movement", "gesture"]

basic_verbal_concepts = ["action", "process"]
