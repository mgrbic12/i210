names = eval(input("Please enter a list of student names!: "))
first_letter = ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'I', 'i', 'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm']
for name in names:
    if name[0] in first_letter:
        print(name)

        
