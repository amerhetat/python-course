
x = 3
d = {'name': 'moien'}
list1 = [2,2,2,2]
try:
    y = x+3
    s = d['name']
    a = list1[10]
except NameError:
    print('some variable names is not defined!!')
except KeyError:
    print('some keys use befor define in dictionary!!')
except IndexError:
    print('an index is greater than list length!!')
finally:
    print('process done!!')



