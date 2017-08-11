example_input="John is connected to Bryant, Debra, Walter.\
John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.\
Bryant is connected to Olive, Ollie, Freda, Mercedes.\
Bryant likes to play City Comptroller: The Fiscal Dilemma, Super Mushroom Man.\
Mercedes is connected to Walter, Robin, Bryant.\
Mercedes likes to play The Legend of Corgi, Pirates in Java Island, Seahorse Adventures.\
Olive is connected to John, Ollie.\
Olive likes to play The Legend of Corgi, Starfleet Commander.\
Debra is connected to Walter, Levi, Jennie, Robin.\
Debra likes to play Seven Schemers, Pirates in Java Island, Dwarves and Swords.\
Walter is connected to John, Levi, Bryant.\
Walter likes to play Seahorse Adventures, Ninja Hamsters, Super Mushroom Man.\
Levi is connected to Ollie, John, Walter.\
Levi likes to play The Legend of Corgi, Seven Schemers, City Comptroller: The Fiscal Dilemma.\
Ollie is connected to Mercedes, Freda, Bryant.\
Ollie likes to play Call of Arms, Dwarves and Swords, The Movie: The Game.\
Jennie is connected to Levi, John, Freda, Robin.\
Jennie likes to play Super Mushroom Man, Dinosaur Diner, Call of Arms.\
Robin is connected to Ollie.\
Robin likes to play Call of Arms, Dwarves and Swords.\
Freda is connected to Olive, John, Debra.\
Freda likes to play Starfleet Commander, Ninja Hamsters, Seahorse Adventures."


def create_data_structure(string_input):
    network = {}
    while string_input:
        user = string_input[:string_input.find(' ')]

        conn_start = string_input.find("is connected to ") + 16
        conn_end = string_input.find(".")
        connections = string_input[conn_start:conn_end].split(", ")
        string_input = string_input[conn_end + 1:]

        games_start = string_input.find("likes to play ") + 14
        games_end = string_input.find(".")
        games = string_input[games_start:games_end ].split(', ')
        network[user] = [connections, games]
        string_input = string_input[games_end + 1:]

    return network


def get_connections(network, user):
    if user in network:
        return network[user][0]
    return None


def get_games_liked(network,user):
    if user in network:
        return network[user][1]
    return None


def add_connection(network, user_A, user_B):
    if user_A not in network or user_B not in network:
        return False
    if user_B not in network[user_A][0]:
        network[user_A][0].append(user_B)
    return network


def add_new_user(network, user, games):
    if user in network:
        return network
    network[user] = [[], games]
    return network


def get_secondary_connections(network, user):
    if user not in network:
        return None
    if not network[user][0]:
        return []
    cons_of_cons = []
    for u in network[user][0]:
        for u2 in network[u][0]:
            if u2 not in cons_of_cons:
                cons_of_cons.append(u2)
    return cons_of_cons


def count_common_connections(network, user_A, user_B):
    if user_A not in network or user_B not in  network:
        return False
    num = 0
    for con in network[user_A][0]:
        if con in network[user_B][0]:
            num += 1
    return num


def find_path_to_friend2(network, user_A, user_B):
    if user_B not in network or user_A not in network:
        return str(None) + ' '
    if user_B in network[user_A][0]:
        return user_A + ' ' + user_B + ' '
    for user in network[user_A][0]:
        check(user_A, checked)
        if check(user, checked):
            return user_A + ' ' + find_path_to_friend2(network, user, user_B)
    return str(None) + ' '

checked = []


def check(user, checked):
    if user in checked:
        checked = []
        return False
    checked.append(user)
    return True


def find_path_to_friend(network, user_A, user_B):
    p = find_path_to_friend2(network, user_A, user_B).split()
    if p == 'None ' or p[-1] == 'None':
        return None
    return p


def get_game_players(network, game):
    players = []
    for user in network:
        if game in network[user][1]:
            players.append(user)
    return players

