import csv

infile = open('sometext-1.txt','r')
text = infile.readline()

#clean up
punctuation = ['.',',']
hyphen = '-'
for symbol in punctuation:
    text = text.replace(symbol, '')
for hyphen in punctuation:
    text = text.replace('-', ' ')

#output
word_list = text.split()
word_dict = {}
for k in word_list:
    if k in word_dict:
        word_dict[k] += 1
    else:
        word_dict[k] = 1

for k,v in word_dict.items():
    print(f"{k.capitalize()}: {v}")