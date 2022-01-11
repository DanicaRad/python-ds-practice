def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    half = int(len(parens) / 2)
    if parens[:half][0] == ('(') and parens[half:][-1] == (')'):
        return parens[:half].count('(') == parens[half:].count(')') or parens[:half] == parens[half:]
    return False