'''
Tokens for Regex+
'''
from tokens import *
import util

class Token:
    def __init__(self, value, type): # value is the string value of the token, type is the type of the token
        self.value = value
        self.type = type
    
    def __str__(self): # for printing
        return f'Token({self.type}, {self.value})'
    
    def __repr__(self): # for debugging
        return self.__str__()

def GetTok(s):
    s1 = s.upper() # Convert to upper case
    match s1: # Match against the list of tokens
        case "SELECT": return Token("SELECT", T_SELECT)
        case "FROM": return Token("FROM", T_FROM)
        case "NUM": return Token("NUM", T_NUM)
        case "LETTER": return Token("LETTER", T_LETTER)

        case "*": return Token("*", T_STAR)

        case "AND": return Token("AND", T_AND)
        case "OR": return Token("OR", T_OR)
        case "NOT": return Token("NOT", T_NOT)
        case "=": return Token("=", T_EQUAL)
        case "!": return Token("!", T_EXCLAMATION)
        case "<": return Token("<", T_LESS)
        case ">": return Token(">", T_GREATER)
        case "<=": return Token("<=", T_LESS_EQUAL)
        case ">=": return Token(">=", T_GREATER_EQUAL)
        case "!=": return Token("!=", T_NOT_EQUAL)
        case "==": return Token("==", T_EQUAL_EQUAL)
        case "TRUE": return Token("TRUE", T_TRUE)
        case "FALSE": return Token("FALSE", T_FALSE)
    
    if s1[:5] == "WHERE": # Check for WHERE keyword (done separately cuz of mode precedence)
        return Token(s1[6:], T_WHERE)

    s2 = s.strip('.') # Remove '.' to check if num
    if s2.isdigit() and util.count(s2, '.') <= 1: # Check if num, ensuring not more than one '.'
        if util.count(s2, '.') == 0: # Check if num is an int
            return Token(int(s2), T_NUMBER) # if so return int
        else:
            return Token(float(s1), T_NUMBER) # else return float

    elif s1[0] == "%": # Check if variable
        return Token(s1[1], T_VARIABLE) # if so return variable

    else:
        if s1[0] == '"' or s1[0] == "'" and s1[0] == s1[-1]: # Check if string
            return Token(s1[1:-1], T_STRING) # if so return string
        else:
            if s1[0] == '"' or s1[0] == "'": # Check if unclosed string
                raise util.RegexSyntaxError(f'unclosed string: {s}') # raise error for unclosed string
            else:
                raise util.RegexSyntaxError(f'invalid token: {s}') # else raise error for invalid token

        