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
    vowels = "aeiouAEIOU"
    s_to_list = list(s)
    left,right = 0, len(s) -1
    while left < right:
        if s_to_list[left]in vowels:
            while right > left and s_to_list[right]not in vowels:
                right -=1
            if right> left:
               s_to_list[left],s_to_list[right]= s_to_list[left]
               right -= 1
        left += 1
    return "".join(s_to_list)