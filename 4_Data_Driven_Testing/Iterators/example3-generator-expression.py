# b = (2*x for x in range(20))
# type(b)
# b.__next__()
# for i in b:
#     print(b, end=' ')

gen = (i for i in range(10) if i % 2 != 0)

# for k in gen:
#     print(k, end=' ')

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))