import re

import nltk
import utilities
from nltk.corpus import stopwords
from pycorenlp import StanfordCoreNLP
import json

class relation_miner():
    def __init__(self, stanfordCoreNLP):
        self.stanfordCoreNLP = stanfordCoreNLP

    def getProperText(self, text):
        pattern = re.compile(r'\b(' + r'|'.join(stopwords.words('english')) + r')\b\s*')
        text = pattern.sub('', text)
        #        print(text)
        return text

    def depparse(self, text):
        output = self.stanfordCoreNLP.annotate(text, properties={
            'annotators': 'depparse',
            'outputFormat': 'json'
        })

        parsed = []
        for i in output["sentences"]:
            current_parsed = []
            #        for j in i["basicDependencies"]:
            for j in i["enhancedPlusPlusDependencies"]:
                # exm: 1st sentence> [('ROOT', 'ROOT', 'eat'), ('nsubj', 'eat', 'I'), ('dobj', 'eat', 'chicken'), ('punct', 'eat', '.')]
                # 2nd sentence> [('ROOT', 'ROOT', 'love'), ('nsubj', 'love', 'I'), ('dobj', 'love', 'chicken'), ('punct', 'love', '.')]
                current_parsed.append(tuple((j['dep'], j['governorGloss'], j['dependentGloss'])))
            # parsed example:
            # [
            #   [('ROOT', 'ROOT', 'eat'), ('nsubj', 'eat', 'I'), ('dobj', 'eat', 'chicken'), ('punct', 'eat', '.')],
            #   [('ROOT', 'ROOT', 'love'), ('nsubj', 'love', 'I'), ('dobj', 'love', 'chicken'), ('punct', 'love', '.')]
            # ]
            parsed.append(current_parsed)
        return parsed

    def get_important_relations(self, dep_tree, sentence):
        extracted_words = dict()
        what_bagofwords = set()
        where_bagofwords = set()
        where_attribute_bagofwords = set()
        how_bagofwords = set()
        why_bagofwords = set()
        when_bagofwords = set()
        subject_bagofwords = set()
        action_bagofwords = set()

        for node in dep_tree[0]:
            # print(node)
            self.get_relation(node, 'dobj', what_bagofwords, where_bagofwords)
            # if node[0] == 'dobj':
            #   action_bagofwords.add(verb+" "+obj)

            self.get_relation(node, 'nsubj',
                              what_bagofwords,
                              subject_bagofwords)

            self.get_relation(node, 'nmod:on',
                              what_bagofwords,
                              where_attribute_bagofwords)

            self.get_relation(node, 'nmod:in',
                              where_attribute_bagofwords,
                              where_attribute_bagofwords)

            self.get_relation(node, 'advcl:to',
                              what_bagofwords,
                              why_bagofwords)

            self.get_relation(node, 'amod',
                              when_bagofwords,
                              how_bagofwords)

            self.get_relation(node, 'compound',
                              where_bagofwords,
                              where_bagofwords)

            self.get_relation(node, 'nsubjpass',
                              where_bagofwords,
                              where_bagofwords)

            self.get_relation(node, 'nmod:agent',
                              where_bagofwords,
                              where_bagofwords)
            self.get_relation(node, 'nmod:from',
                              where_bagofwords,
                              where_bagofwords)
            self.get_relation(node, 'nmod:to',
                              where_bagofwords,
                              where_bagofwords)
            self.get_relation(node, 'nmod:with',
                              where_bagofwords,
                              where_bagofwords)
            self.get_relation(node, 'nmod:via',
                              where_bagofwords,
                              where_bagofwords)
            self.get_relation(node, 'nmod:over',
                              where_bagofwords,
                              where_bagofwords)
            self.get_relation(node, 'nmod:for',
                              where_bagofwords,
                              where_bagofwords)
            self.get_relation(node, 'nmod:via',
                              where_bagofwords,
                              where_bagofwords)
            self.get_relation(node, 'nmod:through',
                              where_bagofwords,
                              where_bagofwords)
            self.get_relation(node, 'nmod:using',
                              where_bagofwords,
                              where_bagofwords)
            self.get_relation(node, 'nmod:into',
                              where_bagofwords,
                              where_bagofwords)

        #        what_bafofwords.append(verb)
        #        where_bagofwords.append(obj)
        extracted_words['what'] = utilities.remove_stopwords(what_bagofwords)
        extracted_words['where'] = utilities.remove_stopwords(where_bagofwords)
        extracted_words['where_attribute'] = utilities.remove_stopwords(where_attribute_bagofwords)
        extracted_words['why'] = utilities.remove_stopwords(why_bagofwords)
        extracted_words['when'] = utilities.remove_stopwords(when_bagofwords)
        extracted_words['how'] = utilities.remove_stopwords(how_bagofwords)
        extracted_words['subject'] = utilities.remove_stopwords(subject_bagofwords)
        extracted_words['action'] = utilities.remove_stopwords(action_bagofwords)
        extracted_words['text'] = sentence


        return extracted_words

    def get_relation(self, node, relation_type, *argv):
        #        print(node)
        if node[0] == relation_type:
            k = 1
            for arg in argv:
                #                print(arg)
                arg.add(node[k])
                k += 1
            #                print(arg)
            #            print(node[1], node[2])
            return node[1], node[2]

    def list_important_info(self, text):

        dep_parse_tree = self.depparse(text)
        #        print(dep_parse_tree)
        important_dict = self.get_important_relations(dep_parse_tree, text)
        return important_dict

    def all_imp_stuff(self, text):
        output_list = list()
        for sent in text:
            # print(sent)
            dict_ = self.list_important_info(sent)
            output_list.append(dict_)

        return output_list
