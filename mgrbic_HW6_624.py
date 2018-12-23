def names():
    students = []
    next_name = ' '

    while True:
        next_name = input("Enter next name: ")
        if next_name == '':
            break
        else:
            students.append(next_name)

    
    for item in set(students):
        print("There is {0} student(s) named {1}".format(students.count(item), item))

        
#Used set(students) and it elimated the duplicate outputs I was obtaining.
#Originally it printed the output correctly but with duplicates corresponding with how many times the students name was there


        
