import time
import sys

class room():
    def __init__(self):
        self.actions = None
        self.init_txt = ''

# all rooms
metaworld0 = room(); metaworld1 = room(); field = room(); fieldq = room(); persuasion= room(); task1 = room(); task2 = room()

furry1 = room()


# all commands, text


with open('fox.txt','r') as f1:
    foxascii = f1.read()
with open('death.txt','r') as f2:
    deathascii = f2.read()
with open('foxking.txt','r') as f3:
    foxkingascii = f3.read()



metaworld0.init_txt = 'Are you Maxwell Dare Porter, otherwise known as Barnacle Bill the Sailor?'
metaworld0.actions = {'say':  {'yes': ('',field),
                               'no' : ('',metaworld1),
                               },
                      'look': {'': ('You are in a black void. The only thing you can perceive is the booming voice which just posed the question.',None)}
                        }

metaworld1.init_txt = 'Do you like Strawberry Slushie Martinis with sugar on the rim?'
metaworld1.actions = {  'say': {'yes': ('',field),
                                'no' : ('I\'m wasting my time with you. Piss off.','EXIT'),
                               },
                        'look': {'': ('You are in a black void. The only thing you can perceive is the booming voice which just posed the question.',None)}
                        }
field.init_txt = 'Great, it\'s you, we don\'t have much time.\nPPPPPPIt seems to me your trans-manifold data buffer is pretty small.\nPPP\
PPPI’ll provide audiovisual descriptions of your coordinates for the time being.\nPPPPPPUpload is a bitch so we’ll keep it to small\
 strings for your responses.\n\nPPPPPPStarting inPPP 3...PPP 2...PPP 1...PPP\n\n\nYou find yourself naked in a field, surrounded by foxes.\nIt\'s night, the moon is full.\n'
  
field.actions = {'look' : {''     : ('There are lots of foxes, solid in a ring around you for at least 10 meters. You see trees in the moonlit distance.',None)},
                 'talk' : {''     : ('You babble to yourself. The foxes do not respond, but seem to grow more angry.',None),
                           'fox'  : ('A fox comes forward, apparently their leader. You talk to the head fox.',fieldq),
                           'foxes': ('A fox comes forward, apparently their leader. You talk to the head fox.',fieldq)
                          },
             }
fieldq.init_txt = 'The head fox climbs on top of two other foxes, reaching up towards your face.PPP PPP\n' + foxascii + '\nPPPAt eye level he asks you: Naked man, can you help me?\n'
fieldq.actions = {'look' : {'' : ('The foxes await your answer intently, their eyes glow softly in the moonlight.',None)},
                  'say'  : {'yes': ('',task1),
                            'no' : ('', persuasion),
                            },
                  }
                  
persuasion.init_txt = 'The head fox scoffs at you.\nPPPHe replies, with a coarse voice: Our king told us \
your kin has a set of pills that concentrate all desirable edibles.\nWe could provide you with those if you \
so choose. Would this change your mind?\n'

persuasion.actions = {'look' : {'' : ('The foxes await your answer intently, their eyes glow softly in the moonlight.',None)},
                      'say': {'yes': ('',task1),
                              'no' : ('The head fox laughs at you an turns toward his pack with this words: \n Brothers,\
                   he clearly isn\'t the chosen one. I say we eat him and wait for the next hairless biped! \n The\
                    foxes tore you to pieces...','EXIT'),
                              },
                     }
task1.init_txt = 'The head fox proceeds: \n Ok, a bit of background. You live in the cotangent bundle of our manifold. \
For every point in our space there’s a vector field in yours. Our king used to study how to minimize \
our actions. And for that he had to go to your world. Our effort to track him down will involve you searching \
for a set of three imprints he must have left in his journeys. \n To our best knowledge, the first one is hidden \
 in the source of all knowledge. With you must retrieve the source of all suffering.  It should look like mountain peeks. \
  Inside search for the reason of the discreetness of a conserved quantity. Reference this.'
task1.actions = {'enter_code': {'6.153': ('',task2)},
                 'look' : {'':('The foxes buzz around in some sort of dance, yipping as they go.\nIt reminds you of the dance of sparks breaking through an air gap.', None)}
                 }

task2.init_txt =  'Great, this means he was in search of the fox monopole. Our monarch is the warmest and furriest of all foxes, \
In order to solve the Original Model Lagrangian he must have required some due preparations. Our experts tell us that his next \
direction would have been in the search of warmth and wakefulness. Hairless friend, search for this ones within your surroundings.'
task2.actions =  {'enter_baby_order' :{'4154781481226426191177580544000000':('',furry1)},
                  'look'  : {'': ('You notice baby foxes cuddling. Your hearth melts. You die.','EXIT')
                            }
                  }
furry1.init_txt = '''Very nice. We have confirmation of the baby monster sequence on our end. Good work, boss.
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
                  'enter_code' : {'12783': ('''Very nice, that checks out...
PPP PPP
FOX KING!'''
+ foxkingascii +
'''PPP
Do you remember your true identity now?
PPP...PPPI told you to stay away from those conventions.
PPPWhat do you call yourselves, again? Skinnies?
PPPI don't judge what you do in your free time, but...PPPyour human analogues, the furries, at least know how to keep the right amount of fur showing! HAHAHA.
PPPGet back to work, your foxes need you.
                      ''','FINAL')},
                  }


def print2(text,**kwargs):
    if 'PPP' in text:
        for textbit in text.split('PPP'):
            print(textbit,end="",flush=True)
            time.sleep(1)
    else:
         print(text,**kwargs)

def get_command(room):
    print('> ',end="",flush=True)
    command = input()
    if command == '':
        return get_command(room)
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

this_room = metaworld0
while True:
    print2(this_room.init_txt)
    val = get_command(this_room)
    while val is None:
        val = get_command(this_room)
    if val == 'EXIT':
        print2(deathascii+'Foxworld connection terminated.\nPPPGoodbye.\n')
        sys.exit(0)
    if val == 'FINAL':
        print2('Foxworld connection terminated.\nPPPGoodbye.\n')
        sys.exit(0)
    this_room = val
        
