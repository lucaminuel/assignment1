import os
import argparse
import logging
import time
import matplotlib.pyplot as plt

start_time = time.time()

#I had some problem with logging text, I solved it in this way, but I don't know why
logger = logging.getLogger('Info')
logger.setLevel(logging.INFO)



def count (path):
    """Main function open the file from the path and count the characters
    """
    #Open file, I had to put encoding='utf8 to not have any problems in
    #decoding characters
    logger.info('Opening file...')
    with open(path, encoding="utf8") as f:
        book=f.read()
    logger.info(f'File opened: there are {len(book)} characters!')

   #Convert text in lower case
    logger.info('Converting the book...')
    for line in book:
        book=book.lower()
    logger.info('Book converted!')

    #Creat dictionary to handle characters frequents
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    freq_letter = {}
    for ch in alphabet:
        freq_letter[ch] = 0

    #For loop: at each occurence increase letter counting by one
    logger.info('Counting...')
    for ch in book:
        if ch in alphabet:
            freq_letter[ch] += 1
    logger.info('Counting done!')

    #Normalise frequence at 1
    logger.info('Normalising...')
    ch_total = float(sum(freq_letter.values()))
    for ch in alphabet:
        freq_letter[ch] = freq_letter[ch] * 100
        freq_letter[ch] /= ch_total
    logger.info('Done!')

    #Print occurence
    print('Frequence:')
    for ch, freq in freq_letter.items():
        print(f'{ch}: {freq: .3f}%')

    #Make Histogram
    logger.info('Done!')
    plt.bar(freq_letter.keys(), freq_letter.values(), color='b')
    plt.title("Histogram of the frequences")
    plt.ylabel("% occurence")
    plt.show()

    #Printing Elapsed time
    print(f"Elapsed time: {time.time()-start_time} seconds")

#Paste correct path of the file .txt
path= os.path.join('ciao.txt')
count(path)