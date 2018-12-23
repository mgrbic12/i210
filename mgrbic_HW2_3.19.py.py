a, b, c = eval(input("Define a, b, c !: "))

if a < b or c < b or (a + b) == c or ((a ** 2) + (b ** 2)) == (c ** 2):
    print("Ok")
else:
    print("Not Ok")
