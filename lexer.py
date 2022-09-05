import re
import sys

LexerList = []
LexerListCounter = -1


def lexer():
    if len(sys.argv) <= 1:
        print('Provide the file name as an argument after the program name:\ntestMain.py input.txt')
        exit(1)

    #--infile = open("input3.txt", "r")
    #f.close()

    infile = open(sys.srvg[1], "r")
    lineNum = 0
    # print("Line \t\t Value \t\t Token")
    # print("---------------------------------")
    lines = infile.readlines()

    # x represents a line, y represents a "word"
    for x in lines:
        lineNum = lineNum + 1
        line = re.split('\s|(;|\(|\)|\+|-|/|\*|<=|>=|\{|}|=|\'|\"|<|>|&&)', x)
        line = list(filter((None).__ne__, line))
        line = list(filter(('').__ne__, line))
        for y in line:
            y = re.sub(r"[\n\t\s]*", "", y)
            tokenize(y, lineNum)

    return LexerList


# so this function gets a "word" and tokenizes it
def tokenize(word, lineNum):
    tokenType = "unknown"
    punct = re.compile(r";|\(|\)|\+|-|/|\*|<=|>=|{|}|=|\'|\"|<|>|&&|\|\|")
    if (bool(punct.search(word))):
        punctList = punct.findall(word)
        for x in punctList:
            if (x == ';'):
                tokenType = "semicolon"
                # print(str(lineNum) + "\t\t\t" + ";" + "\t\t\t" + str(tokenType))
            elif (x == ')'):
                tokenType = "R paren"
                # print(str(lineNum) + "\t\t\t" + ")" + "\t\t\t" + str(tokenType))
            elif (x == '('):
                tokenType = "L paren"
                # print(str(lineNum) + "\t\t\t" + "(" + "\t\t\t" + str(tokenType))
            elif (x == '}'):
                tokenType = "R curly"
                # print(str(lineNum) + "\t\t\t" + "}" + "\t\t\t" + str(tokenType))
            elif (x == '{'):
                tokenType = "L curly"
                # print(str(lineNum) + "\t\t\t" + "{" + "\t\t\t" + str(tokenType))
            elif (x == '+'):
                tokenType = "plus"
                # print(str(lineNum) + "\t\t\t" + "+" + "\t\t\t" + str(tokenType))
            elif (x == '-'):
                tokenType = "minus"
                # print(str(lineNum) + "\t\t\t" + "-" + "\t\t\t" + str(tokenType))
            elif (x == '.'):
                tokenType = "realNum"
                # print(str(lineNum) + "\t\t\t" + "." + "\t\t\t" + str(tokenType))
            elif (x == '/'):
                tokenType = "divide"
                # print(str(lineNum) + "\t\t\t" + "/" + "\t\t\t" + str(tokenType))
            elif (x == '*'):
                tokenType = "mulitply"
                # print(str(lineNum) + "\t\t\t" + "*" + "\t\t\t" + str(tokenType))
            elif (x == '%'):
                tokenType = "modulo"
                # print(str(lineNum) + "\t\t\t" + "%" + "\t\t\t" + str(tokenType))
            elif (x == ']'):
                tokenType = "R sq. br."
                # print(str(lineNum) + "\t\t\t" + "]" + "\t\t\t" + str(tokenType))
            elif (x == '['):
                tokenType = "L sq. br."
                # print(str(lineNum) + "\t\t\t" + "[" + "\t\t\t" + str(tokenType))
            elif (x == '\''):
                tokenType = "single quote"
                # print(str(lineNum) + "\t\t\t" + "\'" + "\t\t\t" + str(tokenType))
            elif (x == '\"'):
                tokenType = "double quote"
                # print(str(lineNum) + "\t\t\t" + "\"" + "\t\t\t" + str(tokenType))
            elif (x == '='):
                tokenType = "assign op"
                # print(str(lineNum) + "\t\t\t" + "=" + "\t\t\t" + str(tokenType))
            elif (x == '<'):
                tokenType = "less than op"
                # print(str(lineNum) + "\t\t\t" + "<" + "\t\t\t" + str(tokenType))
            elif (x == '>'):
                tokenType = "greater than op"
                # print(str(lineNum) + "\t\t\t" + ">" + "\t\t\t" + str(tokenType))
            elif (x == '<='):
                tokenType = "less than or equal to op"
                # print(str(lineNum) + "\t\t\t" + "<=" + "\t\t\t" + str(tokenType))
            elif (x == '&&'):
                tokenType = "and op"
                # print(str(lineNum) + "\t\t\t" + "&&" + "\t\t\t" + str(tokenType))
            elif (x == '||'):
                tokenType = "or op"
                # print(str(lineNum) + "\t\t\t" + "||" + "\t\t\t" + str(tokenType))

        # these lines aren't necessary since they get split up in the lexer function
        # word = re.sub(punct, '', word)
        # if (word != ""):
        #    tokenize(word, lineNum)

    else:
        keyword = re.compile("main|int|char|String|double|if|for|while|bool|else")
        trueword = re.compile("true")
        falseword = re.compile("false")
        variable = re.compile(r"^[a-z](\w*|'-'*|'_'*|'@'*|'#'*)*", re.IGNORECASE)
        realNum = re.compile(r"^\d+.\d+$")
        intNum = re.compile(r"\d+")

        if (keyword.match(word)):
            tokenType = "keyword"
        elif (trueword.match(word)):
            tokenType = "true"
        elif (falseword.match(word)):
            tokenType = "false"
        elif (bool(variable.fullmatch(word))):
            tokenType = "identifier"
        elif (realNum.match(word)):
            tokenType = "RealNum"
        elif (intNum.match(word)):
            tokenType = "IntNum"
        # print(str(lineNum) + "\t\t\t" + str(word) + "\t\t\t" + str(tokenType))

    #print(next(tokenType))
    LexerList.append((word, lineNum, next(tokenType)))


def next(token):
    return token


def lex():
    global LexerListCounter
    if LexerListCounter >= 0:
        print('Line: ' + str(LexerList[LexerListCounter][1]) + '\t\t\tValue: ' + str(LexerList[LexerListCounter][0]) + '\t\t\tToken Category: ' + str(LexerList[LexerListCounter][2]))
    if len(LexerList) <= LexerListCounter:
        exit()
    LexerListCounter += 1
    return LexerList[LexerListCounter]
