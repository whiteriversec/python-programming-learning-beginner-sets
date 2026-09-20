#Given a list of numbers and a target value, search the list and print whether the target was **found** or **not found**.
#
#```python
#numbers = [4, 12, 7, 19, 3, 25, 8]
#target = 19
#```

myList = [4, 12, 7, 19, 3, 25, 8]
found = False;
userNumber = int(input('Pick a number: '))

for i in myList:
    print("Number: " + str(i))
    if i == userNumber:
        print("We found " + str(userNumber))
        found = True;
        break;

if found == False:
    print('Number not found.')