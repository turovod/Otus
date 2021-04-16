def func(a, b):
    if a==b:
        return a
    elif a < b:
        return f'{b}', func(a, b - 1)
    elif a > b:
        return f'{a}', func(a - 1, b)


print(func(1, 10), end=' ')
print()
print(func(100, 90), end=' ')
print("bbbbbbbb")