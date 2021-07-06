import os
import sys
import logging
from Calculator import Calculator

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))

log = logging.getLogger("S_Expr : ")

#Validate the list of keywords
#For now add and multiply are allowed ones
def validateKeywords(tempword):
    flag=0
    allowed_kw=["add", "multiply"]
    for kw in allowed_kw:
        if(tempword.lstrip().split()[0] == kw):
            flag=1
    if(flag!=1):
        raise Exception("Illegal keyword used. Valid keywords are add, multiply")

#Perform the arithmetic operations
def operateOnNumbers(word):
    result=0
    str_add="add"
    str_mul="multiply"
    start_index=0
    word=word.lstrip()
    log.debug(word)

    if (word[start_index:len(str_add)]  == str_add):
        result=0
        newlist=word[len(str_add):].split()
        for myitem in newlist:
            calc=Calculator(result,int(myitem))
            result=calc.add()
    elif (word[start_index:len(str_mul)]  == str_mul):
        result=1
        newlist=word[len(str_mul):].split()
        for myitem in newlist:
            calc=Calculator(result,int(myitem))
            result=calc.multiply()
    return result

def calculate(word):
    c=word.count('(')
    tempstart=0
    tempend=0
    tempstart = word.rindex('(')
    flag=0
    tempword=word[tempstart:len(word)]
    tempend= tempword.index(')')+tempstart
    validateKeywords(tempword[1:])
    result = operateOnNumbers(word[tempstart+1:tempend])
    log.debug(result)
    c=c-1
    if(c>0):        
        newword=word[0:tempstart-1] +' ' + str(result) + word[tempend+1:len(word)]
        log.debug(newword)
        calculate(newword)
    else:
        print(result)

expression=sys.argv[1].lower()
log.debug(expression)
calculate(expression)

