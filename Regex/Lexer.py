'''
Lexer for Regex+
'''
from tokens import *
import token

# https://stackoverflow.com/questions/20256066
def SpaceSplit(string):
  last = 0
  splits = []
  inQuote = None
  for i, letter in enumerate(string):
    if inQuote:
      if (letter == inQuote):
        inQuote = None
    else:
      if (letter == '"' or letter == "'"):
        inQuote = letter

    if not inQuote and letter == ' ':
      splits.append(string[last:i])
      last = i+1

  if last < len(string):
    splits.append(string[last:])

  return splits

class Lexer:
    def __init__(self) -> None:
        pass
    
    def compile(self, string) -> list:
        pass

    def Analyse(self, string) -> list:
        s1 = SpaceSplit(string) # Split string by spaces
        toks = [] # Initialize list of tokens
        for s in s1: # Loop through tokens
            toks.append(token.GetTok(s)) # Add token to list
        return toks # Return list of tokens

    def __str__(self) -> str:
        return self.__class__.__name__
    
    def __repr__(self) -> str:
        return self.__str__()

l = Lexer()