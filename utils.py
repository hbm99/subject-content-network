import spacy
import numpy as np
from nltk.corpus import stopwords
from pathlib import Path
import fitz

def pdfs_info_dict(path : str):
    pdf_files = read_pdfs(path)
    pdfs_text_info = {}
    
    pdf_index = 0
    for pdf in pdf_files:
        with fitz.open(pdf) as document:
            words, nouns = preprocess(document)
            pdfs_text_info[pdf_index] = words, nouns
            print("\n\n\n\n\n")
            print(words)
            print("\n\n\n\n\n")
            print(nouns)
            print("\n\n\n\n\n")
            print(f'Finished document {pdf_index}')
        pdf_index+=1
    
    print("Finished")
    return pdfs_text_info

def read_pdfs(path : str):
    # returns all file paths that has .pdf as extension in the specified directory
    pdf_search = Path(path).glob("*.pdf")
    # convert the glob generator out put to list
    # skip this if you are comfortable with generators and pathlib
    return [str(file.absolute()) for file in pdf_search]

def preprocess(document):
    accum_text = ''
    for i in range(document.page_count):
        page = document.load_page(i)
        text = page.get_text('text')
        accum_text += text

    stop_words = set(stopwords.words("spanish"))
    
    nlp = spacy.load('es_core_news_md')

    accum_text = remove_punctuation(accum_text)
    accum_text = remove_apostrophe(accum_text)
    
    spacy_document = nlp(accum_text)
    nouns = []
    words = []
    for token in spacy_document:
        if token.pos_ == "NOUN":
            nouns.append(token.lemma_.lower())
        words.append(token.lemma_.lower())
    
    return [word for word in words if word.casefold() not in stop_words], [noun for noun in nouns]

def remove_punctuation(text):
    unnecessary_symbols = "¡!\"#$%&()*+-./:;<=>¿?@[\]^_`{|}~\n"
    for i in range(len(unnecessary_symbols)):
        text = np.char.replace(text, unnecessary_symbols[i], ' ')
        text = np.char.replace(text, "  ", " ")
        text = np.char.replace(text, '´', '')
    text = np.char.replace(text, ',', '')
    return str(text)

def remove_apostrophe(text):
    return str(np.char.replace(text, "'", ""))