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

def roadtrip():
    starting = []
    start = input('Enter starting city:\nBoston | New York | Albany | Portland | Philadelphia\n= ')
    hop1 = (city_to_accessible_cities[start])
    print('Cities reached in 1 Hop:', hop1)

    hop2 = 0

    # hop2 = (city_to_accessible_cities[hop1]) Doesn't work
    # achieve, use the dictionary of the start to access those and print those cities
    # dictionaries.
    print('From', start, 'through', hop2, 'you can reach')

roadtrip()