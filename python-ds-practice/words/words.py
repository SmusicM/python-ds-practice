def print_upper_words(words):
    """ for returning word of words in uppper case
    like print_upper_words("hello","lets","dog")
    shoould return ("HELLO","LETS","DOG")"""
    for word in words:
        print(word.upper())


    """for returning words back in uppercase that start with certain letters
       start_with=["x","y","z"] should only print word from words in caps that
       start with the start_with=
       ex: print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
        must_start_with={"h", "y"}) 
        should print those only starting with h y and in caps
        >>>    print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],start_with={"h", "y"})
               HELLO
               HEY
               YO
               YES   
    """
def print_upper_words_starting(words,start_with):
    for word in words:
        for letter in start_with:
            if word.startswith(letter):
                print(word.upper())
                break
          