func = lambda *args: len(args)

def func2(**kwargs):
    return [tuple(kwargs.keys()), tuple(kwargs.values())]

print(func())
print(func(1))
print(func(1, 2))
print(func(1, 'gjg', 3))

print(func2(x='йогурт "Фруктовый взрыв"', y='с эффектом', z='расстройства', w='кишечника'))

input('Press enter to exit')