import re
import sys
import lexer

nextToken = ''


def parser():
    global LexerList
    LexerList = lexer.lexer()
    program()

def lex():
    global LexerList
    global nextToken
    global counter

    nextToken = lexer.lex()

# int main(){<Delcarations><Statements>}
def program():
    global nextToken
    global counter
    global LexerList

    print('\nParsing <Program>\n--------------------------------------------')
    lex()

    if nextToken[0] == 'int':
        lex()
    else:
        print('expecting int')

    if nextToken[0] == 'main':
        lex()
    else:
        print('expecting main')

    if nextToken[0] == '(':
        lex()
    else:
        print('expecting (')

    if nextToken[0] == ')':
        lex()
    else:
        print('expecting )')

    if nextToken[0] == '{':
        lex()
        while nextToken[0] != '}':
            if nextToken[0] == 'int' or nextToken[0] == 'bool' or nextToken[0] == 'float' or nextToken[0] == 'char':
                Declarations()
            elif(nextToken[0] != '}'):
                Statements()
            else: lex()
        else:
            lex()
    else:
        print('expecting {')

# {<Declaration>}
def Declarations():
    global nextToken
    global counter
    global LexerList

    print('\nEnter <Declarations>')
    while nextToken[0] == 'int' or nextToken[0] == 'bool' or nextToken[0] == 'float' or nextToken[0] == 'char':
        Declaration()

# <Type> <Identifier> [[Integer]], {,Identifier[[Integer]]};
def Declaration():
    global nextToken
    global counter
    global LexerList

    print('Enter <Declaration>')
    Type()
    Identifier()

    if nextToken[0] == '[':
        Integer()
        if nextToken[0] == ']':
            lex()

    if nextToken[0] == ',':
        while nextToken[0] == ',':
            lex()
            Identifier()

            if nextToken[0] == '[':
                Integer()
                if nextToken[0] == ']':
                    lex()

    while nextToken[0] != ';':
            lex()
    else:
        lex()
        print('Exit <Declaration>\n')
        True

def Type():
    global nextToken
    global counter
    global LexerList

    print('Enter <Type>')
    if nextToken[0] == 'bool' or 'int' or 'float' or 'char':
        lex()
    else:
        print('expecting a Type')
    print('Exit <Type>')
    True

def Statements():
    global nextToken
    global counter
    global LexerList

    print('\nEnter <Statements>')
    while nextToken[0] != ';':
        Statement()
    else:
        lex()
        print('Exit <Statements>')

def Statement():
    print('Enter <Statement>')
    if nextToken[0] == ';':
        lex()
    elif nextToken[0] == '{':
        Block()
    elif nextToken[2] == 'identifier':
        Assignment()
    elif nextToken[0] == 'if':
        IfStatement()
    elif nextToken[0] == 'while':
        WhileStatement()

    print('Exit <Statement>')
    True

def Block():
    print('Enter <Block>')
    if(nextToken[0] == '{'):
        lex()
        Statements()
    if(nextToken[0] == '}'):
        lex()
    print('Exit <Block>')
    True

def Assignment():
    print('Enter <Assignment>')
    Identifier()
    if(nextToken[0] == '['):
        lex()
        Expression()
        if(nextToken[0] == ']'):
            lex()

    if nextToken[0] == '=':
        lex()
    else:
        print('= missing')

    Expression()
    print('Exit <Assignment>')
    True

def IfStatement():
    print('Enter <ifStatement>')
    if(nextToken[0] == 'if'):
        lex()
    if(nextToken[0] == '('):
        lex()
    Expression()
    if(nextToken[0] == ')'):
        lex()
    Statement()
    if(nextToken[0] == 'else'):
        lex()
        Statement()
    print('Exit <IfStatement>')
    True

def WhileStatement():
    print('Enter <ifStatement>')
    if (nextToken[0] == 'if'):
        lex()
    if (nextToken[0] == '('):
        lex()
    Expression()
    if (nextToken[0] == ')'):
        lex()
    Statement()
    print('Exit <IfStatement>')
    True

def Expression():
    print('Enter <Expression>')
    Conjunction()
    while nextToken[0] == '||':
        lex()
        Conjunction()
    else:
        print('Exit <Expression>')

    True

def Conjunction():
    print('Enter <Conjunction>')
    Equality()
    while nextToken[0] == '&&':
        lex()
        Equality()

    print('Exit <Conjunction')
    True

