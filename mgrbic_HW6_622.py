def mirror(string):
    mirror = {'b':'d', 'd':'b', 'i':'i', 'l':'l', 'm':'m', 'n':'n', 'o':'o', 'p':'q', 'q':'p', 'v':'v', 'x':'x'}
    mirror_word = ''
    
    i = len(string) - 1
    x = 0
    while i >= 0:
        mirror_word = mirror_word + string[i]
        i = i - 1
        x += 1
    if x == len(string):
        print(mirror_word)
    else:
        print("INVALID")


#Main/Test
user_input = input("Please enter a string to get the mirror version: ")
mirror(user_input)

