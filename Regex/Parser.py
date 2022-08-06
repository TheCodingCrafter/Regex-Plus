"""
Regex+ Parser
"""
from tokens import *
from util import *
from token import Token, GetTok
from Lexer import Lexer

class Parser:
    def __init__(self) -> None:
        pass
        
    def __str__(self) -> str:
        return self.__class__.__name__
    
    def __repr__(self) -> str:
        return self.__str__()
    
    def EvalExpr(self, exp) -> list:
        """
        run a regex+ expression
        """
        l = Lexer() # Create lexer
        tmp = l.Compile(exp) # Compile regex+ expression
        src = tmp.code; del tmp # extract code, delete Regex object

        # Initialize variables
        skip = 0 # Skip counter
        RET = [] # Return list, empty initially
        VARS = {
            'I': '',
            'x': '',
        } # Dictionary of variables

        # loop through tokens
        for i, tok in enumerate(src):
            if skip > 0: # If skipping
                skip -= 1 # Decrement skip counter
                continue # Skip to next token

            match tok:
                case Token.SELECT: # SELECT
                    if src[i+2] != Token.FROM: # If not FROM
                        raise RegexSyntaxError('SELECT must be followed by FROM') # Raise exception

                    skip = 2 # Skip next 2 tokens
                    tmp = self.EvalExpr(src[i+3:]) # get selected items
                    if src[i+1].type == Token.STAR:
                        RET = tmp
                    elif src[i+1].type == Token.NUMBER:
                        RET = tmp[src[i+1]:]
                    else:
                        raise RegexSyntaxError('Select must be followed by a number or *') # Raise exception
                
                
