import os
import pdb


class room():
    def __init__(self):
        self.actions = None
        self.init_txt = ''

# all rooms
field = room(); fieldq = room(); forest = room()


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
                  'say'  : {'yes': ('yes text',None),
                            'no' : ('no text', None),
                            },
                  }


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
        print(action[parts[1]][0])
        return action[parts[1]][1]
    except KeyError:
        print("You can't do that.")
        return get_command(room)

this_room = field
while True:
    print(this_room.init_txt)
    val = get_command(this_room)
    while val is None:
        val = get_command(this_room)
    this_room = val
        
