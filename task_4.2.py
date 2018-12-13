def decorator(func):
    def wrapper(*args, **kwargs):
        print ("Hello!", *args, **kwargs)
        result = func(*args, **kwargs)
    return wrapper

@decorator
def full_name(first_name, last_name):
    print ('My name is', first_name, last_name)

full_name('Flo', 'Tranquil')
