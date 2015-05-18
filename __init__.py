import time
import sys

class room():
    def __init__(self):
        self.actions = None
        self.init_txt = ''

# all rooms
metaworld0 = room(); metaworld1(); field = room(); fieldq = room(); persuasion= room(); task1 = room(); task2 = room()


# all commands, text

metaworld0.init_txt = 'Are you Maxwell Dare Porter, otherwise known as Barnacle Bill the Sailor?'
metaworld0.actions = {  'yes': ('',field),
                        'no' : ('',metaworld1)
                        }

metaworld1.init_txt = 'Do you like Strawberry Slushie Martinis with sugar on the rim?'
metaworld1.actions = {  'yes': ('',field),
                        'no' : ('I\'m wasting my time with you. Piss off.','EXIT')
                        }
field.init_txt = 'Great, it\'s you, we don\'t have much time. It seems to me your trans-manifold data buffer is pretty small\
 so I’ll provide audiovisual descriptions of your coordinates for the time being. Upload is a bitch so we’ll keep it to small\
  strings for your responses. Starting in 3 PPP 2 PPP 1 PPP\n\n\n You find yourself naked in a field, surrounded by foxes.'
  
field.actions = {'look' : {''     : ('There are lots of foxes.',None)},
                 'talk' : {''     : ('You babble to yourself. The foxes do not respond, but seem to grow more angry.',None),
                           'fox'  : ('You talk to the head fox.',fieldq),
                           'foxes': ('You talk to the head fox.',fieldq)
                          },
             }
fieldq.init_txt = 'The head fox climbs on top of three other foxes. At eye level he asks you: Naked man, can you help me?'
fieldq.actions = {'look' : {'' : ('The foxes await your answer intently, their eyes glow softly in the darkness.',None)},
                  'say'  : {'yes': ('',None),
                            'no' : ('', persuasion),
                            },
                  }
                  
persuasion.init_txt = 'The head fox scoffs at you. PPP He replies, with a coarse voice: Our king told us \
your kin has a set of pills that concentrate all desirable edibles. We could provide you with those if you \
so choose. Would this change your mind?'

persuasion.actions = {'yes': ('',task1)
                  'no' : ('The head fox laughs at you an turns toward his pack with this words: \n Brothers,\
                   he clearly isn\'t the chosen one. I say we eat him and wait for the next hairless biped! \n The\
                    foxes tore you to pieces...','EXIT')
                  }
task1.init_txt = 'The head fox proceeds: \n Ok, a bit of background. You live in the cotangent bundle of our manifold. \
For every point in our space there’s a vector field in yours. Our king used to study how to minimize \
our actions. And for that he had to go to your world. Our effort to track him down will involve you searching \
for a set of three imprints he must have left in his journeys. \n To our best knowledge, the first one is hidden \
 in the source of all knowledge. With you must retrieve the source of all suffering.  It should look like mountain peeks. \
  Inside search for the reason of the discreetness of a conserved quantity. Reference this.'
task1.actions ={'6.153': ('',task2)}

task2.init_txt =  'Great, this means he was in search of the fox monopole. Our monarch is the warmest and furriest of all foxes, \
In order to solve the Original Model Lagrangian he must have required some due preparations. Our experts tell us that his next \
direction would have been in the search of warmth and wakefulness. Hairless friend, search for this ones within your surroundings.'
task2.actions ={'': ('',)}



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
    print(this_room.init_txt)
    val = get_command(this_room)
    while val is None:
        val = get_command(this_room)
    if val == 'EXIT':
        sys.exit(0)
    this_room = val
        
