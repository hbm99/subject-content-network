import fitz
import spacy
from nltk.corpus import stopwords

doc = fitz.open("pdfs/Conferencia-00-MN-CC-2021-(con-imagenes).pdf")

accum_text = ''
for i in range(doc.page_count):
    page = doc.load_page(i)
    text = page.get_text('text')
    accum_text += text
    
stop_words = set(stopwords.words("spanish"))

nlp = spacy.load('es_core_news_md')

spacy_document = nlp(accum_text)
spacy_words_list = []
for token in spacy_document:
    if token.pos_ == "NOUN":
        spacy_words_list.append(token.lemma_.lower())
    
filtered_spacy_list = [word for word in spacy_words_list if word.casefold() not in stop_words]

print(filtered_spacy_list)