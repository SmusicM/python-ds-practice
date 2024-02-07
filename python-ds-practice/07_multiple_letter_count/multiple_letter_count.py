def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
#    for word in phrase:
#       for letter in list(word):
#           count = list(word).count(letter)
#           print(f"{letter}:{count}")
    ltrcount = {}
    for char in phrase:    #loops
        if char.isalpha():                #check if letter                  
            ltrcount[char] = ltrcount.get(char,0)+1  #ltrcount updated at its char index = get char andd its key value (char/phrase) and 0 if none, +1 iterates again each time ,pushes onto ltrcount
    print(ltrcount)