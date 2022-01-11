def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    reversed_phrase = list(phrase)
    reversed_phrase.reverse()
    return "".join(reversed_phrase)