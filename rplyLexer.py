from rply import LexerGenerator


class RPLYLexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        # Print
        self.lexer.add('PRINT', r'print')
        # Parenthesis
        self.lexer.add('OPEN_PAREN', r'\(')
        self.lexer.add('CLOSE_PAREN', r'\)')
        # Semi Colon
        self.lexer.add('SEMI_COLON', r'\;')
        # Operators
        self.lexer.add('SUM', r'\+')
        self.lexer.add('SUB', r'\-')
        self.lexer.add('MUL', r'\*')
        self.lexer.add('DIV', r'\/')

        self.lexer.add('MOD', r'\%')

        self.lexer.add('EQUALS', r'\=')
        self.lexer.add('EQTO', r'\=\=')
        self.lexer.add('GREQ', r'\>\=')
        self.lexer.add('LSEQ', r'\<\=')
        self.lexer.add('LESS', r'\<')
        self.lexer.add('GREAT', r'\>')

        #Statements
        self.lexer.add('IF', r'if')
        self.lexer.add('ELSE', r'else')

        self.lexer.add('NAME', r'[a-zA-Z_][a-zA-Z0-9_]*')
        # Number
        self.lexer.add('NUMBER', r'\d+')
        # Ignore spaces
        self.lexer.ignore('\s+')

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()
