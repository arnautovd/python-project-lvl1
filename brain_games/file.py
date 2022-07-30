def cons(x, y):
    return lambda f: f(x, y)
# def cons(x, y):
#     def f(function):
#         return function(x, y)
#     return f

a = cons(['hello', 'ivan'], 'b')


def car(pair):
    return pair.__closure__[0].cell_contents

def cdr(pair):
    return pair.__closure__[1].cell_contents

print(car(a))
print(cdr(a))