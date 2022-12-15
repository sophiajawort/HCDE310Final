import random
import logging
class Move:
    # init takes a desired length of a combo and current set of moves dictionary
    def __init__(self, move_data):
        
        self.name = move_data['Name']
        self.baseDamage = move_data['BaseDamage']
        self.type = move_data['MoveType']

        if 'Jab' in self.name:
            self.src = 'https://live.staticflickr.com/65535/52564108792_74e800e1c9_q.jpg'
        elif 'dash' in self.name:
            self.src = 'https://live.staticflickr.com/65535/52565099088_588e878eed_m.jpg'
        elif 'Utilt' in self.name:
            self.src = 'https://live.staticflickr.com/65535/52565053125_2ea6e29d81_q.jpg'
        elif 'Dtilt' in self.name:
            self.src = 'https://live.staticflickr.com/65535/52565130098_51b157fbd9_q.jpg'
        elif 'Ftilt' in self.name:
            self.src = 'https://live.staticflickr.com/65535/52564599901_eb03d55df2_q.jpg'
        elif 'throw' in self.name:
            self.src = 'https://live.staticflickr.com/65535/52564980694_a9666868cf.jpg'
        elif self.type =='special':
            self.src = 'https://live.staticflickr.com/65535/52565150348_4fd61efc17_m.jpg'
        elif 'Usmash' in self.name:
            self.src = 'https://live.staticflickr.com/65535/52565053125_2ea6e29d81_q.jpg'
        elif 'Dsmash' in self.name:
            self.src = 'https://live.staticflickr.com/65535/52565130098_51b157fbd9_q.jpg'
        elif 'Fsmash' in self.name:
            self.src = 'https://live.staticflickr.com/65535/52564599901_eb03d55df2_q.jpg'
        elif 'Nair' in self.name:
            self.src = 'https://live.staticflickr.com/65535/52564331327_3325648d74_q.jpg'
        elif 'Dair' in self.name:
            self.src = 'https://live.staticflickr.com/65535/52564331367_21fbe49200_m.jpg'
        elif 'Fair' in self.name:
            self.src = 'https://live.staticflickr.com/65535/52564331342_aa64bc02e1_m.jpg'
        elif 'Bair' in self.name:
            self.src = 'https://live.staticflickr.com/65535/52564331342_aa64bc02e1_m.jpg'
        else:
            self.src = 'https://live.staticflickr.com/65535/52564904929_c3acf48fcc_m.jpg'


    def __str__(self):
        string = "%s: Base Damage - %s, Move Type - %s\n "%(self.name, self.baseDamage, self.type)
        return string
    
class Combo:
    def __init__(self, possible_moves, combo_length = random.choice([3, 4])):
        self.length = combo_length
        print('SELF LENGTH', self.length)
        #for i in range(self.length):
        keys = possible_moves.keys()
        for key in keys:
            key = key
        move_type_option = ['ground', 'throw', 'aerial']
        move_type = random.choice(move_type_option)
        # current options for first move of the combo 
        # ground or throw type
        # list of move objects
        curr_moves = possible_moves[key][move_type]
        self.move1 = random.choice(curr_moves)
        if self.length == 2:
            move_type = 'special'
            curr_moves = possible_moves[key][move_type]
            self.move2 = random.choice(curr_moves)
        else:
            move_type = 'ground'
            curr_moves = possible_moves[key][move_type]
            self.move2 = random.choice(curr_moves)
            move_type = 'special'
            curr_moves = possible_moves[key][move_type]
            self.move3 = random.choice(curr_moves)
        
    def __str__(self):
        if self.length ==2:
            string = "Move 1: %s \n"%(self.move1)
            string += 'Move 2: %s'%(self.move2)
        else:
            string = 'Move 1: %s \nMove 2: %s \nMove 3: %s'%(self.move1, self.move2, self.move3)
        return string

    def main():
        print('hello world')
    
