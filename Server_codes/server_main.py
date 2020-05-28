#
# import configuration
# from mapModule import preProcessTool
# from mapModule import seperated_ontology
#
#
# preprocessOntologies = preProcessTool.preProcessTool(isGhaithOntology=configuration.isGhaithOntology)
# configuration.isFile=False
#
# '''
#     Creates the final map for the server.
# '''
# def server_mapping(result, ttp_df):
#     __list__ = list()
#     for mapped_technique in result:
#         text = mapped_technique['text']
#         mapped = mapped_technique['map']
#         for each_mapped in mapped:
#             try:
#                 ttp_id = each_mapped['ttp_id']
#                 if (each_mapped['ttp_score'] >= configuration.BM25_THRESHOLD):
#                     __dict__ = dict()
#                     __dict__['serial'] = '1'
#                     __dict__['subSerial'] = '0'
#                     __dict__['typeOfAction'] = 's'
#                     __dict__['original_sentence'] = text
#                     __temp_dict__ = {'description':'','data':each_mapped['bow']['what'],'link':'','highlight':''}
#                     __dict__['action'] = __temp_dict__
#                     __temp_dict__ = {'description':'','data':each_mapped['bow']['where'],'link':'','highlight':''}
#                     __dict__['object'] = __temp_dict__
#                     __temp_dict__ = {'description':'','data':each_mapped['bow']['why'],'link':'','highlight':''}
#                     __dict__['goal'] = __temp_dict__
#                     __temp_dict__ = {'description':'','data':each_mapped['bow']['when'],'link':'','highlight':''}
#                     __dict__['precondition'] = __temp_dict__
#                     __temp_dict__ = {'description':'','data':each_mapped['bow']['how'],'link':'','highlight':''}
#                     __dict__['api'] = __temp_dict__
#                     __temp_dict__ = {'description':'','data':each_mapped['ttp_id'],'link':'','highlight':''}
#                     __dict__['techId'] = __temp_dict__
#                     __temp_dict__ = {'description':'','data':ttp_df[ttp_id]['TECHNIQUE'],'link':'','highlight':''}
#                     __dict__['technique'] = __temp_dict__
#                     __temp_dict__ = {'description':'','data':ttp_df[ttp_id]['TACTIC'],'link':'','highlight':''}
#                     __dict__['tactic'] = __temp_dict__
#                     __list__.append(__dict__)
#             except:
#                 print('None')
#             print('\n\n')
#     print(__list__)
#     return __list__
#
# def hello():
#
#     temp = str(request.get_data())
#     reportTxt = temp[temp.find('\'') + 1 : temp.rfind('\'') ]
#
#     # print("***********************:  ", reportTxt)
#     result = seperated_ontology(preprocessOntologies, isDependencyParser=configuration.isDependencyParser,isGhaithOntology=configuration.isGhaithOntology, report_name=reportTxt)
#     return {'result':server_mapping(result,preprocessOntologies.ttp_df)}
#
# if __name__ == "__main__":
#     print('___server___')
#     print('___server___')
#     # hello('Malware deletes a file.')
