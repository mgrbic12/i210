#distance function
def distance(time_elapsed):
    speed = 340.29
    time = ((time_elapsed * speed) / 1000)
    return(time)

time_elapsed = eval(input("Please enter the time elapsed between the flash and the thunder: "))
print("The distance to the lightning strink is below in kilometers:")
print(distance(time_elapsed))
