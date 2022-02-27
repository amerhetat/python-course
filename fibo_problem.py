

def isprime(number):
    counter = 0
    output = False
    for i in range(1,number+1):
        rem = number%i
        if rem ==0:
            counter += 1

    if counter ==2:
        output = True
    return  output

def iseven(number):
    output = False
    rem = number%2
    if rem == 0:
        output = True

    return output

def isodd(number):
    output = False
    rem = number%2
    if rem != 0:
        output = True

    return output
def fibosec(limit):
    fibo_list = [1, 1]
    n = 2
    an = 1
    while an < limit:
        an = fibo_list[n - 1] + fibo_list[n - 2]
        fibo_list.append(an)
        n += 1
    fibo_list = fibo_list[:-1]
    return fibo_list


## main code ##
limit = 100
fibo_list = fibosec(limit)
print('fibonacci sequence: ')
print(fibo_list)
print('--------------------')
listODD = []
listEVEN = []
for number in fibo_list:
    ## check if number is odd
    out1 = isodd(number)
    if out1 ==True:
        listODD.append(number)
    ## check if number is even
    out1 = iseven(number)
    if out1 ==True:
        listEVEN.append(number)
print('odd numbers:')
print(list(set(listODD)))
print('-----------------')
print('even numbers:')
print(listEVEN)
print('-----------------')