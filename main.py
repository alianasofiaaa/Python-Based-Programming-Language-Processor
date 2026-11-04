from scanner import lexer
from my_parser import parser
from interpreter import Interpreter

print("Starting Program")

textFile = open('Program_Test.txt', 'r')
data = textFile.read()

# parse
ast = parser.parse(data, lexer=lexer)

print("\nAbstract Syntax Tree:\n")
print(ast)

# interpret
if ast is not None:
    runner = Interpreter()
    result = runner.evaluate(ast)

    print("\nExecution Result:\n")
    print(result)
else:
    print("\nParsing failed. No execution performed.")