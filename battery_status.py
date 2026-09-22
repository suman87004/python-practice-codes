# battery_status

def battery_status(level):
    if(level > 80):
        return "full"
    
    elif(level > 50 and level <= 79):
        return "good"

    elif(level > 20 and level <= 49):
        return "low", "below"

    else:
        return "critical"


print(battery_status(82))
print(battery_status(45))
print(battery_status(15))
print(battery_status(18))
