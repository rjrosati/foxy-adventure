import time
import sys

class room():
    def __init__(self):
        self.actions = None
        self.init_txt = ''

# all rooms
field = room(); fieldq = room(); forest = room()

furry1 = room()


# all commands, text
field.init_txt = 'You find yourself naked in a field, surrounded by foxes.'
field.actions = {'look' : {''     : ('There are lots of foxes.',None)},
                 'talk' : {''     : ('You babble to yourself. The foxes do not respond, but seem to grow more angry.',None),
                           'fox'  : ('You talk to the head fox.',fieldq),
                           'foxes': ('You talk to the head fox.',fieldq)
                          },
             }
fieldq.init_txt = 'The head fox climbs on top of three other foxes. At eye level he asks you: can you help me?'
fieldq.actions = {'look' : {'' : ('The foxes await your answer intently, their eyes glow softly in the darkness.',None)},
                  'say'  : {'yes': ('yes text',coffee),
                            'no' : ('no text', None),
                            },
                  }
furry1.init_txt = 'Very nice. We have confirmation of the coffee code sequence on our end. Good work, boss.\nPPPWe have another task for you.\nPPPWe think we\'ve found something on your manifold. \nPPPSomething... PPPbig.\nPPPThere\'s a fox monopole right under your hairless ass.\nSearch high in the room where old hopes go to die, inked in red. There you shall find a small, fuzzy dual of the fox monopole in our realm. Find it and enter the secret numbers the transdimensional lift has imparted to its buttocks.'
furry1.actions = {'look' : {'' : ('',None)},
                  'say'  : {'yes': ('yes text',coffee),
                            'no' : ('no text', None),
                           },
                  'help' : {'': ('What more help do you want, flat-face? I gave you all the computers have.\nPPPThese transdimensional computations are only possible to solve in riddles analytically.'
                  }


def print2(text,**kwargs):
    if 'PPP' in text:
        for textbit in text.split('PPP'):
            print(textbit,end="")
            time.sleep(1)
    else:
         print(text,**kwargs)

def get_command(room):
    print('> ',end="",flush=True)
    command = input()
    parts = command.lower().split()
    if len(parts) == 1:
        parts.append('')
    if parts[0] not in room.actions.keys():
        print('Unrecognized command: ',parts[0])
        print('Valid commands in this area are:',', '.join(room.actions.keys()))
        return get_command(room) 
    action = room.actions[parts[0]]
    try:
        print2(action[parts[1]][0])
        return action[parts[1]][1]
    except KeyError:
        print("You can't do that.")
        return get_command(room)

this_room = field
while True:
    print2(this_room.init_txt)
    val = get_command(this_room)
    while val is None:
        val = get_command(this_room)
    if val == 'EXIT':
        print2('Foxworld connection terminated.\nPPPGoodbye.')
        sys.exit(0)
    this_room = val
        
