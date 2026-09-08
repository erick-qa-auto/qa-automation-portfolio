brands = ["Carel", "Carel", "Danfoss", "Danfoss", "Unox", "Eliwell"]

def count_brand(brand):
    counter = 0
    for item in brands:
        if item == brand:
            counter = counter + 1
    return counter

#print(count_brend("Carel"))