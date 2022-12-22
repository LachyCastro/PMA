import pickle
from collections import Counter
from .ranking import order_ranking, cal_ranking
from .proc_query import calc_tf_query, calc_weight_query, get_query_input_v
from .load import charge_corpus

def vectorial_model(query,load_c):
    if not load_c:
        charge_corpus()
    splited_query = query.split()
    procesed_query = get_query_input_v(splited_query)

    pickle_1 = open('dic_vocabulary.txt', 'rb')
    vocabu = pickle.load(pickle_1)
    pickle_2 = open('dic_word_idf.txt', 'rb')
    dic_word_idf = pickle.load(pickle_2)
    pickle_3 = open('dic_indx_tfidf.txt', 'rb')
    dic_indx_tfidf = pickle.load(pickle_3)
    pickle_4 = open('dic_doc_words.txt', 'rb')
    dic_doc_words = pickle.load(pickle_4)
    pickle_5 = open('dic_doc_path.txt', 'rb')
    dic_doc_patch = pickle.load(pickle_5)
    counter_dict = Counter(procesed_query)
    tf_query = calc_tf_query(counter_dict, procesed_query)
    query_weight = calc_weight_query(
        procesed_query, tf_query, dic_word_idf)
    rank = cal_ranking(dic_doc_words, vocabu, query_weight,
                       dic_indx_tfidf, procesed_query)
    orded_rank = order_ranking(rank, dic_doc_patch)
    return orded_rank