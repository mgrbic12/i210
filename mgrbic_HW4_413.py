s = 'abcdefghijklmnopqrstuvwxyz'

print("s =",s)

print()
#(a)
print("The slice consisting of the second and third character of 's' is 'bc':",s[1:3] == 'bc')

print()
#(b)
print("The slice consisting on the first 14 characters of 's' is 'abcdefghijklmn':", s[0:14] == 'abcdefghijklmn')

print()
#(c)
print("The slice of 's' excluding the first 14 characters is 'opqrstuvwxyz':",s[14:] == 'opqrstuvwxyz')

print()
#(d)
print("The slice of 's' excluding the first and last characters is 'bcdefghijklmnopqrstuvw':",s[1:-1] == 'bcdefghijklmnopqrstuvw')
