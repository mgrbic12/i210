#Function for lastF()
def lastF(FirstName, LastName):
    return(LastName, FirstName[0])

first = input("Please enter your first name: ")
last = input("Please enter your last name: ")

print(lastF(first, last))
