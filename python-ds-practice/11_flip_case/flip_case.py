def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    result = ""
    for swapchar in phrase:
        if swapchar.lower() == to_swap.lower():
            result += swapchar.swapcase()
        else:
            result += swapchar
    return result
    
flip_case('Aaaahhh', 'a')