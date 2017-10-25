'''

Lab 28 - All My Socks - These Are The Socks Of Our Lives

'''

import random

# random socks from :
# sock_types = ['ankle', 'crew', 'dress', 'hiking']

def random_socks():
    sock_types = ['ankle', 'crew', 'dress', 'hiking']
    sock_colors = ['black', 'pattern', 'gray']
    my_socks = []
    pairs = {}
    singles = {}
    for i in range(100):
        randsock = random.choice(sock_types)
        randcolor = random.choice(sock_colors)
        my_socks.append((randcolor, randsock))
    # print(my_socks)
    while len(my_socks) > 0:
        sock = my_socks.pop(0)
        if sock in my_socks:
            my_socks.remove(sock)
            if sock in pairs:
                pairs[sock] += 1
            else:
                pairs[sock] = 1
        else:
            if sock in singles:
                singles[sock] +=1
            else:
                singles[sock] = 1


    # crew_count = 0
    # ankle_count = 0
    # dress_count = 0
    # hiking_count = 0
        # if randsock == 'ankle':
        #     #my_socks.append(randsock)
        #     ankle_count +=1
        # if randsock == 'crew':
        #     #my_socks.append(randsock)
        #     crew_count +=1
        # if randsock == 'dress':
        #     #my_socks.append(randsock)
        #     dress_count +=1
        # if randsock == 'hiking':
        #     #my_socks.append(randsock)
        #     hiking_count +=1
    # for i in range(len(crew_count)-1):
    #     pass
    # return list(sorted(my_socks))


    # for sock in singles:
    #     print('The single and lonely socks are: ')
    #     print(sock)

    print(singles)

    # for sock in pairs:
    #     print(sock)

    print(pairs)


random_socks()



