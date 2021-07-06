#Validate the list of keywords
#For now add and multiply are allowed ones
def validateKeywords(tempword):
    flag=0
    allowed_kw=["(add", "(multiply"]
    for kw in allowed_kw:
        if(tempword.split()[0]  == kw):
            flag=1
    if(flag!=1):
        #print(kw, tempword)
        raise Exception("Illegal keyword used. Valid keywords are ")

#Perform the arithmetic operations
def operateOnNumbers(word, start, end):
    print(word)
    #print(str(start) +"  "+end)
    print(f'{start} {end}')
    mylist=list(word)
    resultadd=0
    resultmul=1
    if ('a' in mylist[start + 1] and 'd' in mylist[start + 2] and  'd' in mylist[start + 3]):
        newstring=word[start+5:end]
        newlist=newstring.split()
        for myitem in newlist:
            resultadd=resultadd+int(myitem)
            result=resultadd
    elif ('m' in mylist[start + 1] and 'u' in mylist[start + 2] and  'l' in mylist[start + 3] 
        and 't' in mylist[start+4] and 'i' in mylist[start+5] and 'p' in mylist[start+6] 
        and 'l' in mylist[start+7] and 'y' in mylist[start+8] ):
        newstring=word[start+10:end]
        newlist=newstring.split()
        for myitem in newlist:
            resultmul=resultmul*int(myitem)
            result=resultmul
    
    return result

def calculate(word):
    c=word.count('(')
    #print(len(word))
    tempstart=0
    tempend=0
    result=0
    tempstart = word.rindex('(')
    #print(str(tempstart))
    flag=0
    tempword=word[tempstart:len(word)]
    tempend= tempword.index(')')+tempstart
    validateKeywords(tempword)
    result = operateOnNumbers(word,tempstart,tempend)
    c=c-1
    if(c>0):        
        newword=word[0:tempstart-1] +' ' + str(result) + word[tempend+1:len(word)]
        #print(newword)
        calculate(newword)
    else:
        print(result)

import os
import sys

#print("\nName of Python script:", sys.argv[0])
expression=sys.argv[1].lower()
#expression = "(add (add (add 10 (add 123 245) ) (add 120 121) ) 1)"
#print(expression)
calculate(expression)
