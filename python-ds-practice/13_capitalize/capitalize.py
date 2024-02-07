def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """
    if phrase.isspace():
        return phrase[0]+ phrase[1:]
    elif not phrase.isspace():
        return phrase.capitalize()