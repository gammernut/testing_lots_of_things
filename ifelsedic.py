price_list = {
    'fish': 8,
    'beef': 7,
    'broccoli': 3,
}


# find price clunky ver
# def find_price(item):
#     if item in price_list:
#         return 'The price for {} is {}'.format(item, price_list[item])
#     else:
#         return 'The price for {} is not available'.format(item)
#
#
# print(find_price('fish'))
# print(find_price('cauliflower'))

# find price better ver
# def find_price(item):
#     return f'The price for {item} is {price_list.get(item, "not available")}'
#
#
# print(find_price('fish'))
# print(find_price('cauliflower'))


# operations worse ver
# def operations(operator, x, y):
#     if operator == 'add':
#         return x + y
#     elif operator == 'sub':
#         return x - y
#     elif operator == 'mul':
#         return x * y
#     elif operator == 'div':
#         return x / y
#
#
# operations('mul', 2, 8)


# operations better ver
# def operations(operator, x, y):
#     return {
#         'add': lambda: x + y,
#         'sub': lambda: x - y,
#         'mul': lambda: x * y,
#         'div': lambda: x / y,
#     }.get(operator, lambda: 'Not a valid operation')()
#
#
# print(operations('mul', 2, 8))
# print(operations('unknown', 2, 8))

# x = lambda a: a + 10
# print(x(5))
#
# x = lambda a, b: a * b
# print(x(5, 6))
#
# x = lambda a, b, c: a + b + c
# print(x(5, 6, 2))


# def myfunc(n):
#     return lambda a: a * n
#
#
# mydoubler = myfunc(2)
#
# print(mydoubler(11))


def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))
