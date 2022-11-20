import fitz
from utils import preprocess


if __name__ == '__main__':
    document = fitz.open("pdfs/Conferencia-00-MN-CC-2021-(con-imagenes).pdf")
    
    words, nouns = preprocess(document)
    
    print(words)
    
    print("\n\n\n\n\n")
    
    print(nouns)
    