def Equality():
    print('Enter <Equality>')
    Relation()
    if nextToken[0] == '==' or nextToken[0] == '!=':
        EquOp()
        Relation()
    print('Exit <Equality>')

    True

def EquOp():
    print('Enter <EquOp>')
    if nextToken[0] == '==' or nextToken[0] == '!=':
        lex()
    else: print ('missing EquOp')
    print('Exit <EquOp')
    True

def Relation():
    print('Enter <Relation>')
    Addition()
    if nextToken[0] == '<' or nextToken[0] == '<=' or nextToken[0] == '>' or nextToken[0] == '>=':
        RelOp()
        Addition()
    print('Exit <Relation>')
    True

def RelOp():
    print('Enter <RelOp>')
    if nextToken[0] == '<' or nextToken[0] == '<=' or nextToken[0] == '>' or nextToken[0] == '>=':
        lex()
    print('Exit <RelOp>')
    True

def Addition():
    print('Enter <Addition>')
    Term()
    if nextToken[0] == '+' or nextToken[0] == '-':
        AddOp()
    True

def AddOp():
    print('Enter <AddOp>')
    if nextToken[0] == '+' or nextToken[0] == '-':
        lex()
        print('Exit <AddOp>')
    else:
        print('add op not found')
    True

def Term():
    print('Enter <Term>')
    Factor()
    while nextToken[0] == '*' or nextToken[0] == '/' or nextToken[0] == '%':
        MulOp()
        Factor()
    else:
        print('Exit <Term>')
    True

def MulOp():
    print('Enter <MulOp>')
    if nextToken[0] == '*' or nextToken[0] == '/' or nextToken[0] == '%':
        lex()
    else:
        print('missing MulOp')
    print('Exit <MulOp>')
    True

def Factor():
    print('Enter <Factor>')
    if nextToken[0] == '-' or nextToken[0] == '!':
        UnaryOp()
    Primary()
    True

def UnaryOp():
    if nextToken[0] == '-' or nextToken[0] == '!':
        lex()
    else:
        print('missing UnaryOp')

    True

def Primary():
    print('Enter <Primary>')
    if(nextToken[2] == 'identifier'):
        Identifier()
        if nextToken[0] == '[':
            lex()
            Expression()
            if nextToken[0] == ']':
                lex()
    elif(nextToken[2] == 'IntNum' or nextToken[2] == 'RealNum' or nextToken[2] == 'true' or nextToken[2] == 'false'):
        Literal()
    elif(nextToken[0] == '('):
        lex()
        Expression()
        if(nextToken[0] == ')'):
            lex()
    elif(nextToken[0] == 'int' or nextToken[0] == 'bool' or nextToken[0] == 'float' or nextToken[0] == 'char'):
        Type()
        if (nextToken[0] == '('):
            lex()
            Expression()
            if (nextToken[0] == ')'):
                lex()





def Identifier():
    global nextToken
    global counter
    global LexerList

    print('Enter <Identifier>')
    if nextToken[2] == 'identifier':
        lex()
        print('Exit <Identifier>')
    else:
        print('Identifier Not Found')
    True

def Letter():
    pattern = re.compile("[a-z]",re.IGNORECASE)
    if(pattern.fullmatch(nextToken[0]) is not None):
        lex()
    True

def Digit():
    pattern = re.compile("^\d$")
    if (pattern.fullmatch(nextToken[0]) is not None):
        lex()
    True

def Literal():
    print('Enter <Literal>')
    if(nextToken[2] == 'RealNum' or nextToken[2] == 'IntNum' or nextToken[2] == 'True' or nextToken == 'False'):
        lex()

    if nextToken[0] == '\'':
        lex()
        while nextToken[0] != '\'':
            lex()
        else:
            lex()

def Integer():
    print('Enter <Integer>')
    pattern = re.compile("^\d$")
    if (pattern.fullmatch(nextToken[0]) is not None):
        lex()
        print('Exit <Integer>')
    True

def Boolean():
    print('Enter <Boolean>')
    if(nextToken == 'true' or nextToken == 'false'):
        lex()
        print('Exit <Boolean>')
    else:
        print('boolean missing')
    True

def Float():
    print('Enter <Integer>')
    pattern = re.compile(r"^\d+.\d+$")
    if (pattern.fullmatch(nextToken[0]) is not None):
        lex()
        print('Exit <Integer>')

def Char():

    True
