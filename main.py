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
def rental_cost(days):
    cost = days * 40
    if days >= 3:
        return cost - 20
    elif days >= 7:
        return cost - 50
    else:
        return cost

# trip cost returns sum of calling all previously defined functions

def trip_cost(city, days):
    city = plane_ride_cost(city)
    days = rental_cost(days) + hotel_cost(days)
    return city + days

# modified trip_cost function
def trip_cost(city, days, spending_money):
    city = plane_ride_cost(city)
    days = rental_cost(days) + hotel_cost(days) + spending_money
    return city + days + spending_money





