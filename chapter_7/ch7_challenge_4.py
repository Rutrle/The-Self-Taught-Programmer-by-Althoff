

numbers =[5,22,36,49]
while True:
    user_input=input('Enter "q" to qout \nGuess a number from 0 to 50')
    if user_input =='q':
        break
    elif int(user_input) in numbers:
        print('you have guessed one of the numbers correctly')

    else:
        print('Wrong guess, try again!')





