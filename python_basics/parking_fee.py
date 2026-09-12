def parking_cost(minutes):
    if minutes <= 0:
        return None
    if minutes <= 30:
        price = 50
    elif minutes <= 120:
        price = 150
    else:
        price = 300
    return price
print(parking_cost(15))
print(parking_cost(60))
print(parking_cost(200))
print(parking_cost(-5))