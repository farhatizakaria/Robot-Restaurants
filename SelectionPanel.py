import time
print('Welcome to the Selection Panel !')
time.sleep(3)
refuse = ['nothing','none','nobe']
accept = ['I wanna something','order']
reponse=raw_input('So what the want! order or nothing! ')
if reponse in refuse:
    time.sleep(2)
    print('Alright sir')
elif reponse in accept:
    time.sleep(2)
    print('Ok write it !')
    drinks = ['coffie','tie','juice','lemonad']
    meals = ['meat','chiken','lamp']
    code_wifi = 'azer1234'
    choice=raw_input()
    if choice in drinks:
        time.sleep(2)
        print('You wanna drink !')
        time.sleep(2)
        print('Please be patient your drink will be ready soon !')
        time.sleep(6)
        print('Alright check it up your drink !')
        time.sleep(3)
        print('I hope you love it')
    elif choice in meals:
        time.sleep(2)
        print('You wanna eat a awesome meal !')
        time.sleep(2)
        print('Please be patient your meal will be ready soon !')
        time.sleep(6)
        print('Alright check it up your meal !')
        time.sleep(3)
        print('I hope you love it')
    else:
        time.sleep(2)
        print('We are so sorry honey your order not avaibable in our resturant !')
else:
    print('We are so sorry honey your order not avaibable now ! good luck in other time')

