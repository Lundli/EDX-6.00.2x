###########################
# 6.00.2x Problem Set 1: Space Cows

from ps1_partition import get_partitions
import sys
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')

    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict

def total_weight(cowList):
    weight = 0
    for cow in cowList:
        try:
            weight += cows.get(cow)
        except:
            print("cow not found")
            # sys.exit()
    return weight

# Problem 1
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)

    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here

    def heaviest_cow(transported_list, cows_dict, max_weight):
        ### Helper function, will find heaviest cow that has max weight,
        ## returns name and weight
        heavy_name = ""
        heavy_weight = 0

        for name, weight in cows.items():
            if name not in transported_list:
                if max_weight >= weight > heavy_weight:
                    heavy_name = name
                    heavy_weight = weight
        if heavy_name == "":
            return None, None

        return heavy_name, heavy_weight




    # List of cows that has already been transported
    transported = []
    # list of lists, transport plan
    greedy_transport = []

    while len(transported) != len(cows):
        best_cow = ""
        temp = []
        while best_cow != None:
            # print(str(limit - total_weight(temp)))
            best_cow, best_weight = heaviest_cow(transported, cows, (limit - total_weight(temp)))

            if best_cow != None:
                temp.append(best_cow)
                transported.append(best_cow)
        greedy_transport.append(temp)

    return greedy_transport


# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)

    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    ## Power set containing alll possible variations
    variations = get_partitions(cows)

    valid_variations = []


    for i in variations:
        ship = []
        for j in i:
            ship_weights = []
            for k in j:
                ship_weights.append(cows[k])
            ship.append(sum(ship_weights))

        if all( d <= limit for d in ship):
            valid_variations.append(i)

    best = 10000
    best_ship = []
    for ship in valid_variations:
        if len(ship) < best:
            best = len(ship)
            best_ship = ship
    return ship


# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.

    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    pass


"""
Here is some test data for you to see the results of your algorithms with.
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

if __name__ == "__main__":
    cows = load_cows("ps1_cow_data.txt")
    limit=10
    print(cows)
    print(len(cows))
    print("--------------------------------------------------------------------------------------------------")
    print(greedy_cow_transport(cows, limit))
    print(str(len(greedy_cow_transport(cows, limit))) + " trips needed.")
    print()
    print()
    print(brute_force_cow_transport(cows, limit))
