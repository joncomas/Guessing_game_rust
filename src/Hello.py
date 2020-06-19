# This program says hello and asks for my name ans age.
print('Hello World')
print('Hello, what is your name?') # asks for name. 
myName = input()
print('your name is ' + myName)
print('The length of your name is:')
print(len(myName))

print('What is your age?') #Asks for age.
myAge = input()
print('Your age is ' + myAge + ' now')
print('and you\'ll be ' + str(int(myAge) + 1) ' in a year.')
