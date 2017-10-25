'''

We road trippin' through space and time!

'''



city_to_accessible_cities = {
    'Boston': {'New York', 'Albany', 'Portland'},
    'New York': {'Boston', 'Albany', 'Philadelphia'},
    'Albany': {'Boston', 'New York', 'Portland'},
    'Portland': {'Boston', 'Albany'},
    'Philadelphia': {'New York'}
}

## Travling from one city to an adjacent one is called a hop.
## Let the user input a city out of the list
## Print out all of the cities connected to that via a hop
## Then print out all of the cities that can be reached through two hops

def hop(city):
    return city_to_accessible_cities[city]
    #return a list of all the cities in 1 hop

def hop2(city):
    one_hop = hop(city)
    two_hops = set() # set is like a list but you can only have unique elements
    for one_hop_city in one_hop:
        two_hop_cities = hop(one_hop_city)
        two_hops |= two_hop_cities
    return two_hops


def roadtrip():
    starting = []
    start = input('Enter starting city:\nBoston | New York | Albany | Portland | Philadelphia\n= ')
    hop1 = hop(start)
    print('Cities reached in 1 Hop:', hop1)
    hop_two = hop2(start)
    # hop2 = (city_to_accessible_cities[hop1]) Doesn't work
    # achieve, use the dictionary of the start to access those and print those cities
    # dictionaries.
    print('From', start, 'through', hop_two, 'you can reach')

roadtrip()