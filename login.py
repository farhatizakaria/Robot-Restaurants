print('Please fill the next requirements ')

userName_db = 'Zakaria'     #Data base of user name !
userPassword_db = 1234      #Data base of password !  
user_name = raw_input('Enter your name: ')  #We ask the user about name
user_password = input('Enter your password: ')  #We ask the user about password
#We comparing between Data
if userName_db == user_name and userPassword_db == user_password:
    #When the Data is correct !
    import SelectionPanel
else:
    print('Your data are false !')
    #When the Data is incorrect !
    


