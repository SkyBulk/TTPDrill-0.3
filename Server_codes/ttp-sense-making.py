# from flask import Flask, request
# app = Flask(__name__)
#
# from utilities import FileReader, StanfordServer
# from relation_miner import relation_miner
# from ontology_reader import ReadOntology
# from BM25 import BM25, BM25L, BM25Okapi, BM25Plus
# import json
#
# def getGhaithOntology(isStemmer):
#     from ontology_reader import ParseGhaithOntology
#     ontology = ParseGhaithOntology(isStemmer)
#     ontology_dict = ontology.read_csv()
#     what_list, list_map_dict = ontology.parse_ontology(ontology_dict)
#     ontology = ReadOntology()
#     ttp_df = ontology.read_mitre_TTP()
#     return what_list, list_map_dict, ttp_df
#
# def getOntology(isStemmer):
#     from ontology_reader import ReadOntology
#     file_name = 'resources/ontology_details.csv'
#     ontology = ReadOntology()
#     ontology_df = ontology.read_csv(file_name)
#     ontology_dict = ontology.data_frame.to_dict('records')
#     __ = ontology.split_ontology_list(ontology_dict)
#     what_list = list()
#     for i in __:
#
#         what_list.append([i['Id'], i['action_what'], i['action_where'], i['why_what'], i['why_where']])
# #    print(what_list[0])
#     what_list, list_map_dict = combine_parsed_ontology_in_bow(what_list,isStemmer)
#     ttp_df = ontology.read_mitre_TTP()
#     # for key, val in ttp_df.items():
#     #     print(key, val['TECHNIQUE'] )
#     # print(ttp_df)
#
#
#
#     # file_name = 'resources/ontology_details_1.csv'
#     # file_name = 'resources/ontology_details.csv'
#     # file_name = 'resources/export_dataframe.csv'
#     # ontology = ReadOntology()
#     # ontology_df = ontology.read_csv(file_name)
#     # ontology_dict = ontology.refine_ontology()
#     # stem_list = ontology.stem()
#     # # for ont  in stem_list:
#     # #     print(ont['action_what'])
#     # ontology.print_ontology(stem_list)
#     #
#     #
#     #
#     # what_list = list()
#     # for i in stem_list:
#     #     what_list.append([i['Id'], i['action_what'], i['action_where']])
#     # #what_list[0]
#
#     return what_list, list_map_dict, ttp_df
#
# def combine_parsed_ontology_in_bow(what_list, isStemmer):
#     list_map_dict = dict()
#     new_list = list()
#     for index in enumerate(what_list):
#         # print(tuples)
#         a = list()
#         for attribute in index[1]:
#             if type(attribute) is str:
#                 a.append(attribute.strip())
#             elif type(attribute) is list:
#                 for each_sttribute in attribute:
#                     for each_word in each_sttribute.split(' '):
#                         if isStemmer:
#                             a.append(stemmer.stem(each_word.strip()))
#                         else:
#                             a.append(lemmatizer.lemmatize(each_word.strip()))
#         a = utilities.remove_stopwords(a)
#         list_map_dict[index[0]] = a[0]
#         new_list.append(a[1:])
#
#     return new_list, list_map_dict
#
# def stanfordServerStart(isServerRestart):
#     stanfordServer = StanfordServer()
#     try:
#         if isServerRestart:
#             stanfordServer.startServer()
#     except:
#         print('Error in stanford nlp')
#     stanfordNLP = stanfordServer.get_stanforcorenlp()
#     return stanfordNLP
#
# def getReportExtraction(isFile,isStemmer, stanfordNLP, file_name = 'reports/fireeye_fin7_application_shimming.txt'):
#     # print("file: ", file_name)
# #    file_name = 'reports/fireeye_fin7_application_shimming.txt'
#
#
#     preprocess_tools = FileReader(file_name)
#     # text_list = list of str, contains valid sentences with no fullstop or file path with them
#     if isFile:
#         text = preprocess_tools.read_file()
#         text = text.replace('\n',' ')
#         text_list = preprocess_tools.get_sent_tokenize(text)
#     else:
#         text = file_name
#         text_list = preprocess_tools.get_sent_tokenize(text)
#     # print(text_list)
#
#     r_miner = relation_miner(stanfordNLP)
#     extracted_infor_list = r_miner.all_imp_stuff(text_list)
#     extracted_list = get_all(extracted_infor_list, isStemmer)
#
#     return extracted_list
#
# def get_all(temp_list, isStemmer):
#     all_list = list()
#     for temp_dict in temp_list:
#         all_dict = dict()
#         tt_list = list()
#         for key, val in temp_dict.items():
#             if key == 'what' or key == 'where' or key == 'where_attribute' or key == 'why' or key == 'when' or key == 'how' or key == 'subject':
#                 for __ in val:
#                     if isStemmer:
#                         tt_list.append(stemmer.stem(__))
#                     else:
#                         tt_list.append(lemmatizer.lemmatize(__))
#         all_dict['text'] = temp_dict['text']
#         all_dict['bow'] = tt_list
#         all_list.append(all_dict)
#     return all_list
#
# from nltk.stem import WordNetLemmatizer, PorterStemmer
# from nltk.tokenize import sent_tokenize, word_tokenize
#
# lemmatizer = WordNetLemmatizer()
# stemmer = PorterStemmer()
# import utilities
#
# def buildBM25(what_list):
#     '''
#     :param what_list:
#     :return:
#     '''
#     """
#     Example of using BM25
#     """
#     # corpus = [
#     #     "Hello there good man!",
#     #     "It is quite dry in London",
#     #     "How is the weather today?",
#     #     "Hello Ruhani, How was your trip to London",
#     #     "Did the weather in London is windy?"
#     # ]
#     # corpus = [
#     #     "use scanner","inject","copy","delete","file","use"
#     # ]
#
#     # tokenized_corpus = [word_tokenize(doc) for doc in corpus]
#     # #tokenized_corpus = [doc.split(" ") for doc in corpus]
#     # tokenized_stemmed_corpus = list()
#     # for doc in tokenized_corpus:
#     #     doc_stemmed = list()
#     #     for word in doc:
#     #         doc_stemmed.append(stemmer.stem(word))
#     #     tokenized_stemmed_corpus.append(doc_stemmed)
#
#     # tokenized_corpus = [word_tokenize(doc) for doc in what_list]
#     # print(tokenized_stemmed_corpus)
#     bm25 = BM25Okapi(what_list)
#     return bm25
#
# def query(extracted_list, ontology_list, list_map, bm25_model, ttp_df, isStemmer):
#     final = {}
#     __list__ = list()
#     # print('-------------****---------------')
#     # print(extracted_list)
#     for __ in extracted_list:
#         # print(__['bow'])
#         if isStemmer:
#             tokenized_query = [stemmer.stem(word) for word in __['bow']]
#         else:
#             tokenized_query = [lemmatizer.lemmatize(word) for word in __['bow']]
#
#         #    print(tokenized_query)
#         doc_scores = bm25_model.get_scores(tokenized_query)
#         #    print(doc_scores)
#
#         print('Text:\n', __['text'], '\n')
#         print('Extracted Information:\n', __['bow'], '\n')
#         print('Mapped:\n')
# #        scores = bm25_model.get_scores(tokenized_query)
#         top_index, match_ttp, score = bm25_model.get_top_n(tokenized_query, ontology_list, n=5)
#         create_ttp_map(__, list_map, ttp_df, top_index, match_ttp, score, __list__)
#         # for ___ in zip(top_index, match_ttp, score):
#         #     try:
#         #         ttp_index = ___[0]
#         #         ttp_id = list_map[___[0]]
#         #         ttp_technique = ttp_df[ttp_id]['TECHNIQUE']
#         #         ttp_tactic = ttp_df[ttp_id]['TACTIC']
#         #         ttp_ontology = ___[1]
#         #         ttp_score = ___[2]
#         #         # ___[2] == score
#         #         # ___[1] == match_ttp
#         #         if (ttp_score > 0.1):
#         #             print(ttp_index, ' : ', ttp_score, ' : ', ttp_id, ' : ', ttp_technique, ' : ', ttp_tactic, ' : ', ttp_ontology)
#         #     except:
#         #         print('None')
#         # print('\n\n')
#     final['a'] = 'a'
#     final['b'] = __list__
#     print(final)
#
#     return final
#
# def create_ttp_map(text_dict, list_map, ttp_df, top_index, match_ttp, score, __list__):
#     for ___ in zip(top_index, match_ttp, score):
#         try:
#             ttp_index = ___[0]
#             ttp_id = list_map[___[0]]
#             ttp_technique = ttp_df[ttp_id]['TECHNIQUE']
#             ttp_tactic = ttp_df[ttp_id]['TACTIC']
#             ttp_ontology = ___[1]
#             ttp_score = ___[2]
#             if (ttp_score > 0.1):
#
#                 __dict__ = dict()
#                 __dict__['serial'] = '1'
#                 __dict__['subSerial'] = '0'
#                 __dict__['typeOfAction'] = 's'
#                 __dict__['original_sentence'] = text_dict['text']
#                 __temp_dict__ = {'description':'','data':text_dict['bow'],'link':'','highlight':''}
#                 __dict__['action'] = __temp_dict__
#                 __temp_dict__ = {'description':'','data':ttp_id,'link':'','highlight':''}
#                 __dict__['techId'] = __temp_dict__
#                 __temp_dict__ = {'description':'','data':ttp_technique + '  (' + str(ttp_score) + ')','link':'','highlight':''}
#                 __dict__['technique'] = __temp_dict__
#                 __temp_dict__ = {'description':'','data':ttp_tactic,'link':'','highlight':''}
#                 __dict__['tactic'] = __temp_dict__
#
#
#                 __list__.append(__dict__)
#                 # print(__list__)
#         except:
#             print('None')
#     # print('\n\n')
#     # print(__list__)
#     return
#
#
# def read_API_doc():
#     import pandas
#     api_data_frame = pandas.read_csv('resources/API_Description_MSDN.csv', encoding="ISO-8859-1")
#     return api_data_frame.to_dict('records')
#
# # if __name__=='__main__':
# @app.route("/", methods=["POST"])
# def hello():
#     serverStart = False
#     isAPI = False
#     stanfordServer = StanfordServer()
#     try:
#         stanfordNLP = stanfordServer.get_stanforcorenlp()
#     except:
#         print('No Stanford NLP Server.')
#         stanfordNLP = stanfordServerStart(serverStart)
#
#     # temp = str(request.get_data())
#     # reportTxt = temp[temp.find('\'') + 1 : temp.rfind('\'')]
#
#     json_data = json.loads(request.data)
#     outputFormat = json_data['output']
#     reportTxt = json_data['value']
#
#     print("***********************:  ", reportTxt)
#
#     # print("***********************:  ", reportTxt)
#
#
#     """----------------------------------------------------------------------------------------"""
#     ### Building Ontology
#     isStemmer = True
#     what_list, list_map, ttp_df = getOntology(isStemmer)
#     # what_list, list_map, ttp_df = getGhaithOntology(isStemmer)
#     bm25_model = buildBM25(what_list)
#     """-----------------------------------------------------------------------------------------"""
#
#
#
#
#     if isAPI:
#         api_dict_list = read_API_doc()
#         print("----------------------------------------------------------------------------------------")
#         for api in api_dict_list:
#             # for key, val in api.items():
#             print("-----------------------------------" + api['API_NAME'] + "-----------------------------------")
#             print('API_NAME: ', api['API_NAME'])
#             print('API_Description: ', api['API_Description'])
#             extracted_list = getReportExtraction(False, isStemmer, False,  api['API_Description'])
#             query(extracted_list, what_list, list_map, bm25_model, ttp_df, isStemmer)
#
#             print("-----------------------------------" + api['API_NAME'] + "-----------------------------------\n\n")
#
#     else:
#
#         isFile = False
#
#         #while(True):
#         if isFile:
#             report_name = 'scrapper/only_description/Trojan.Mdrop.BWJ.2008-102219-5606-99.txt'
#             # report_name = 'C:\\Users\\rrahman3\\Google Drive\\Study UNCC\\TTPDrill Handover\\Raw Threat Reports\\ThreatReport\\relevent\\Infostealer.Alina_ThreatReport.txt'
#             # report_name = 'C:\\Users\\rrahman3\\Google Drive\\Study UNCC\\TTPDrill Handover\\Raw Threat Reports\\ThreatReport\\ghaith\\tested_output\\Trojan.Downexec.B_ThreatReport.txt'
#
#         else:
#             report_name = reportTxt #input("Enter Text:\t")
#         extracted_list = getReportExtraction(isFile,isStemmer, stanfordNLP, report_name)
#         # print(what_list)
#         return query(extracted_list,what_list,list_map, bm25_model, ttp_df,isStemmer)
#
# if __name__ == "__main__":
#     serverStart = True
#     stanfordServerStart(serverStart)
#     app.run()
#     # hello('Malware deletes file.')
