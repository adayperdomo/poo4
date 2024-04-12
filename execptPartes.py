values = [4, 2, 7]

try:
    r = values[2]
except IndexError:
    print('Error: Index not in list')
else:
    print(f'Your wishes are my command: {r}')
finally:
    print('Have a good day!')