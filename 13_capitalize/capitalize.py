def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """
    upper = phrase[0].upper()
    return phrase.replace(phrase[0], upper, 1)