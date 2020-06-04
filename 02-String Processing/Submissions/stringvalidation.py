# Student Name: Ali Al-Musawi
# Student ID: aalmusaw

# This module defines several functions that validate string inputs.
# In the case an input is invalid, the function prints an error message.
# By default, all strings are invalid.
# Once each function determines that the string is valid, then the function will return 'True'.

# This function validates full names.
# @param fullname is a string that the function validates.

def checkName(fullname):
    ValidName = False
    position = 0
    SpaceCounter = 0
    while position < len(fullname):
        if not fullname[position].isalpha():                    # Test 1: Is it not a letter?
            if position != 0 and fullname[position] == " ":         # Case 1A: Is it a space?
                SpaceCounter += 1
                position += 1
                continue
            elif position != 0 and position != (len(fullname) - 1) \
                    and fullname[position] == "-":                  # Case 1B: Is it a hyphen?
                if not fullname[position - 1].isalpha() or not fullname[position + 1].isalpha():
                    print('A hyphen must only separate letters.')
                    break
                else:
                    position += 1
                    continue
            else:                                                   # Case 1C: Is it a number or a symbol?
                print('Error. You must begin and end with letters. Only letters, a space, or a hyphen are allowed.')
                print('Numbers and other characters are not allowed.')
                break
        elif position == 0 and not fullname[position].isupper():   # Test 2: Is the first name capitalized?
            print('Error. The first name must start with an upper case letter.')
            break
        elif position != 0 and fullname[position - 1] == " " \
                and not fullname[position].isupper():              # Test 3: Is the last name capitalized?
            print('Error. The last name must start with an upper case letter.')
            break
        else:                                                      # Great! This letter passed all tests. Move on!
            position += 1

    # We are out of the loop. It either got broken or the loop finished successfully.
    if position == len(fullname) and SpaceCounter != 1:            # Do we have more than a single blank space?
        print('Error. You must enter at most a single blank space to separate the first and last name.')
    elif fullname[-1].isspace():                                   # Do we have a last name?
        print('Error, you must enter your last name.')
    elif position < len(fullname):                                 # Did we break out of the loop?
        pass
    else:                                                          # Did we finish the loop successfully?
        ValidName = True                                           # Hooray!
    return ValidName

# This function validates email addresses.
# @param email_address is a string that the function validates.
def checkEmail(email_address):
    ValidEmail = False
    position = 0
    while position < len(email_address):
        if not email_address[position].isalnum():              # Test 1: Is it not a letter or a number?
            if position != 0 and position != (len(email_address) - 1) \
                    and email_address[position] == "@":             # Test 1A: Is it @ symbol?
                if not (email_address[position - 1].isalnum() and\
                        email_address[position + 1].isalpha()):       # Test 1Aa: Is the @ in the right place?
                    print('Error. The symbol @ must separate the Domain Name and the Local-Part (User Name)')
                    print('Letters/Numbers must precede the @ symbol. Only letters can immediately follow the @ symbol.')
                    break
                else:
                    postAt = position + 1
                    while postAt < len(email_address):
                        if not email_address[postAt].isalpha():
                            if email_address[postAt] == ".":
                                postAt += 1
                                pass
                            else:
                                print('Error. Only letters then a dot symbol may follow the @ symbol.')
                                break
                        else:
                            postAt += 1

                    if postAt < len(email_address):
                        break
                    else:
                        position += 1
                        continue
            elif position != 0 and position != (len(email_address) - 1) and \
                    email_address[position] == ".":                 # Test 1B: Is it . symbol?
                if not (email_address[position - 1].isalpha()\
                        and email_address[position + 1].isalpha()):     # Test 1Ba: Is it separating the right things?
                    print('Error. The Domain Name must consist of letters followed by dot followed by 3 letters.')
                    break
                elif not (email_address.endswith(".com", position, position+4) or \
                          email_address.endswith(".net", position, position+4) or \
                          email_address.endswith(".ca", position, position+3) or \
                          email_address.endswith(".org", position, position+4)): # Test 1Bb: Is it in the right place?
                    print('Error. The Domain Name must end with either of: ".com" or ".net" or ".ca" or ".org".')
                    print('The dot symbol may only precede the 4 suffixes above immediately. No other use of the dot is allowed.')
                    break
                else:
                    position += 1
                    continue
            else:                                                  # Test 1C: Is a symbol other than '@' or '.' ?
                print('Error. No symbols other than "@" and "." are allowed.')
                print('The email address must be in the form: "abcd123@xxmail.com" or any other variant suffix:')
                print('.net, .org, .ca')
                break
        else:                                                      # Test 2: Is it a letter/number?
            position += 1

    # Now we are outside of the loop.
    if position < len(email_address):                               # Did we break out of the loop?
        pass
    elif "@" not in email_address:                                  # Is there a "@" ?
        print('Error. The email address must contain an @ symbol.')
    elif "." not in email_address:                                  # Is there a "."?
        print('Error. The email address must contain a dot symbol.')
    else:                                                           # Did we finish the loop successfully?
        ValidEmail = True                                           # Hooray!
    return ValidEmail

# This function validates passwords
# @param password is a string that the function validates

def checkPassword(password):
    ValidPassword = False
    position = 0
    lowercaseCounter = 0
    uppercaseCounter = 0
    spaceCounter = 0
    numberCounter = 0
    while position < len(password):     # The loop's job is to count the frequency of each significant character.
        if password[position].isalpha():
            if password[position].islower():
                lowercaseCounter += 1
            else:
                uppercaseCounter += 1
        elif password[position].isnumeric():
            numberCounter += 1
        elif password[position] == " ":
            spaceCounter += 1
        else:
            pass
        position += 1
    # Now that the loop finished its job, we validate the password based on the minimum requirements:
    if len(password) < 8:
        print("Error. The password must be at least 8 characters long.")
    elif spaceCounter > 0:
        print("Error. Spaces are not allowed.")
    elif lowercaseCounter < 1:
        print('Error. There must be at least one lower case letter.')
    elif uppercaseCounter < 1:
        print('Error. There must be at least one upper case letter.')
    elif numberCounter < 1:
        print('Error. There must be at least one numeric digit.')
    else:
        ValidPassword = True        # Hooray!
    return ValidPassword

# This function validates physical addresses.
# @param address is a string validated by the function.

def checkAddress(address):
    ValidAddress = False
    position = 0
    if not (len(address)>0 and address[0].isnumeric()): # This is a preliminary test. Does it even start with a number?
        print('Error. The address must start with the street number.')
    else:
        position_num = 0
        while position_num < len(address):      # This loop locates the end of the street number.
            if address[position_num].isnumeric():
                LAST_DIGIT_POSITION = position_num
            else:
                break
            position_num += 1
        position = LAST_DIGIT_POSITION + 1
        while position < len(address):          # This loop checks if there are special characters.
            if not address[position].isalpha() and not address[position] == " ":
                print('Error. No special characters are allowed. Only letters separated by space may follow the street number.')
                break
            position += 1
# The loop is over now. Let's see if the address provided is valid.
    if len(address) == 0:
        print('You must enter a value')
    elif position < len(address):       # Did we break out of the loop?
        pass                            # No good.
    elif address[-1].isspace():         # Is there a street name?
        print('You cannot have a space at the end.')
    elif address[-1].isnumeric():
        print('Please enter the street name.')
    else:                               # Did we finish the loop successfully?
        ValidAddress = True             # Hooray!
    return ValidAddress



