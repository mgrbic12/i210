def translate(dictionary):
    print("Welcome to this translation service!")

    user_word = ' '
    while user_word != 'Quit':
        user_word = input("Please enter a word: ")
        if user_word in dictionary:
            print("The translation is:", dictionary[user_word] + '.')
        else:
            print("The translation is: ____")
    
