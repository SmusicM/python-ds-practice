def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    reverse = list(phrase)
    resultrev = reversed(reverse)
    result = "".join(resultrev)
    print(result)
    
