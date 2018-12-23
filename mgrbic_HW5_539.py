def exclamation(string):
    new_string = " "
    for i in string:
        if ( i == "a" or i == "e" or i == "i" or i == "o" or i =="u"):
            new_string = new_string + (i * 4)
        else:
            new_string = new_string + i
    final_string = new_string
    print (final_string + "!")

user_input = input("Enter a string: ")
exclamation(user_input)
