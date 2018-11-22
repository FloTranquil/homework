#9. You need to write a function that reverses the words in a given string.
#A word can also fit an empty string.
#As the input may have trailing spaces, you will also need to ignore unneccesary whitespace.


words = input()
def revers(words):
    words = words.split()
    words = ' '.join(words[ : :-1])
    return words
revers(words)
