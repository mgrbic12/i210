def evenrow(numbers):
    numsum = 0
    for num in numbers:
        numsum = sum(numbers)
        if numsum % 2 == 0:
            print("True")
        else:
            print("False")

                
user_input = eval(input("Enter a list of numbered pairs: "))
evenrow(user_input)
