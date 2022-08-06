def count(string, pattern):
    """
    Count the number of times pattern occurs in string.
    """
    count = 0 # Initialize count
    for i in range(len(string)): # Loop through string
        if string[i:i+len(pattern)] == pattern: # Check if pattern is at i
            count += 1 # If so, increment count
    return count # Return count


class RegexSyntaxError(Exception): # Exception for syntax errors in regex+
    """
    Raised when the syntax of a regex is incorrect.
    """
    pass