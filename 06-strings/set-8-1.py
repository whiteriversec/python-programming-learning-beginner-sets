name = input('Enter your name: ')

def capitalise_first_letter(name):
    firstLetter = name[0].upper()
    restOfName = name[1:].lower()
    new_name = firstLetter + restOfName
    return new_name

print(capitalise_first_letter(name))

    