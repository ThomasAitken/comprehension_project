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