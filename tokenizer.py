import os
import sys
import re 
#todo remove multiline comments
regex_pat=re.compile('\w')
def tokenize(text):
    tokenized_dirty=tokenize_line_by_line(text)
    return tokenized_dirty#clean_token_table(tokenized_dirty)

def clean_token_table(dirty_table):
    for line in dirty_table:
        for symbol in line:
            print(symbol)

def clean_symbols_from_statement(statment):
    ss=regex_pat.findall(statment)
    return ''.join(i for i in ss)

def clean_comments(line):
    return line.split("//")[0]
    
def tokenize_line_by_line(text):
    line_line=text.split("\n")
    file_tokenized=[]
    for line in line_line:
        file_tokenized.append(tokenize_line(clean_comments(line)))
    return file_tokenized

def tokenize_line(line):
    line=[line]
    line_tokenized=[]
    if '"' in line[0]:
        line=line[0].split('"')    
    line_tokenized=[i.split(" ") for i in line] # if i.endswith("\n")==False
    
    return line_tokenized
