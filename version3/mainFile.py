import os
import sys
import logging
from Calculator import Calculator

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))

log = logging.getLogger("S_Expr : ")

# Validate the list of keywords
# For now add and multiply are allowed ones
# We evaluate the first sub-word of the sent partial expression and validate against the allowed keywords
# We also lstrip the spaces for this partial expression to remove the preceeding spaces             
def validateKeywords(tempword):
    flag=0
    allowed_kw=["add", "multiply"]
    for kw in allowed_kw:
        if(tempword.lstrip().split()[0] == kw):
            flag=1
    if(flag!=1):
        raise Exception("It looks like there is no valid keyword. Valid keywords are add, multiply")

# Parse the provided partial expression and pass it on to calculator for arithmetic operations
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
        if (len(newlist)<2):
            raise Exception("It looks like the number of operands are less than 2. Please follow the S-Expression syntax ("+word+")")
        for myitem in newlist:
            calc=Calculator(result,int(myitem))
            result=calc.add()
    elif (word[start_index:len(str_mul)]  == str_mul):
        result=1
        newlist=word[len(str_mul):].split()
        log.debug("Length of new list is "+str(len(newlist)))
        if (len(newlist)<2):
            raise Exception("It looks like the number of operands are less than 2. Please follow the S-Expression syntax ("+word+")")
        for myitem in newlist:
            if(int(myitem) == 0):
                result=0
                break
            calc=Calculator(result,int(myitem))
            result=calc.multiply()
    return result

#Recursively, parse the right extreme expression and keep working left to complete the arithmetic operations, following the S-Expression syntax
def calculate(word):
    log.debug(word)
    #Get the count of left paranthesis. This is to used for evaluating the expressions and come out of the recursion.
    c=word.count('(')
    #If the left and right are not equal, that is not a valid S-Expression syntax 
    if(c!=word.count(')')):
        raise Exception("It looks like the expression is invalid. Please check the expression. It should follow the S-Expression syntax.")
    if(c==0):
        print(word)
        return
    tempstart=0
    tempend=0
    #Getting the index of the right most paranthesis. Start of identifying the right most expression
    tempstart = word.rindex('(')
    flag=0
    
    tempword=word[tempstart:len(word)]
    tempend= tempword.index(')')+tempstart
    #First validate the keyword for this expresion. 
    #We remove the current expression right paranthesis and send the remaining.
    validateKeywords(tempword[1:])
    
    #Start the operation to perform the calculation.
    result = operateOnNumbers(word[tempstart+1:tempend])
    log.debug(result)
    c=c-1
    if(c>0):        
        newword=word[0:tempstart-1] +' ' + str(result) + word[tempend+1:len(word)]
        log.debug(newword)
        calculate(newword)
    else:
        print(result)


#Main program starts here
expression=sys.argv[1].lower()
log.debug(expression)
calculate(expression)
