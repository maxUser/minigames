import json
import sqlite3
from Player import Player

def determine_players():
    # essentially, logging in
    # search for each player in database
    # if player is found, add to arena
    # else ask if new player should be created
    print('determine_players')

    # p1 = input('Name of player: ')
    p1 = 'player1'
    p1 = find_player(p1)
    p1 = Player(p1[0])
    p1.printPlayer()

    # p2 = input('Name of player: ')
    p2 = 'player2'
    p2 = find_player(p2)
    p2 = Player(p2[0])
    p2.printPlayer()

    return (p1, p2)

def find_player(name):
    # search for existing player in database
    # if none found, retry with another name or create new player
    conn = sqlite3.connect('noname.db')
    cursor = conn.cursor()
    t = (name, ) # recommended by https://docs.python.org/3.7/library/sqlite3.html
    player_row = cursor.execute("SELECT * FROM Players WHERE Name=?", t).fetchall()
    if len(player_row) == 1:
        conn.close()
        return player_row[0]
    else:
        # eventually ask to create new player here
        conn.close()
        print('Could not find player: {}'.format(name))
        name = input('Try another name: ')
        find_player(name)

def determine_companion(player):
    # giving players a preset companion
    print('determine_companion')

    conn = sqlite3.connect('noname.db')
    cursor = conn.cursor()
    if player.name == 'player1':
        t = ('Bulbasaur', )
        bulba = cursor.execute("SELECT * FROM Companions WHERE Name=?", t).fetchone()
        json_bulba = json.dumps(bulba)
        # json_bulba = tuple(json_bulba)
        # json_bulba = [c.replace('[', '(') for c in json_bulba]
        # json_bulba = [c.replace(']', ')') for c in json_bulba]
        print(type(json_bulba))
        # print(json_bulba)
        for c in json_bulba:
            print(c)
        exec_string = "UPDATE Players SET Companions = %s WHERE Name = \'%s\'" % (json_bulba, player.name)
        # print(exec_string)
        cursor.execute(exec_string)
        cursor.commit()
    elif player.name == 'player2':
        t = ('Charmander', )
        charm = cursor.execute("SELECT * FROM Companions WHERE Name=?", t).fetchone()

    conn.close()




def combat():
    # each player chooses their companion
    # companions take turns fighting
    print('combat')

    players = determine_players()
    determine_companion(players[0])
