# speed_level

def speed_level(speed):
    if(speed > 120):
        return "very fast"

    elif(speed > 80 and speed <= 120):
        return "fast"

    elif(speed > 40 and speed <= 79):
        return "normal", "below"

    else:
        return "slow"


print(speed_level(122))
print(speed_level(90))
print(speed_level(50))
print(speed_level(32))