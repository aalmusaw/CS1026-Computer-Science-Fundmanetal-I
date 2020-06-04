# Student Name: Ali Al-Musawi
# Student ID: aalmusaw

# This program imports functions that validate the inputs of the user
from stringvalidation import checkEmail, checkPassword, checkAddress, checkName

# Receive user input and validate.
InputName = input('Please enter your full name: ')
while checkName(InputName) == False:
    InputName = input('Please enter your full name: ')

InputEmail = input('Please enter your email address: ')
while checkEmail(InputEmail) == False:
    InputEmail = input('Please enter your email address: ')

InputPassword = input('Please enter your password: ')
while checkPassword(InputPassword) == False:
    InputPassword = input('Please enter your password: ')

InputAddress = input('Please enter your address: ')
while checkAddress(InputAddress) == False:
    InputAddress = input('Please enter your address: ')

# Print the validated information.
print('Thank You, ', InputName, '.', sep="")
print('Your email address is: ', InputEmail)
print('Your password is: ', InputPassword)
print('Your address is: ', InputAddress)

