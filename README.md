# JAVA-syntax-Validator-with-Lex-Yacc

This program has two parts. (JAVA declaration syntax validation)

The first part validates whether a given function declaration is a valid function declaration or not.

The second part validates whether a given variable declaration is a valid variable declaration or not.

We use Lex-Yacc here. 

Since the program doesn't take user inputs, to use your own test cases, change the test cases in the program.


To install needed modules:

pip install ply


Context Free Grammar for the function declaration:

S -> ABC

A -> void | int | float | double | char | boolean

B -> fnname

C -> (P)|(P);

P -> DV,P | DV | λ

D -> int | float | double | char | boolean

V -> varname  



Context Free Grammar for the variable validation:

S -> AB

A -> int | float | double | char | boolean

B -> D;

D -> varname | varname,D | varname=C,D | varname=C

C -> const
