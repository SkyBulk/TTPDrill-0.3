import pandas
import copy

class ReadOntology():

    def __init__(self):
        #        self.temp_refined_ontolog = dict()
        self.mitre_tech_list = list()
        pass

    def read_mitre_TTP(self, file_name = 'resources/mitre_ttp.csv'):
        self.mitre_tech_df = pandas.read_csv(file_name,encoding="ISO-8859-1")
        self.mitre_tech_list = self.mitre_tech_df.to_dict('records')
        self.mitre_tech_dict = dict()
        for mitre_tech in self.mitre_tech_list:
            try:
                tactic = self.mitre_tech_dict[mitre_tech['ID']]['TACTIC'] + ','
            except:
                tactic = ''
            self.mitre_tech_dict[mitre_tech['ID'].lower()] = {'TECHNIQUE':mitre_tech['TECHNIQUE'],'TACTIC':tactic + mitre_tech['TACTIC']}
        return self.mitre_tech_dict

    def read_csv(self, file_name):
        if file_name is None:
            self.data_frame = pandas.read_csv('resources/ontology_details.csv', encoding="ISO-8859-1")
        else:
            self.data_frame = pandas.read_csv(file_name, encoding="ISO-8859-1")
        self.data_frame = self.data_frame.fillna(0)
        return self.data_frame

    def split_ontology(self, ontology_list, split_char):

        refined_ontology_list = list()
        for each_row in ontology_list:
            print(each_row)
            action_what = each_row['action_what']
            #    print(type(action_what))
            action_where = each_row['action_where']
            if type(action_what) != type(0) and type(action_where) != type(0):
                #        print(action_what)
                what_list = action_what.split(split_char)
                where_list = action_where.split(split_char)
                for each_what in what_list:
                    for each_where in where_list:
                        new_entry = copy.deepcopy(each_row)
                        new_entry['action_what'] = each_what.strip()
                        new_entry['action_where'] = each_where.strip()

                        refined_ontology_list.append(new_entry)
        return refined_ontology_list

    """
        This method takes a list of string and returns a list of string without '/', ',', '-'
    """
    def replace_string(self, list_string):
        return_list = list()
        if type(list_string) != type(0) and type(list_string) != type(0.0):
            temp = list_string.replace('/', ',')
            temp = temp.replace('-', ' ')
            return_list = [word.strip() for word in temp.split(',')]
        return return_list


    def split_ontology_list(self, ontology_list):
        refined_ontology_list = list()
        for each_row in ontology_list:
            # __action_what_list = self.replace_string(each_row['action_what'])
            # __action_where_list = self.replace_string(each_row['action_where'])
            # __why_what_list = self.replace_string(each_row['why_what'])
            # __why_where_list = self.replace_string(each_row['why_where'])
            each_row['action_what'] = self.replace_string(each_row['action_what'])
            each_row['action_where'] = self.replace_string(each_row['action_where'])
            each_row['why_what'] = self.replace_string(each_row['why_what'])
            each_row['why_where'] = self.replace_string(each_row['why_where'])
            each_row['how_what'] = self.replace_string(each_row['how_what'])
            each_row['how_where'] = self.replace_string(each_row['how_where'])

        return ontology_list



    def refine_ontology(self):
        ontology_dict = self.data_frame.to_dict('records')
        temp = self.split_ontology(ontology_dict, '/')
        temp_refined_ontology = self.split_ontology(temp, ',')
        self.temp_refined_ontology = temp_refined_ontology
        return temp_refined_ontology

    def print_ontology(self, data_frame):
        if data_frame is None:
            for __ in self.temp_refined_ontology:
                #    if __['_2'] == '212':
                print(__['Id'], ',', __['action_what'], ',', __['action_where'])
        else:
            for __ in data_frame:
                #    if __['_2'] == '212':
                print(__['Id'], ',', __['action_what'], ',', __['action_where'])

    def write_ontology(self, file_name, data_frame):
        if data_frame is None:
            data_frame = pandas.DataFrame(self.temp_refined_ontology)
        if file_name is not None:
            data_frame.to_csv(r'resources/export_dataframe_1.csv', index=None, header=True)
        else:
            data_frame.to_csv(file_name, index=None, header=True)

    def stem(self, ontology_list):
        from nltk.stem import PorterStemmer
        from nltk.tokenize import word_tokenize
        import copy
        ps = PorterStemmer()
        stem_list = list()

        for single_dict in ontology_list:
            temp_dict = dict()
            for key, val in single_dict.items():
                try:
                    temp_dict[key] = ps.stem(val)
                except:
                    temp_dict[key] = val
            stem_list.append(temp_dict)
        return stem_list

