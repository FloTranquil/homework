#Параметризуемый декоратор, добавляющий тэги.

def tag (tag):
    def decorator (func):
        def wrapper (*args, **kwargs):
            result = func(*args, **kwargs)
            return f'<{tag}>{result}</{tag}>'
        return wrapper
    return decorator
@tag('b')
@tag('tag')
def foo(): 
    return 'BlueBear'
foo()
