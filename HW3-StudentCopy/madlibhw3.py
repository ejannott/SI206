# Ethan Jannott
# ejannott
# 22235024

# Using text2 from the nltk book corpa, create your own version of the
# MadLib program.  

# Requirements:
# 1) Only use the first 150 tokens
# 2) Pick 5 parts of speech to prompt for, including nouns
# 3) Replace nouns 15% of the time, everything else 10%

# Deliverables:
# 1) Print the orginal text (150 tokens)
# 1) Print the new text

import nltk
from nltk.book import *
import math
import random

def spaced(word):
	if word in [",", ".", "?", "!", ":"]:
		return word
	else:
		return " " + word

print("START*******")
print('- - - - - - - - - - - - - ORIGINAL TEXT - - - - - - - - - - - - -')
first150words = text2[11:161]
# Mend the words together into a 'paragraph' format
originalText = ' '.join(first150words)
print (originalText)

# Turn original text into tokens
tokens = nltk.word_tokenize(originalText)
print(tokens)

print("\n\nEND*******")
