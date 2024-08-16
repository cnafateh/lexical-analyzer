import os
import platform

cpp_program = open("./test.c", "r").read()

symbols = ['!', '@', '#', '$', '%', '&', '^', '*']
oparators = ['+', '-', '*', '/', '=', '+=', '-=', '==', '<=', '>=']
keywords = ['auto','break', 'case', 'char', 'const', 'continue', 'default', 'do', 
			'double', 'else', 'enum', 'extern', 'float', 'for', 'goto', 'if', 
			'int', 'long', 'register', 'return', 'short', 'signed', 'sizeof', 'static', 
			'struct', 'switch', 'typedef', 'union', 'unsigned', 'void', 'volatile', 'while']
delimiters = ['.', ',', ';', '(', ')', '<', '>', '{', '}', '[', ']']
# delimiters = [' ', '	', '.', ',', '\n', ';', '(', ')', '<', '>', '{', '}', '[', ']']

def symptoms_check(chr):
    for symptom in symbols:
        if chr == symptom:
            return True, chr, "symbols"
    
    for symptom in oparators:
        if chr == symptom:
            return True, chr, "oparators"
    
    for symptom in keywords:
        if chr == symptom:
            return True, chr, "keywords"

    for symptom in delimiters:
        if chr == symptom:
            return True, chr, "delimiters"
    
    return False, chr


if(platform.system() == 'Linux'):
    clc = 'clear'
else:
    clc = 'cls'

os.system(clc)

token = ""
tokens = []
flag = False
counter = 0
num = ""

for chr in cpp_program:
    if chr == " " or chr == '\n':
        flag = True
        tokens.append(num)
        num = ""

    elif (chr in symbols) or (chr in oparators) or (chr in delimiters):
        tokens.append(chr)
        flag = True


    if 97 <= ord(chr) <= 122 or 65 <= ord(chr) <= 90:
        token += chr


    elif flag:
        tokens.append(token)
        token = ""
    
    try:
        int(chr)
        num += chr
    except:
        continue 
tokens.append(num)   

tokens = [item for item in tokens if item != ""]
# print(tokens)

for item in tokens:

    if item in symbols:
        print(f"{item:8} --->  symbol")

    elif item in oparators:
        print(f"{item:8} --->  oparator")
        
    elif item in keywords:
        print(f"{item:8} --->  keyword")

    elif item in delimiters:
        print(f"{item:8} --->  delimiter")
    
    else:
        print(f"{item:8} --->  constants")
