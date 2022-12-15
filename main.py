
import urllib.parse, urllib.request, urllib.error, json
import logging
import buildingblocks as buildingblocks
from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def main_handler():
    app.logger.info("In MainHandler")
    return render_template('homepage.html',page_title="Smash Bros Coach")

def move_name(x):
    return x['Name']

def filter(string):
    substrings = ['(Late)', '(Early', 'Angle','Charge','Dash', 'Grab', 'Roll', 'dodge']
    for filter in substrings:
        if filter in string:
            return False
    return True

def safe_get_character_moves(name='Kirby'):
    character_game_moves = 'https://api.kuroganehammer.com/api/characters/name/' + name +'/moves?expand=false'
    try:
        move_page = urllib.request.urlopen(character_game_moves)
        move_page = move_page.read()
        move_page = json.loads(move_page)
        return move_page
    except urllib.error.HTTPError as e:
        return('<!DOCTYPE html><html><p>Error trying to retrieve data<p></html>')
    except urllib.error.URLError as e:
        return('<!DOCTYPE html><html><p>We failed to reach a server:p></html>')

@app.route("/gresponse")
def character_response_handler():
    character = request.args.get('character')
    app.logger.info(character)
    if character:
        char_data = safe_get_character_moves(character)
        list_of_moves = []
        for move in char_data:
            move_object = buildingblocks.Move(move)
            check = filter(move_object.name)
            if check == True:
                list_of_moves.append(move_object)
        # I want to make dictionary for char and movetypes
        move_dict = {}
        move_dict[character] = {}
        # sorting the moves by movetype into a move_dict
        for move in list_of_moves:
            curr_key = move.type

            if curr_key in move_dict[character]:
                curr_moves = move_dict[character][curr_key]
                curr_moves = curr_moves.append(move)
            else:
                move_dict[character][curr_key] = [move]
        
        list_of_combos = []
        for i in range(0,10):
            combo_object = buildingblocks.Combo(move_dict)
            length = combo_object.length
            print(length)
            list_of_combos.append(combo_object)
        
        # now have moves sorted, generate combos
        return render_template('responsePage.html',character=character, page_title='Combos for %s'%(character), 
                                combos = list_of_combos, char_data=char_data)

# parameter: move data from safe_get_character
# prints out the move name and move type for each move of the
# specified character
def print_moves(move_page):
    moves = {}
    for move in move_page:
        # want the name of move and the move type 
        move_name = move['Name']
        move_type = move['MoveType']
        moves[move_name] = move_type

    for move in moves:
        print(move,":", moves[move])

# Parameters: list of character names
# prints out the move list for each specified character
# in the list
def my_mains_moves(main_list):
    mains = main_list
    for main in mains:
        print('Moves for %s:'%(main))
        character_moves = safe_get_character_moves(main)
        print_moves(character_moves)
        print('FINISHED THE MOVE LIST FOR THIS CHARACTER\n')

if __name__ == "__main__":
# Used when running locally only. 
# When deploying to Google AppEngine, a webserver process will
# serve your app. 
    app.run(host="localhost", port=8080, debug=True)
    safe_get_character_moves('Kirby')