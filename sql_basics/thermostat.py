temps = [5, 12, 25, 8, 30]

def count_overheating(temperatures, limit):
    counter = 0
    for temperature in temperatures:
        if temperature >= limit:
            counter = counter + 1
    return counter
print(count_overheating(temps, 15))