import re
import pandas
from nltk.stem import WordNetLemmatizer, PorterStemmer
class ParseGhaithOntology():

    def __init__(self,isStemmer):
        self.isStemmer = isStemmer
        pass
    def read_csv(self,file_name='resources/ontology_ghaith.csv'):
        data_frame = pandas.read_csv(file_name, encoding="ISO-8859-1")
        data_frame = data_frame.fillna('0')
        data_frame_dict = data_frame.to_dict('records')
        return  data_frame_dict
    def parse_ontology(self, data_frame_dict):
        stemmer = PorterStemmer()
        lemmnizer = WordNetLemmatizer()
        ontology_list = list()
        ontology_dict_map = dict()
        for dict_entry in enumerate(data_frame_dict):
            temp_list = list()
            for key, val in dict_entry[1].items():
                try:
                    if key == 'CODE':
                        ontology_dict_map[dict_entry[0]] = re.search("T\d*", val).group().lower()
                    if key == 'NAME':
                        list_of_word = val.strip().split(' ')
                        for each_word in list_of_word:
                            if self.isStemmer:
                                temp_list.append(stemmer.stem(each_word))
                            else:
                                temp_list.append(lemmnizer.lemmatize(each_word))
                except:
                    break

            ontology_list.append(temp_list)
        return ontology_list, ontology_dict_map

def read_ghaith_ontology():
    from ontology_reader import ParseGhaithOntology
    ontology = ParseGhaithOntology(True)
    ontology_dict = ontology.read_csv()
    what_list, list_map_dict = ontology.parse_ontology(ontology_dict)
    mapped_list = zip(list_map_dict.values(), what_list)
    data_frame = pandas.DataFrame(mapped_list)
    data_frame.to_csv(r'resources/ghaith_onto.csv', index=None, header=True)

def split_1(ontology_dict):
    list_ = list()
    for __each__entry__ in ontology_dict:
        what_list = __each__entry__['action_what'].split(',')
        list_.append([ __each__entry__['Id'],__each__entry__['action_what'].split('/'),__each__entry__['action_where']])


    for __each__ in list_:
        print(__each__)

if __name__=='__main__':
    # read_ghaith_ontology()
    file_name = 'resources/ParsedMitreTechnique_V5_Ruhani.csv'
    # file_name = 'resources/export_dataframe.csv'
    # file_name = 'resources/ontology_details.csv'
    ontology = ReadOntology()
    ontology_df = ontology.read_csv(file_name)
    # print(ontology_df.head())
    ontology_dict = ontology.data_frame.to_dict('records')
    print(ontology_dict)
    split_1(ontology_dict)
    # ontology_dict = ontology.split_ontology_list(ontology_dict)
    # print(ontology_dict)
    # stem_list = ontology.stem()
    # # for ont  in stem_list:
    # #     print(ont['action_what'])
    # ontology.print_ontology(stem_list)
    # from ontology_reader import ReadOntology
    #
    # file_name = 'resources/ontology_details.csv'
    # ontology = ReadOntology()
    # ontology_df = ontology.read_csv(file_name)
    # ontology_df
    # ontology_dict = ontology.data_frame.to_dict('records')
    # ontology_dict
    # __ = ontology.split_ontology_list(ontology_dict)
    # print(__)
    # stem_list = ontology.stem(__)
    # for _ in stem_list:
    #    print(_['Id'], _['action_what'], _['action_where'])
    #    print(_['Id'], _['why_what'], _['why_where'])
    # what_list = list()
    # for i in stem_list:
    #     what_list.append([i['Id'], i['action_what'], i['action_where'], i['why_what'], i['why_where']])
    # print(what_list[0])
    # ttp_df = ontology.read_mitre_TTP()
    # for key, val in ttp_df.items():
    #     print(key, val['TECHNIQUE'] )
    # print(ttp_df)