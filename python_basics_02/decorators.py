def outer(message):
    print('In the outer function')
    
    def inner():
        print('calling the inner function')
        print(message)
        
    return inner
# f = outer('keep challenging yourself')
# f()

'''def decorator(original_func):
    print('In the decorator function\n')
    def wrapper():
        print(f'wrapper executed before {original_func.__name__}()')
        
        if 10>5:
            print('Yes, Interesting and I like it')
        
        return original_func() 
    return wrapper

'''
# Using decorator: OneWay
'''def print_something():
    print('print_Something is being executed') 
decorated_f=decorator(print_something)
decorated_f()'''
'''
# Using decorator: the OtherWay
@decorator
def print_something():
    print('print_Something is being executed') 
print_something()'''




def decorator_2(original_func):
    print('In the decorator_2 function\n')
    def wrapper(*args, **kwargs):
        print(f'wrapper executed before {original_func.__name__}()')
        
        if 10>5:
            print('Yes, Interesting and I like it')
        
        return original_func(*args, **kwargs) 
    return wrapper


@decorator_2
def print_something_more(arg1,arg2):
    print(f'printing argument_1={arg1} and argument_2={arg2}') 
    

print_something_more(2,3)