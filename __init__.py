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
                  'say'  : {'yes': ('yes text',furry1),
                            'no' : ('no text', None),
                            },
                  }
furry1.init_txt = '''Very nice. We have confirmation of the coffee code sequence on our end. Good work, boss.
PPPThere aren't more than 5 foxes in the world capable of that feat. We almost know who you are.
PPPWe have one finaltask for you.

PPPWe think we\'ve found something on your manifold.
PPPSomething... PPPbig.
PPPThere\'s a fox monopole right under your tailless ass.
PPPSearch high in the room where old hopes go to die, inked in red.
There you\'ll find a small, fuzzy dual of the fox monopole in our realm.
Find it and enter the secret numbers the transdimensional lift has inscribed to its buttocks.'''

furry1.actions = {'look' : {'' : ('The fox computer nerd is waiting patiently. The audience looks on with awe. They\'re counting on you...PPP sexy.',None),
                           'computer' : ('It\'s an older computer, no match for a skilled hacker. Alas, you aren\'t even caught up on your basics.',None)
                           },
                  'say'  : {'fuck': ('Profanity will not be tolerated here. May you rot in that human-infested hell.','EXIT'),
                            'no'  : ('You can\'t refuse me and get away with it!\nPPP', 'EXIT'),
                            'yes' : ('Well, get on with it.', None),
                           },
                  'help' : {'': ('What more help do you want, flat-face? I gave you all the computers have.\nPPPThese transdimensional computations are only possible to solve in numerical riddles.',None)},
                  'enter_code' : {'12783', '''Very nice, that checks out...
                      PPP PPP
                      FOX KING!
                      PPP
                      Do you remember your true identity now?
                      PPP...PPPI told you to stay away from those conventions.
                      PPPWhat do you call yourselves, again? Skinnies?
                      PPPI don't judge what you do in your free time, but...PPPyour human analogues, the furries, at least know how to keep the right amount of fur showing! HAHAHA.
                      PPPGet back to work, your people need you.
                      ''','EXIT')},
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
        
