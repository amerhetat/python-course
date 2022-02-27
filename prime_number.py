user_number = int(input('Enter a number: '))
counter =0
for i in range(2,user_number):
    rem1 = user_number%i
    if rem1==0:
        counter +=1

if counter==0:
    print('number is prime!!')
else:
    print('number is not prime!!')