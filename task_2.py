#9. You need to write a function that reverses the words in a given string. A word can also fit an empty string. If this is not clear enough, here are some examples. As the input may have trailing spaces, you will also need to ignore unneccesary whitespace.

x = input()
def revers(x):
    x = x.split()
    x.reverse()
    for i in x:
        print(i, end=' ')
    print()
revers(x)
