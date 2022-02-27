


user_input_number = int(input('Enter a number: '))
ZeroRemNumber = 0
for range_num in range(1, user_input_number+1):
    rem = user_input_number%range_num

    if rem ==0:
        ZeroRemNumber += 1
prime_number_list = []
if ZeroRemNumber == 2:
    for range_num in range(1, user_input_number + 1):
        zeroremcounter = 0
        for counter in range(1, range_num+1):
            rem2 = range_num%counter
            if rem2==0:
                zeroremcounter += 1
        if zeroremcounter ==2:
            prime_number_list.append(range_num)
            # print('%i is prim' %range_num)
    print(prime_number_list)




else:
    zeroremlist = []
    for range_num in range(1, user_input_number + 1):
        rem3 = user_input_number%range_num
        if rem3==0:
            zeroremlist.append(range_num)

    print(zeroremlist)








