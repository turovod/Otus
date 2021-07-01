def ddd():
    for i in 'fasdffghdfghjhfgj':
        yield i

a = ddd()
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
