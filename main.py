# logic function
def recharge_station_list(recharging, distances, cities):
    original_capacity = recharging
    output_list = [cities[0]]

    for pos in range(len(distances)):
        if distances[pos] <= recharging / 2:
            recharging = recharging - distances[pos]
        else:
            recharging = original_capacity
            recharging -= distances[pos]
            output_list.append(cities[pos])

    output_list.append(cities[len(cities) - 1])

    return output_list


# Introduction and the complete problem state with required help menu.
print("\t\t________________________________________________________")
print("\n\t\t***** WELCOME TO THE ELECTRIC CAR TRAVELER PROBLEM *****")
print("\t\t________________________________________________________\n\n")
print("-->> Problem Statement <<--\n")
print("♦Given a capacity C in miles that represents the maximum number of miles your electric car can drive, "
      "n cities and (n-1) distances between two consecutive cities, design an algorithm that outputs the list L of "
      "cities where one need to stop and charge the car such that:".ljust(40, '-'))
print("\t- L is if minimum length among all possible list of cities.")
print("\t- The starting city, which is the first city, is the first element of L.")
print("\t- The destination city, which is the last city, is the last element of L.")
print("\t- If j and k are two consecutive cities in L, then when the car is in city j, the car is able to drive to "
      "city k and back to the city before city k, in case the charge station in city k is broken.\n\n")
print("!!BASIC INSTRUCTIONS!!\n")
print("\t>> Input Variables:\n\t\t - capacity = The capacity in miles upto which the electric car can travel.")
print("\t\t - n = The number of cities.")
print("\t\t - List_Cities = List of cities with relevant names.")
print("\t\t - Dist_Cities = List of distances in order for the input cities.\n")
print("\t>> Output Variables:\n\t\t")
print("\t\t - List_Recharging_Cities = A list of city where the car recharge itself.\n\n\n")
print("________________________________________________Let's "
      "Begin________________________________________________\n\n")

# input variables with constraints
# capacity in miles where capacity can be between 250 and 350
capacity = int(input("Please enter the total capacity (integer) in the range 250-350:"))

while capacity not in range(250, 351):
    print("Invalid Input")
    capacity = int(input("Please enter the total capacity (integer) in the range 250-350:"))
    if (capacity >= 250) and (capacity <= 350):
        break

# number of cities (integer) between 3-20
number_cities = int(input("Enter the number of cities(integer between 3-20):"))
while number_cities not in range(3, 21):
    print("Invalid Input")
    number_cities = int(input("Enter the number of cities(integer between 3-20):"))
    if (number_cities >= 3) and (number_cities <= 20):
        break

# list of cities
list_cities = []
print("Enter the name of the cities:")
for position in range(number_cities):
    element = str(input())
    list_cities.append(element)

# entering the distances between the cities
list_dist = []
print("Enter the distances between cities in order:")
for position in range(number_cities - 1):
    element = int(input())
    while (element < 10) or (element >= capacity / 2):
        print("Invalid Input!!! Please enter the distances between cities in order:")
        element = int(input())

    list_dist.append(element)

length = len(list_dist)

print("Name of cities where the car is recharged:", recharge_station_list(capacity, list_dist, list_cities))
end_of_program = input("Press any key to close the application!")
