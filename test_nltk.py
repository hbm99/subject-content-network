#import nltk
#nltk.download('punkt')
#nltk.download("stopwords")
#nltk.download('wordnet')

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


#from nltk.stem import WordNetLemmatizer #for english
# lemmatizer = WordNetLemmatizer()
# print(lemmatizer.lemmatize("scarves"))

stop_words = set(stopwords.words("spanish"))
#print(stop_words)

quote = "Su temperatura corporal es alta, muy caliente"
quote = "La cabeza mía es grande y muy gorda, límites laterales"
words_in_quote = word_tokenize(quote)

filtered_list = [word for word in words_in_quote if word.casefold() not in stop_words]
#print(filtered_list)


import spacy

nlp = spacy.load('es_core_news_md')

spacy_document = nlp(quote)
spacy_words_list = []
for token in spacy_document:
    spacy_words_list.append(token.lemma_.lower())
    
filtered_spacy_list = [word for word in spacy_words_list if word.casefold() not in stop_words]

print(filtered_spacy_list)
    
# pendiente a partir de Chunking

