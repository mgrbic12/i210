#Was unsure which way to do it: Input from the user, or just print the variable the question had. So here is both!
#This takes input from user and display it with user input
sender = input("sender = ")
recipient = input("recipient = ")
subject = input("subject = ")

print()

print("From: {}\nTo: {}\nSubject: {}\n".format(sender, recipient, subject))

print()
#This the layout the question had with the variable from the question
sender = "tim@abc.com"
recipient = "tom@xyz.org"
subject = "Hello!"
print("From: {}\nTO: {}\nSubject: {}\n".format(sender,recipient, subject))
