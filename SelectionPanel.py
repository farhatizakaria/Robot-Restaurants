import time

print('This is our menu')
time.sleep(3)
refuse = ['nothing','none','nope','nah'] #refusal for the customer not order
accept = ['I want to order something','order','im ready','ill order'] #customer is ready to order
response = raw_input('welcome to our automated restaurant ! ')
class Refusal:
    if response in refuse:
        time.sleep(1)
        print('of course, would like more time?')
class Acceptance:
    if response in accept:
        def acceptance(self):
        time.sleep(2)
        print('Ok write it !')
        drinks = ['coffie','tie','juice','lemonade']
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

