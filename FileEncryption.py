import csv

msg = open('info_security-1.txt','r')
encryption = open('encrypted.txt','w')

text = msg.readline()

cipher = {
            'A':'1', 'a':'2', 'B':'3', 'b':'4', 'C':'5',
              'c':'6', 'D':'7', 'd':'8', 'E':'9', 'e':'0',
             'F':'!', 'f':'@', 'G':'#', 'g':'$', 'H':'%', 
             'h':'^', 'I':'&', 'i':'*', 'J':'(', 'j':')', 
             'K':'`', 'k':'~', 'L':'=', 'l':'+', 'M':'œ', 
             'm':'∑', 'N':'®', 'n':'†', 'O':'¥', 'o':'¨', 
             'P':'π', 'p':'å', 'Q':'ß', 'q':'∂', 'R':'ƒ',
             'r':'©', 'S':'˙', 's':'∆', 'T':'˚', 't':'¬', 
             'U':'≈', 'u':'ç', 'V':'√', 'v':'∫', 'W':'?', 
             'w':'÷', 'X':'«', 'x':'◊', 'Y':'Ç', 'y':'Œ', 
             'Z':'Â', 'z':''}

for character in text:
    if character in cipher:
        encryption.write(cipher[character])
    else:
        encryption.write(character)


encryption.close()