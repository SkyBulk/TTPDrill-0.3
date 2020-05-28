# import configuration
# import re, nltk, json, os
# from nltk.corpus import stopwords
#
# def read_file(file_name):
#     with open(file_name, 'r', encoding="utf8") as report:
#         text = report.read()
#     return text
#
# def remove_stopwords(word_tekens):
#     from nltk.corpus import stopwords
#     stop_words = stopwords.words('english')
#     stop_words.append('-')
#     stop_words.append('some')
#     stop_words = set(stop_words)
#     filtered_sentence = [w for w in word_tekens if not w in stop_words]
#     return filtered_sentence
#
# def remove_stopwords_from_sentence(sentence):
#     from nltk.corpus import stopwords
#     stop_words = stopwords.words('english')
#     stop_words.append('-')
#     stop_words.append('some')
#     stop_words = set(stop_words)
#     text = ' '.join([word for word in sentence.split() if word not in stop_words])
#     return text
#
# def lemmatize_and_stem(single_word, isLmmatize, isStem):
#     lem_output = single_word
#     if isLmmatize:
#         lem_output = configuration.lemmatizer.lemmatize(single_word)
#     stem_output = lem_output
#     if isStem or single_word.endswith('ing') or single_word.endswith('ed') or single_word.endswith('s'):
#         stem_output = configuration.stemmer.stem(lem_output)
#     return stem_output
#
# class FileReader():
#     def __init__(self, file_name):
#         self.file_name = file_name
#
#     def read_file(self):
#         with open(self.file_name,'r', encoding="utf8") as report:
#             strs = report.read()
#         self.text = strs
#         # print(strs)
#         return strs
#
#     def print_sentence(self, sent_list):
#         for sent in enumerate(sent_list):
#             print('Sentence ',sent[0],':',sent[1])
#         return
#
#     def get_all_sentences(self, text):
#         sentence_tokenize_list = list()
#         paragraphs = text.split('\n')
#         for paragraph in paragraphs:
#             sent_tokenize = nltk.sent_tokenize(paragraph)
#             for sentence in sent_tokenize:
#                 sentence_tokenize_list.append(sentence)
#         return sentence_tokenize_list
#
#     # # Return the valid senteces only, Do not consider the topic sentence
#     def get_all_valid_sentences(self, text):
#         sentence_tokenize_list = list()
#         paragraphs = text.split('\n')
#         for paragraph in paragraphs:
#             sent_tokenize = nltk.sent_tokenize(paragraph)
#             for sentence in sent_tokenize:
#                 print(sentence)
#                 ###
#                 # if len(sentence) == sentence.rfind('.') + 1:
#                     # sentence = self.remove_fullstop(sentence)
#                 sentence = self.remove_filepath(sentence)
#                 sentence_tokenize_list.append(sentence)
#         return sentence_tokenize_list
#
#     def get_sent_tokenize(self, text):
#         sentence_tokenize_list = list()
#         sent_tokenize = nltk.sent_tokenize(text)
#         for sentence in sent_tokenize:
#             ###
#             if len(sentence) == sentence.rfind('.') + 1:
#                 # sentence = self.remove_fullstop(sentence)
#                 sentence = self.remove_filepath(sentence)
#                 sentence_tokenize_list.append(sentence)
#         return sentence_tokenize_list
#
#
#     def remove_fullstop(self, text):
#         """This method removes the fullstop in the middle of a sentence eg. 'services.exe' changes to 'servicesexe'."""
#         """
#         :parameter text str
#         :return str
#         """
#         result_string = text.replace('.','',text.count('.')-1)
#         return result_string
#
#     # def remove_filepath(self, text):
#     #     x = re.findall(r"([a-zA-Z]:[\\\\[a-zA-Z0-9]*]*)", text)
#     #
#     #     for _ in x:
#     #         text = text.replace(_,'file path',1)
#     #     x = re.findall(r'(\/.*?\.[\w:]+)',text)
#     #     for _ in x:
#     #         text = text.replace(_,'file path',1)
#     #     return text
#
#     def remove_filepath(self, text):
#         # r'((((? < !\w)[A - Z, a - z]:) | (\.{1, 2}\\))([ ^\b % \ / \ |:\n\"]*))|(\"\2([^%\/\|:\n\"]*)\")|((?<!\w)(\.{1,2})?(?<!\/)(\/((\\\b)|[^ \b%\|:\n\"\\\/])+)+\/?)|(%([a-zA-Z]+)%)\\((?:[a-zA-Z0-9() ]*\\)*).*'
#         pattern = re.compile(r"((((?<!\w)[A-Z,a-z]:)|(\.{1,2}\\))([^\b%\/\|:\n\"]*))|(\"\2([^%\/\|:\n\"]*)\")|((?<!\w)(\.{1,2})?(?<!\/)(\/((\\\b)|[^ \b%\|:\n\"\\\/])+)+\/?)|(%([a-zA-Z]+)%)\\((?:[a-zA-Z0-9() ]*\\)*).*")
#         cleantext = re.sub(pattern, 'directory', str(text))
#         pattern = re.compile(r'([a-zA-Z]:[\\\\[a-zA-Z0-9]*]*)')
#         cleantext = re.sub(pattern, ' ', str(cleantext))
#         pattern = re.compile(r'(\/.*?\.[\w:]+)')
#         cleantext = re.sub(pattern, ' ', str(cleantext))
#         pattern = re.compile(r'“')
#         cleantext = re.sub(pattern, ' ', str(cleantext))
#         pattern = re.compile(r'”')
#         cleantext = re.sub(pattern, ' ', str(cleantext))
#         pattern = re.compile(r'\((.*?)\)')
#         cleantext = re.sub(pattern, ' ', str(cleantext))
#         pattern = re.compile(r'(\w+\\\w+(\\)?)')
#         cleantext = re.sub(pattern, ' ', str(cleantext))
#         # File Extension .exe|.zip
#         pattern = re.compile(r'(\.[a-z]{3})')
#         cleantext = re.sub(pattern, ' ', str(cleantext))
#         # [12] remove
#         pattern = re.compile(r'(\[\d+\])')
#         cleantext = re.sub(pattern, ' ', str(cleantext))
#         # IP Address, Port
#         pattern = re.compile(r'([0-9]{1,3}\.){3}[0-9]{1,3}\:[0-9]{2,5}|([0-9]{1,3}\.){3}[0-9]{1,3}')
#         text = re.sub(pattern, ' ip address ', str(cleantext))
#
#         # text = text.replace('.','',text.count('.')-1)
#
#         return str(text.strip())
#
#     def symantec_sent_tokenize(self, text):
#         sentence_tokenize_list = list()
#         paragraphs = text.split('\n')
#         for paragraph in paragraphs:
#             sent_tokenize = nltk.sent_tokenize(paragraph)
#             for sentence in sent_tokenize:
#                 ###
#                 # if len(sentence) == sentence.rfind('.') + 1:
#                     # sentence = self.remove_fullstop(sentence)
#                     # sentence = self.remove_filepath(sentence)
#                 sentence_tokenize_list.append(sentence)
#         return sentence_tokenize_list
#
#
#
#
# def regex_checker():
#     reader = FileReader('reports/test.txt')
#     # text = 'Monitor for registry key creation and/or modification events for the keys of  HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\AppCompatFlags\Custom  and  HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\AppCompatFlags\InstalledSDB'
#     import re
#     # pattern = re.compile(r'(\w+\\\w+(\\)?)')
#     # result = re.sub(pattern=pattern, repl='', string=text)
#     # print(result)
#     text = reader.read_file()
#     text = reader.remove_filepath(text)
#     print(text)
#
# def get_verb_list(filename='ontology/verb_list.txt'):
#     with open(filename, 'r') as file:
#         verb_lists = file.read()
#     verb_lists = verb_lists.split('\n')
#     # configuration.stemmer.stem(verb)
#     verbs_dictionary = dict()
#     for verbs in verb_lists:
#         verbs_dictionary[configuration.stemmer.stem(verbs)] = verbs
#     verb_lists = [configuration.stemmer.stem(verb) for verb in verb_lists]
#     return verb_lists, verbs_dictionary
#
# def is_action_verb(verb_lists, verb):
#     if verb in verb_lists:
#         return True
#     return False
#
#
# if __name__=='__main__':
#     print(configuration.JAVA_HOME)
#     # regex_checker()
#     # pass