def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """

    vowels = []
    vowel_idx = []
    s_lst = list(s)

    for idx in list(range(0, len(s))):
        if 'aeiou'.count(s[idx].lower()) > 0:
            vowels.append(s[idx])
            vowel_idx.append(idx)

    vowels.reverse()

    for num in list(range(0, len(vowels))):
        s_lst[vowel_idx[num]] = vowels[num]

    return "".join(s_lst)
    