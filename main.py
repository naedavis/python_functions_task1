#Calculating trip Cost
#calculates hotel cost per night
def hotel_cost(nights):
    return 140 * nights

#returns different place depending on cost
def plane_ride_cost(city):
    if city == "Cape Town":
        return 2500
    elif city == "Durban":
        return 2300
    elif city == "JHB":
        return 2000
    else:
        return 1800

#cost for renting a car
def trip_cost(days):
    cost = days * 40
    if days >= 3:
        return cost - 20
    elif days >= 7:
        return cost - 50
    else:
        return cost




