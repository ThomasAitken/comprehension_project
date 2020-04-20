import spacy

nlp = spacy.load("en_core_web_lg")

doc=nlp(u"Apple's position in the stock market is going from strength to strength after another big quarter. Apple has always put aesthetics and design at front and centre of its technology products. Apples are a wonderfully versatile fruit, perfect in pies, salads or just as a raw snack. Apple is my favourite fruit by far. My favourite fruit by far is apple.")


# for sent in list(doc.sents):
#     for ent in sent.ents:
#         print(ent.text, ent.label_)
#     for token in sent:
#         ORG=nlp(u"business")
#         FOOD = nlp(u"food")
#         if "apple" in token.text.lower():
#             print(token.text, token.similarity(ORG), token.similarity(FOOD))
#             print(ORG.similarity(sent), FOOD.similarity(sent))


'''
Apple ORG
another big quarter DATE
Apple 0.20133079997660672 0.3607391636060644 [[[1st sentence word similarities]]]
0.560074474112831 0.4857149737372199 [[[1st sentence sentence-level]]]

Apple ORG
Apple 0.20133079997660672 0.3607391636060644 [[[2nd sentence word]]]
0.5814027113322515 0.516488788344492 [[[2nd sentence sentence-level]]]

Apples ORG
Apples 0.09617324563915237 0.4069360270660443 [[[3rd sentence word]]]
0.4129833618341481 0.6327367655456232 [[[3rd sentence sentence-level]]]

Apple ORG
Apple 0.20133079997660672 0.3607391636060644 [[[4th sentence word]]]
0.41347232085146157 0.5659679579347844 [[[4th sentence sentence-level]]]

apple ORG
apple 0.20133079997660672 0.3607391636060644 [[[5th sentence word]]]
0.41347232085146157 0.5659679579347844 [[[5th sentence sentence-level]]]
'''

#VERDICT = EVERYTHING WORKS AT THE SENTENCE LEVEL!! WOW, GOOD OUTCOME! GREAT MODEL!



# from benepar.spacy_plugin import BeneparComponent
# nlp.add_pipe(BeneparComponent("benepar_en2"))
# doc = nlp(u"Apple's position in the stock market is going from strength to strength after another big quarter. Apple has always put aesthetics and design at front and centre of its technology products. Apples are a wonderfully versatile fruit, perfect in pies, salads or just as a raw snack. Apple is my favourite fruit by far. My favourite fruit by far is apple.")
# for sent in list(doc.sents):
#     print(sent._.parse_string)
#     print(sent._.parent)
#     print(list(sent._.children))

'''

[[[[parse_string]]] (S (NP (NP (NP (NNP Apple) (POS 's)) (NN position)) (PP (IN in) (NP (DT the) (NN stock) (NN market)))) (VP (VBZ is) (VP (VBG going) (PP (IN from) (NP (NN strength))) (PP (TO to) (NP (NN strength))) (PP (IN after) (NP (DT another) (JJ big) (NN quarter))))) (. .))
[[[parent]]] None
[[[children]]]  [Apple's position in the stock market, is going from strength to strength after another big quarter, .]

[[[parse_string]]] (S (NP (NNP Apple)) (VP (VBZ has) (ADVP (RB always)) (VP (VBN put) (NP (NNS aesthetics) (CC and) (NN design)) (PP (IN at) (NP (NP (NN front) (CC and) (NN centre)) (PP (IN of) (NP (PRP$ its) (NN technology) (NNS products))))))) (. .))
[[[parent]]] None
[[[children]]]  [Apple, has always put aesthetics and design at front and centre of its technology products, .]

[[[[parse_string]]] (S (NP (NNS Apples)) (VP (VBP are) (NP (NP (DT a) (ADJP (RB wonderfully) (JJ versatile)) (NN fruit)) (, ,) (ADJP (JJ perfect) (PP (PP (IN in) (NP (NNS pies)) (, ,) (NP (NNS salads))) (CC or) (PP (ADVP (RB just)) (IN as) (NP (DT a) (JJ raw) (NN snack))))))) (. .))
[[[parent]]] None
[[[children]]]  [Apples, are a wonderfully versatile fruit, perfect in pies, salads or just as a raw snack, .]

[[[[parse_string]]] (S (NP (NN Apple)) (VP (VBZ is) (NP (PRP$ my) (JJ favourite) (NN fruit)) (PP (IN by) (ADVP (RB far)))) (. .))
[[[parent]]] None
[[[children]]]  [Apple, is my favourite fruit by far, .]

[[[[parse_string]]] (S (NP (PRP$ My) (JJ favourite) (NN fruit)) (PP (IN by) (ADVP (RB far))) (VP (VBZ is) (NP (NN apple))) (. .))
[[[parent]]] None
[[[children]]]  [My favourite fruit, by far, is apple, .]
'''

# from benepar.spacy_plugin import BeneparComponent
# nlp.add_pipe(BeneparComponent("benepar_en2"))
# doc = nlp(u"I wonder if this sentence is long enough to have a parent and a child, such that it will help me identifying what those terms are supposed to mean. Apples, a wonderfully versatile fruit, are still no match for peaches, which are the ultimate in adaptability. Batman and Superman fought out a terrible and bloody conflict, each suffering injuries. I love to annoy the angry pedants who love to annoy those who speak colloquially.")
# for sent in list(doc.sents):
#     print(sent._.parse_string)
#     print(sent._.parent)
#     print(list(sent._.children))

# doc=nlp(u"Abstract; universal; emotion; thought")
# doc1 = nlp(u"Tangible; useful; common; physical; object")
# concrete_things = [nlp("leaf"), nlp("table"), nlp("book"), nlp("spaghetti"), nlp("tree"), nlp("cat")]
# abstract_things = [nlp("mathematics"), nlp("physics"), nlp("love"), nlp("light"), nlp("energy")]

# for thing in concrete_things:
#     print(thing, "abstraction similarity: %f" % thing.similarity(doc), "concreteness similarity: %f" % thing.similarity(doc1))
# for thing in abstract_things:
#     print(thing, "abstraction similarity: %f" % thing.similarity(doc), "concreteness similarity: %f" % thing.similarity(doc1))

category_tokens = [nlp(u"mammal"), nlp(u"reptile"), nlp(u"insect"), nlp(u"fish"), nlp(u"business"), nlp(u"building"), nlp(u"infrastructure"), nlp(u"event"), nlp(u"date"), nlp(u"activity"), nlp(u"game"), nlp(u"sport"), nlp(u"country"), nlp(u"city"), nlp(u"state"), nlp(u"language"), nlp(u"location"), nlp(u"person"), nlp(u"plant"), nlp(u"tree"), nlp(u"product"), nlp(u"food"), nlp(u"tool"), nlp(u"toy"), nlp(u"work of art"), nlp(u"object"), nlp(u"rock"), nlp(u"mineral"), nlp(u"appliance"), nlp(u"app"), nlp(u"emotion"), nlp(u"happiness"), nlp(u"sadness"), nlp(u"anger"), nlp(u"surprise"), nlp(u"container"), nlp(u"science")]

doc = nlp("the light of the moon")
doc1 = nlp("the sun came up")
# for c_t in category_tokens:
#     print(c_t, doc.similarity(c_t))
print(doc.similarity(nlp("night, night-time")))
print(doc.similarity(nlp("day, day-time")))
print(doc1.similarity(nlp("day, day-time")))
for ent in nlp("One Sunday morning").ents:
    print(ent.label_, ent.text)
