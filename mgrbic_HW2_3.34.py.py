def pay(wage, hrs_worked):
    if hrs_worked > 40:
        OT_pay = ((wage * 1.5) * (hrs_worked - 40)) + ( wage * 40 )
        return(OT_pay)
    else:
        weeks_pay = wage * hrs_worked
    return(weeks_pay)


wage = eval(input("Please enter your hourly wage: "))
hrs_worked = eval(input("Please enter how many hours were worked in a week: "))

total_pay = pay(wage, hrs_worked)

print("Your total pay for this week is!: ", total_pay)

