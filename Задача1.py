user_name = str('Your name')
age_int = str('Your age')

age_int = int(34)

if 16 < age_int <70:
    print('Welcome', user_name, 'on our website.')
elif age_int == 16:
    print('Dear', user_name, 'need to wait one year')
elif 70 <= age_int <= 90:
    print('You are lucky',  user_name, 'and welcome.')
elif age_int > 121:
    print('You are not real', user_name)
else:
    print("I'm sorry", user_name, "you are too young.'")
