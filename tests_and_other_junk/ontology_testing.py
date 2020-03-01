import spacy
nlp = spacy.load("en_core_web_lg")

category_tokens = [nlp(u"mammal"), nlp(u"reptile"), nlp(u"insect"), nlp(u"fish"), nlp(u"business"), nlp(u"building"), nlp(u"infrastructure"), nlp(u"event"), nlp(u"date"), nlp(u"activity"), nlp(u"game"), nlp(u"sport"), nlp(u"country"), nlp(u"city"), nlp(u"state"), nlp(u"language"), nlp(u"location"), nlp(u"person"), nlp(u"plant"), nlp(u"tree"), nlp(u"product"), nlp(u"food"), nlp(u"tool"), nlp(u"toy"), nlp(u"work of art"), nlp(u"object"), nlp(u"rock"), nlp(u"mineral"), nlp(u"appliance"), nlp(u"app"), nlp(u"happy emotion"), nlp(u"sad emotion"), nlp(u"anger"), nlp(u"surprise"), nlp(u"container")]

strongest_match = max(category_tokens, key=lambda x: x.similarity(nlp(u"packet")))
print(strongest_match)
strongest_match = max(category_tokens, key=lambda x: x.similarity(nlp(u"bowl")))
print(strongest_match)
'''container'''
'''container'''
"HOLY SHIT IT REALLY WORKS HOLY SHIT THIS SHIT REALLY WORKS HOLY SHIT!"