***Python-Based Programming Language Processor***

About the Project

This project was developed for a Programming Languages course. It is a language processor built with Python that can read, analyze, and execute programs written in a custom programming language.

The project uses PLY (Python Lex-Yacc) for lexical and syntax analysis. After parsing the input, it creates an Abstract Syntax Tree (AST), which is then used by the interpreter to execute the program.

Technologies

* Python
* PLY (Python Lex-Yacc)

Features

* Variable declarations and assignments
* Basic arithmetic operations (+, -, *, /)
* Comparison operators (=, <, >)
* Logical operators (AND, OR)
* IF/THEN/ELSE statements
* LET expressions
* Function definitions and calls
* Passing arguments to functions
* Basic error handling, including division by zero and undefined variables or functions

How It Works

The project has three main parts:

* Scanner: Reads the source code and identifies its tokens.
* Parser: Checks the syntax and builds the Abstract Syntax Tree (AST).
* Interpreter: Uses the AST to execute the instructions.

The main.py file connects these components. It reads a .txt file, sends the code to the parser, and passes the resulting AST to the interpreter.

How to Run

1. Clone the repository:

git clone YOUR_REPOSITORY_URL

2. Go to the project folder:

cd YOUR_PROJECT_FOLDER

3. Install the required library:

pip install -r requirements.txt

4. Run the program:

python3 main.py

What I Learned

Working on this project helped me understand how programming languages process code, from recognizing tokens and checking syntax to building an AST and executing instructions. It also gave me more practice with Python, recursion, and working with functions and variables.
