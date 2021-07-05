# Python3 program to Split string into characters
#"(add (multiply 2 3) 1)"
def calculate(word):
    c=word.count('(')
    mydict={}
    mywords=[]
    #print(len(word))
    mylist=list(word)
    tempstart=0
    tempend=0
    result=0
    resultadd=0
    resultmul=1
    tempstart = word.rindex('(')
    #print(str(tempstart))
    flag=0
    tempword=word[tempstart:len(word)]
    tempend= tempword.index(')')+tempstart
    #print(word[tempstart:tempend+2])
    allowed_kw=["(add", "(multiply"]
    for kw in allowed_kw:
        if(tempword.split()[0]  == kw):
            flag=1
    if(flag!=1):
        #print(kw, tempword)
        print("Illegal keyword used")
        sys.exit()
    
    if ('a' in mylist[tempstart + 1] and 'd' in mylist[tempstart + 2] and  'd' in mylist[tempstart + 3]):
        newstring=word[tempstart+5:tempend]
        newlist=newstring.split()
        for myitem in newlist:
            resultadd=resultadd+int(myitem)
            result=resultadd
    if ('m' in mylist[tempstart + 1] and 'u' in mylist[tempstart + 2] and  'l' in mylist[tempstart + 3] 
        and 't' in mylist[tempstart+4] and 'i' in mylist[tempstart+5] and 'p' in mylist[tempstart+6] 
        and 'l' in mylist[tempstart+7] and 'y' in mylist[tempstart+8] ):
        newstring=word[tempstart+10:tempend]
        newlist=newstring.split()
        for myitem in newlist:
            resultmul=resultmul*int(myitem)
            result=resultmul
    c=c-1
    if(c>0):        
        newword=word[0:tempstart-1] +' ' + str(result) + word[tempend+1:len(word)]
        #print(newword)
        calculate(newword)
    else:
        print(result)

import os
import sys

n = len(sys.argv)
#print("Total arguments passed:", n)

# Arguments passed
##print("\nName of Python script:", sys.argv[0])
expression=sys.argv[1]
#expression = "(add (add (add 10 (add 123 245) ) (add 120 121) ) 1)"
#print(expression)


calculate(expression)
