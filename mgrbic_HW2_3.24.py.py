#User inputs a list of words

word_list = eval(input("Enter a list of words!['cia', 'secret', 'etc']: "))

#if statement to determine if "secret' is in the list

if "secret" in word_list:
    word_list.remove("secret")
    
#for loop to print out names vertically
    
print()
    
for word in word_list:
    print(word)

