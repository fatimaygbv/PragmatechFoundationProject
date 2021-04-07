def checkVoidOrReturn(func):
    def wrapper():
        if type(func())=='None':
            print(f'{func.__name__} methodu void methoddur')
        else:
            print(f'{func.__name__} methodu return methoddur')
    return wrapper

@checkVoidOrReturn
def Foo():
    return 5

@checkVoidOrReturn
def Bar():
    print(5)

print(Bar())    