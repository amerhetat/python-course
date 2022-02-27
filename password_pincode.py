defaul_pincode = '1357'
user_pin = ''
correctpin = False
from time import sleep
## check pin code
for counter in range(1,3):
    for chance in range(1,4):
        ## get and check format pin code from user
        for i in range(100):
            user_pin = input('-Please enter 4 digit pin code: ')
            if user_pin.isnumeric() and len(user_pin) == 4:
                break
            else:
                print('-Pin code format is wrong! try again!')
        # print('your pin code is %s .' % user_pin)


        if defaul_pincode == user_pin:
            print('device unlocked!!!')
            correctpin = True
            break

        else:
            if chance==3:
                if counter==1:
                    print('you have no more chance! try again in 10 second!')
                    sleep(2)
                else:
                    print('you have no more chanse!! call with costumer support!!')

            else:
                print('wrong pin code! try again!! you have %i more chance' %(3-chance))
    if correctpin == True:
        break










