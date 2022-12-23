import pickle
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from .proc_text import filter_words
#from proc_text import filter_words
from pathlib import Path
from PyPDF2 import PdfReader

def load_corpus(path):
    text = []
    dict_doc_path = {}
    # por ahora el metodo solo devolvera la lista de los documentos leidos
    if os.path.isdir(path):
        doc = 0
        for root, dirs, files in os.walk(path):
            for filename in files:
                with open(os.path.join(root, filename), encoding='utf8', errors='ignore') as f:
                    dict_doc_path[doc] = os.path.join(root, filename)
                    complete_path = os.path.join(root, filename) 
                    complete_path = complete_path.replace('\\','/')
                    text_pdf = read_pdf(complete_path)
                    doc += 1
                    text.append(text_pdf)
    else:
        print("La direccion no es correcta")

    return [text, dict_doc_path]

def charge_corpus():
    BASE_DIR = Path(__file__).resolve().parent.parent.parent
    STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static/documents'),)
    path = STATICFILES_DIRS[0].replace('\\','/')
    text, dic_doc_path = load_corpus(path)
    tfidf = TfidfVectorizer()
    filter_text = []
    count = 0
    for t in text:
        filter_text.append(filter_words(t, False))
        print(count)
        count += 1

    # aqui se guardaa para cada dcoumento la lista de terminos d ese documento #! dicc2
    dict_doc_words = {}
    for i in range(len(filter_text)):
        dict_doc_words[i] = [word for word in filter_text[i].split()]
    result_ = tfidf.fit_transform(filter_text)
    dic_indx_tfidf = result_
    vocabu = tfidf.vocabulary_  # aqui se guarda nombre vs indice #! dicc4
    dic_word_idf = {}  # aqui se guarda para cada palabra su idf asociado #! dicc1
    for ele1, ele2 in zip(tfidf.get_feature_names_out(), tfidf.idf_):
        dic_word_idf[ele1] = ele2
    print("--------------------------------------------------------------aqui")
    with open('dic_indx_tfidf.txt', 'wb') as fh:
        pickle.dump(dic_indx_tfidf, fh)
        fh.close()
    with open('dic_doc_words.txt', 'wb') as fh:
        pickle.dump(dict_doc_words, fh)
        fh.close()
    with open('dic_vocabulary.txt', 'wb') as fh:
        pickle.dump(vocabu, fh)
        fh.close()
    with open('dic_word_idf.txt', 'wb') as fh:
        pickle.dump(dic_word_idf, fh)
        fh.close()
    with open('dic_doc_path.txt', 'wb') as fh:
        pickle.dump(dic_doc_path, fh)
        fh.close()

def read_pdf(path):
    temp = open(path, 'rb')
    PDF_read = PdfReader(temp)
    text = ''
    for x in range(len(PDF_read.pages)):
        first_page = PDF_read.pages[x].extract_text() + " "
        text += first_page
    return text

charge_corpus()