def vowelCount(string):
    a_total = string.count("a")
    e_total = string.count("e")
    i_total = string.count("i")
    o_total = string.count("o")
    u_total = string.count("u")
    print("a, e, i, o, and u appear, respectively, {1}, {2}, {3}, {4}, {5} times".format(a_total, e_total, i_total, o_total, u_total)

user_string = input("Enter a string: ").lower()
vowelCount(user_string)


