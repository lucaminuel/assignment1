"""Give you the frequence occurence of each letter of a text \
   and print the histogram
"""

import os
import logging
import time
import argparse

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
    os.path.join(path)
    with open(path, encoding="utf8") as file_:
        book=file_.read()
    logger.info('File opened: there are {len(book)} characters!')

    #Creat dictionary to handle characters frequents
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    freq_letter = {}
    for letter in alphabet:
        freq_letter[letter] = 0

    #For loop: at each occurence increase letter counting by one
    logger.info('Counting...')
    for letter in book.lower():
        if letter in alphabet:
            freq_letter[letter] += 1
    logger.info('Counting done!')

    #Normalise frequence at 1
    logger.info('Normalising...')
    ch_total = float(sum(freq_letter.values()))
    for letter in alphabet:
        freq_letter[letter] = freq_letter[letter] * 100
        freq_letter[letter] /= ch_total
    logger.info('Done!')

    #Print occurence
    print('Frequence:')
    for letter, freq in freq_letter.items():
        print(f'{letter}: {freq: .3f}%')

    #Make Histogram
    logger.info('Done!')
    plt.bar(freq_letter.keys(), freq_letter.values(), color='b')
    plt.title('Histogram of the frequences')
    plt.ylabel('% occurence"')
    plt.show()

    #Printing Elapsed time
    print(f"Elapsed time: {time.time()-start_time} seconds")

#Setting argparse to read file path name from command line
parser = argparse.ArgumentParser()
parser.add_argument('path', help='Write the correct path of the text that you want \
                                  to analyze')
args = parser.parse_args()
count(args.path)