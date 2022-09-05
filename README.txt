Team Member Names:
Alex Diehl

Purpose:
This program acts as a Parser able to parse through C style code

Classes Explanation:
The three classes are the testMain class and lexer class. The testMain class invokes the parser function from the Parser class. The lexer class reads the provided text file containing C++ style code and identifies all keywords, operations, and punctuation in order. The class will then display a table of all these in order of the provided code. The Parser class utilizes the recognized tokens from the lexer, and pieces them together in larger patterns in the C style langauges, such as declarations and statements.

Functions Explination:

Parser.py file
--------------------------
parser(): begins the parsing process, gets the list of tokens from the lexer file. Statrs by invoking the program function

lex(): calls the lex() function from the lexer.py file. from here the lexer token is printed, and the program moves on to the next lexer token

program(): the first and highest-level function deticated to parsing through the c style code. Looks for int main() to start the program, and looks for delcarations and statements from there.

Declarations(): looks for variables being declared

Declaration(): one instance of a variable being declared, looks for a time and an identifier following the type

Type(): determines the type of variable being declared (bool, int, etc)

Statements(): looks for statements in which a program completes a calculation or action

Statement(): a body of code in which a program achieves a calculation or task, such as changing the value of a variable

Block(): surrounded by brackets, a block encompasses multiple statements in one body

Assignment(): gives a variable a certain value

IfStatement(): looks for a condition in order to complete a statement, the condition must be met in order to do so

WhileStatement(): will repeat a statement or body of statements until a condition is no longer met

Expression(): for expressing multiple conditions with OR

Conjunction(): for expressing multiple conditions with AND

Equality(): expression in which two value must be equal to each other

EquOp(): looks for symbols indicating equivilancy (or lack therof)

Relation(): condition in which one value is creater or less than another

RelOp(): searches for and identifies the symbols for comparing values in terms of less than and greater than

Addition(): in which two or more values can be added or subtracted

AddOp(): searches for the symbols regarding adding and subtracting

Term(): for multiplying and dividing

MulOp(): searches for symbols regarding multiplying and dividing

Factor(): for modifying values, either in the negatives or through factorial

UnaryOp(): searches for the operational symbols meant to modify a value

Primary(): regards the actual value in question

Identifier(): parses variable names meant to identify valuese

Letter(): parses through a latter of the english alphabet

Digit(): parses through a numerical digit

Literal(): parses the value itself

Integer(): parses a whole number, which can be negative or positive

Boolean(): parses a value which is either true or false

Float(): parses a number which can be a fraction of a whole, represented using decimals

Char(): parses a single character
 

Running the Code:
To run the code, first, make sure python is installed on your machine. Next, in your OS file explorer, navigate to the current directory containing the testMain.py and lexer.py files. Within this same directory, place the desired text file containing C++ style code that will be read by the lexer program.

Finally, run the program: open the command prompt window, and navigate to the current directory containing the testMain.py, lexer.py, and text file that has been inserted within the prompt. Next, run the program by typing "py testMain.py input.txt", or input2.txt or input3.txt accordingly. This should run the program using your installed version of Python.

The first input.txt file deals with basic delation and assignment. The second input2.txt deals with an if statement. Input three deals with expressions.