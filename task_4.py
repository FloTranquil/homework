#Декоратор, считающий и выводящий количество вызовов декорируемой функции.

def counter(func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        result = func(*args, **kwargs)
        print("{0} вызвана: {1} раз(а)".format(func.__name__, wrapper.count))
        return result
    wrapper.count = 0
    return wrapper
@counter
def foo(a, b):
    return a ** b
foo(10, 5)
foo(5, 2)
