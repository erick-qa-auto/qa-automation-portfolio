def calculate_shipping_cost(weight_kg, distance_km, is_express=False):
    if weight_kg <= 0 or distance_km <= 0:
        return None
    
    base_cost = 5.0
    
    if weight_kg <= 1:
        weight_cost = 2.0
    elif weight_kg <= 5:
        weight_cost = 5.0
    elif weight_kg <= 20:
        weight_cost = 10.0
    else:
        weight_cost = 20.0
    
    distance_cost = distance_km * 0.1
    
    total = base_cost + weight_cost + distance_cost
    
    if is_express:
        total *= 1.5
    
    return round(total, 2)