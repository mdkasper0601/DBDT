#Travelling salesman problems
from sys import maxsize

#task 1

#parcels_arrangment function


def parcels_arrangment(optimum_path_in_letter, list_parcels):
    parcels_arranged = []
    truck_slot = []

    for i in range(len(optimum_path_in_letter)):
        for j in range(len(list_parcels)):
            if optimum_path_in_letter[i] in list_parcels[j]:
                truck_slot.append(list_parcels[j])

        parcels_arranged.append(truck_slot)
        truck_slot = []

    return parcels_arranged

#truck_loading function


def truck_loading(parcels_arranged):
    vehicle = []
    door1 = []
    door2 = []
    for i in range(len(parcels_arranged)):
        if i % 2 == 0:
            door1.append(parcels_arranged[i])
        else:
            door2.append(parcels_arranged[i])
    vehicle.append(door1)
    vehicle.append(door2)

    return vehicle

#truck_unloading function


def truck_unloading(vehicle):
    temp = 0
    while len(vehicle[0]) != 0 or len(vehicle[1]) != 0:
        if temp % 2 == 0:
            vehicle[0].pop(0)
        else:
            vehicle[1].pop(0)
        temp += 1
        print(vehicle)
    return vehicle


def truck_loading1(parcels_arranged):
    for i in range(len(parcels_arranged) // 2):
        parcels_arranged[i], parcels_arranged[-1 -i] = parcels_arranged[-1 - i], parcels_arranged[i]

    return parcels_arranged


def truck_unloading1(parcels_arranged):
    for i in range(len(parcels_arranged)):
        parcels_arranged.pop(0)
        print(parcels_arranged)
    return parcels_arranged


#task 2
#generate all possible solutions
def possible_solution(tsp):
    if len(tsp) == 0:
        return []
    elif len(tsp) == 1:
        return [tsp]

    ran_solution = []
    for i in range(len(tsp)):
        route = tsp[i]
        #Extract tsp[i] or route from the list, remain_tsp is the remaining list
        remain_tsp = tsp[:i] + tsp[i+1:]
        #generating all permutaions where route is the first element
        for j in possible_solution(remain_tsp):
            ran_solution.append([route] + j)

    return ran_solution

#implementation of travelling salesman problem


def travellingsaleman(tsp, s):

    #store all vertex apart from source vertex
    vertex = []
    for i in range(len(tsp)):
        if i != s:
            vertex.append(i)

    min_cost = maxsize
    possible_path = possible_solution(vertex)

    cost = []
    optimum_path = []
    optimum_path_in_letter = []

    for i in possible_path:
        current_cost = 0

        #calculate current cost
        k = s
        for j in i:
            current_cost += tsp[k][j]
            k = j
        current_cost += tsp[k][s]

        #update minimum and store all the cost coressponding to each path
        min_cost = min(min_cost, current_cost)
        cost.append(current_cost)

    #append the paths with the smallest cost to the array
    for i in range(len(cost)):
        if cost[i] == min_cost:
            optimum_path.append(possible_path[i])
    for i in optimum_path[0]:
        if i == 1:
            optimum_path_in_letter.append("B")
        elif i == 2:
            optimum_path_in_letter.append("C")
        elif i == 3:
            optimum_path_in_letter.append("D")
    return optimum_path_in_letter

#sample program


def main():
    #sample graph
    tsp = [[0, 10, 15, 20],
           [10, 0, 35, 25],
           [15, 35, 0, 30],
           [20, 25, 30, 0]]

    a = int(input(""" 
    please enter kind of truck that you want: 
        1. 1 door
        2. 2 doors """))

    if a == 1:
        real_optinum_path = ['A', ]
        for i in range(len(travellingsaleman(tsp, 0))):
            real_optinum_path.append(travellingsaleman(tsp, 0)[i])
        real_optinum_path.append('A')
        print(real_optinum_path)
        list_parcels = ["B", "D", "C", "D", "C", "B", "D", "C", "C", "B", "D"]
        print(parcels_arrangment(travellingsaleman(tsp, 0), list_parcels))
        print(truck_loading1(parcels_arrangment(
            travellingsaleman(tsp, 0), list_parcels)))
        truck_unloading1(truck_loading1(parcels_arrangment(
            travellingsaleman(tsp, 0), list_parcels)))

    elif a == 2:
        real_optinum_path = ['A', ]
        for i in range(len(travellingsaleman(tsp, 0))):
            real_optinum_path.append(travellingsaleman(tsp, 0)[i])
        real_optinum_path.append('A')
        print(real_optinum_path)
        list_parcels = ["B", "D", "C", "D", "C", "B", "D", "C", "C", "B", "D"]
        print(parcels_arrangment(travellingsaleman(tsp, 0), list_parcels))
        print(truck_loading(parcels_arrangment(
            travellingsaleman(tsp, 0), list_parcels)))

        truck_unloading(truck_loading(parcels_arrangment(
            travellingsaleman(tsp, 0), list_parcels)))
    else:
        print('please run the programn again')


if __name__ == "__main__":
    main()
