#Function that takes no argument, asks user for a sentence, splits the sentence in order to use for loop more effeciently
def average():
    user_string = input("Enter a sentence: ")
    words = user_string.split()
    word_count = 0
    total_char = 0
    for word in words:
        word_count += 1
        total_char += len(word)
        return(total_char / word_count)

print(average())

