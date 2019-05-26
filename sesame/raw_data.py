# -*- coding: utf-8 -*-
import nltk
lemmatizer = nltk.stem.WordNetLemmatizer()

from conll09 import CoNLL09Element, CoNLL09Example
from sentence import Sentence


def make_data_instance(text, index):
    """
    Takes a line of text and creates a CoNLL09Example instance from it.
    """
    tokenized = nltk.tokenize.word_tokenize(text.lstrip().rstrip())
    # for t in tokenized:
    #     print("p1", t, type(t))
    # tokenized = [x.decode("latin-1") for x in tokenized]
    # for t in tokenized:
    #     print("p2", t, type(t))

    #tokenized = [x.encode("ascii", "ignore") for x in tokenized]

    # for t in tokenized:
    #     print("p3", t, type(t))
    tokenized = [x for x in tokenized if x]
    # print("TOKENIZING the following")
    # print("this")
    # print(tokenized)
    # print("TOKENIZING results")
    # print(nltk.pos_tag(tokenized))
    pos_tagged = [p[1] for p in nltk.pos_tag(tokenized)]

    lemmatized = [lemmatizer.lemmatize(tokenized[i]) 
                    if not pos_tagged[i].startswith("V") else lemmatizer.lemmatize(tokenized[i], pos='v') 
                    for i in range(len(tokenized))]
    # print(lemmatized)

    conll_lines = ["{}\t{}\t_\t{}\t_\t{}\t{}\t_\t_\t_\t_\t_\t_\t_\tO\n".format(
        i+1, tokenized[i], lemmatized[i], pos_tagged[i], index) for i in range(len(tokenized))]
    elements = [CoNLL09Element(conll_line) for conll_line in conll_lines]

    sentence = Sentence(syn_type=None, elements=elements)
    #print(sentence)
    instance = CoNLL09Example(sentence, elements)

    return instance
