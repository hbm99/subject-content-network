import fitz
from utils import preprocess, read_pdfs


if __name__ == '__main__':
    
    pdf_files = read_pdfs("pdfs/")
    pdfs_text_info = {}
    
    pdf_index = 0
    for pdf in pdf_files:
        with fitz.open(pdf) as document:
            words, nouns = preprocess(document)
            pdfs_text_info[pdf_index] = words, nouns
            print(f'Finished document {pdf_index}')
            print("\n\n\n\n\n")
            print(words)
            print("\n\n\n\n\n")
            print(nouns)
            print("\n\n\n\n\n")
        pdf_index+=1
    
    print("Finished")
    
    
    
    
    