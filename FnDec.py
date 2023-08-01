# this program runs as long as the data we parse is a valid function declaration.

import ply.lex as lex
import ply.yacc as yacc

tokens = ['fnname', 'openbracket', 'closebracket', 'semicolon', 'int', 'float', 'char', 'boolean', 'double', 'x', 'y', 'z', 'comma', 'void'];
t_ignore=' \t'
t_openbracket = r'\(';
t_closebracket = r'\)';
t_semicolon = r';';
t_comma = r'\,';
t_void = r'void';
t_int = r'int';
t_float = r'float';
t_double = r'double';
t_char = r'char';
t_boolean = r'boolean';
# t_string = r'string';
t_x = r'x';
t_y = r'y';
t_z = r'z';
t_fnname= r'fnname';

try:
    def p_func(p):
        '''assign : returntype fnname openbracket paramlist closebracket 
        | returntype fnname openbracket closebracket 
        | returntype fnname openbracket paramlist closebracket semicolon 
        | returntype fnname openbracket closebracket semicolon 
        '''
        print("Syntax is correct.");

    def p_returntype(p):
        '''returntype : void
        | int
        | float
        | double
        | boolean
        | char
        '''

    def p_paramlist(p):
        '''paramlist : datatype x comma paramlist
            | datatype x
            | datatype y comma paramlist 
            | datatype y
            | datatype z comma paramlist 
            | datatype z
        '''

    def p_datatype(p):
        '''datatype : int
        | float
        | double
        | boolean
        | char
        '''

    def p_error(p):
        print("Syntax is incorrect - grammar is wrong");

    def t_error(p):
        print("Syntax is incorrect - a token is wrong");

    lex.lex();
    yacc.yacc();
    data1 = '''void fnname ( int x , float y , double z )''';
    data2 = '''int fnname (char x, boolean y )''';
    data3 = '''boolean fnname ( );''';
    data4 = '''void fnname( )''';
    data5 = ''' random (random text)''';

    yacc.parse(data1)
    yacc.parse(data2)
    yacc.parse(data3)
    yacc.parse(data4)
    yacc.parse(data5)

except: 
    print(" ")
