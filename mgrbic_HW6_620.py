def reverse(phoneBook):
    reversePhoneBook = {}

    for key in phoneBook:
        key2 = phoneBook[key]
        reversePhoneBook[key2] = key
    return reversePhoneBook

#Main/test
phoneBook = {'Smith, Jane' : '1-765-987-6432', 'Doe, John' : '1-765-654-9087'}
print(reverse(phoneBook))

