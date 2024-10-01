import csv

encryption = open('encrypted.txt','r')

text = encryption.readline()

reverse_cipher = {
            '1':'A', '2':'a', '3':'B', '4':'b', '5':'C',
              '6':'c', '7':'D', '8':'d', '9':'E', '0':'e',
             '!':'F', '@':'f', '#':'G', '$':'g', '%':'H', 
             '^':'h', '&':'I', '*':'i', '(':'J', ')':'j', 
             '`':'K', '~':'k', '=':'L', '+':'l', 'œ':'M', 
             '∑':'m', '®':'N', '†':'n', '¥':'O', '¨':'o', 
             'π':'P', 'å':'p', 'ß':'Q', '∂':'q', 'ƒ':'R',
             '©':'r', '˙':'S', '∆':'s', '˚':'T', '¬':'t', 
             '≈':'U', 'ç':'u', '√':'V', '∫':'v', '?':'W', 
             '÷':'w', '«':'X', '◊':'x', 'Ç':'Y', 'Œ':'y', 
             'Â':'Z', '':'z'}

msg = ''
for character in text:
    if character in reverse_cipher:
        msg += reverse_cipher[character]
    else:
        msg += character

print(msg)
        

