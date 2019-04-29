import os 
import sys
import pprint
from tokenizer import tokenize
file_to_yeet=sys.argv[1]
#tokenize(open(file_to_yeet,'r').read())
pprint.pprint(tokenize(open(file_to_yeet,'r').read()))