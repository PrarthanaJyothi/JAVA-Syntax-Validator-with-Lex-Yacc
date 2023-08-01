# this program runs as long as the data we parse is a valid variable declaration.
import ply.lex as lex
import ply.yacc as yacc

tokens = ['const', 'equals', 'semicolon', 'int', 'float', 'char', 'boolean', 'double', 'x', 'y', 'z', 'comma'];
t_ignore=' \t'
t_semicolon = r';';
t_comma = r'\,';
t_int = r'int';
t_float = r'float';
t_double = r'double';
t_char = r'char';
t_boolean = r'boolean';
# t_string = r'string';
t_x = r'x';
t_y = r'y';
t_z = r'z';
t_const = r'const';
t_equals = r'=';

try:
    def p_vardec(p):
        '''assign : datatype dec semicolon
        '''
        print("Syntax is correct.");

    def p_dec(p):
        '''dec : x
        | x comma dec
        | x equals const comma dec
        | x equals const
        | y
        | y comma dec
        | y equals const comma dec
        | y equals const
        | z
        | z comma dec
        | z equals const comma dec
        | z equals const
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
    data1 = '''int x;''';
    data2 = '''float x, y;''';
    data3 = '''char x = const, y = const;''';
    data4 = '''int a''';

    yacc.parse(data1)
    yacc.parse(data2)
    yacc.parse(data3)
    yacc.parse(data4)

except: 
    print(" ")
