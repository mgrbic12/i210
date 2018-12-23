def av_nums(first3_nums):
    average_of_nums = (sum(first3_nums)) / 3
    return(average_of_nums)


#User number input

first_num = eval(input("Enter first number: "))
second_num = eval(input("Enter second number: "))
third_num = eval(input("Enter third number: "))
fourth_num = eval(input("Enter last number: "))
first3_nums = first_num, second_num, third_num

average_of_nums = av_nums(first3_nums)

if average_of_nums == fourth_num:
    print("Equal")
else:
    print("Not Equal")


               
