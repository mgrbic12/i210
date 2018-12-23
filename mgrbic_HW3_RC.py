import random

user_words = eval(input("Please enter a list of words: "))

num_of_movies = eval(input("Please enter a number of movies you'd like to generate: "))

print("Welcome to Randoplex! Currently playing movies are: ")
for i in range(len(user_words)):
    print(random.choice(user_words) + " " + random.choice(user_words) + " " + random.choice(user_words) + "")
