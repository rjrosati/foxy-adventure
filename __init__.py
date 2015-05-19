#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import sys
import hashlib

class room():
    def __init__(self):
        self.actions = None
        self.init_txt = ''

# all rooms
metaworld0 = room(); metaworld1 = room(); field = room(); fieldq = room(); persuasion= room(); task1 = room(); task2 = room()

furry1 = room()


# all commands, text


with open('fox.txt','r') as f:
    foxascii = f.read()
with open('death.txt','r') as f:
    deathascii = f.read()
with open('foxking.txt','r') as f:
    foxkingascii = f.read()
with open('field.txt','r') as f:
    fieldascii = f.read()


metaworld0.init_txt = 'Are you Maxwell Dare Porter, otherwise known as Barnacle Bill the Sailor?'
metaworld0.actions = {'say':  {'yes': ('',field),
                               'no' : ('',metaworld1),
                               'fuck': ('Profanity will not be tolerated here. May you rot in that human-infested hell.','EXIT'),
                               },
                      'look': {'': ('You are in a black void. The only thing you can perceive is the booming voice which just posed the question.',None)}
                        }

metaworld1.init_txt = 'Do you like Strawberry Slushie Martinis with sugar on the rim?'
metaworld1.actions = {  'say': {'yes': ('',field),
                                'no' : ('I\'m wasting my time with you. Piss off.','EXIT'),
                                'fuck': ('Profanity will not be tolerated here. May you rot in that human-infested hell.','EXIT'),
                               },
                        'look': {'': ('You are in a black void. The only thing you can perceive is the booming voice which just posed the question.',None)}
                        }
field.init_txt = '''Great, it's you, we don't have much time.
PPPPPPIt seems to me your trans-manifold data buffer is pretty small.
PPPPPPI'll provide audiovisual descriptions of your coordinates for the time being.
PPPPPPUpload is a bitch so we'll keep it to small strings for your responses.

PPPPPPStarting inPPP 3...PPP 2...PPP 1...PPP
 
 '''+fieldascii+'''
 
 You find yourself naked in a field, surrounded by foxes.
 It's night, the moon is full.
 '''
  
field.actions = {'look' : {''     : ('There are lots of foxes, solid in a ring around you for at least 10 meters. You see trees in the moonlit distance.',None)},
                 'talk' : {''     : ('You babble to yourself. The foxes do not respond, but seem to grow more angry.',None),
                           'fox'  : ('A fox comes forward, apparently their leader. You talk to the head fox.',fieldq),
                           'foxes': ('A fox comes forward, apparently their leader. You talk to the head fox.',fieldq)
                          },
             }
fieldq.init_txt = '''The head fox climbs on top of two other foxes, reaching up towards your face.
PPP PPP
''' + foxascii + '''
PPPAt eye level he asks you:
"Our king has disappeared. Naked man, can you help me?"
'''
fieldq.actions = {'look' : {'' : ('The foxes await your answer intently, their eyes glow softly in the moonlight.',None)},
                  'say'  : {'yes': ('',task1),
                            'no' : ('', persuasion),
                            'fuck': ('Profanity will not be tolerated here. May you rot in that human-infested hell.','EXIT'),
                            },
                  }
                  
persuasion.init_txt = '''The head fox scoffs at you.
PPPHe replies, with a coarse voice: Our king told us your kin has a set of pills that concentrate all desirable edibles.PPP
PPPWe could provide you with those if you so choose. PPP

Would this change your mind?
'''

persuasion.actions = {'look' : {'' : ('The foxes await your answer intently, their eyes glow softly in the moonlight.',None)},
                      'say': {'yes': ('',task1),
                              'no' : ('The head fox laughs at you an turns toward his pack with this words: \nBrothers, he clearly isn\'t the chosen one. I say we eat him and wait for the next hairless biped! \nThe foxes tear you to pieces...','EXIT'),
                              'fuck': ('Profanity will not be tolerated here. May you rot in that human-infested hell.','EXIT'),
                              },
                     }
task1.init_txt = '''The head fox proceeds:
PPPOk, a bit of background. You live in the cotangent bundle of our manifold.PPP

For every point in our space there's a vector space in yours.PPP
Our king used to study how to minimize our actions.PPP
PPPAnd for that he had to go to your world. PPPOur effort to track him down will involve you searching for a set of three imprints he must have left in his journeys. PPP PPP

PPPTo our best knowledge, the first one is hidden in the source of all knowledge.PPP
PPPWithin, you must retrieve the source of all suffering.PPP
PPPIt should look like mountain peaks.PPP

PPPInside search for the reason of the discreetness of a conserved quantity.PPP
Reference its identifying number here.
'''
task1.actions = {'enter_code': {'c32992e3b2a8e986c4ea1b19378b0280d765f12b20053bf2351b86fc': ('',task2)},
                 'look' : {'':('The foxes buzz around in some sort of dance, yipping as they go.\nIt reminds you of the dance of sparks breaking through an air gap.', None)},
                 'help' : {'': ('I managed to get a bit more info out of the computer:\n"FUCK YOU NO HELP HERE YOU DON\'T GET OFF THAT EASY MOFO!"\nI wonder what it means?',None)},
                 'say'  : {'fuck': ('Profanity will not be tolerated here. May you rot in that human-infested hell.','EXIT'),
                           'no'  : ('You can\'t refuse me and get away with it!\nPPP', 'EXIT'),
                           'yes' : ('Well, get on with it.', None),
                          },
                 }

task2.init_txt =  '''Great, this means he was in search of the fox monopole.PPP
PPPOur monarch is the warmest and furriest of all foxes, PPPin order to solve the Original Model Lagrangian he must have required some due preparations.PPP
PPPOur experts tell us that his next direction would have been in the search of baby monsters.PPP
PPPHairless friend, search for this ones within your heart, and enter its order.
'''
task2.actions =  {'enter_baby_order' :{'69baadf19ba802db53bc21a019a27d37ff92cc00ffe0a411f38c7fba':('',furry1)},
                  'look'  : {'': ('You notice baby foxes cuddling. Your hearth melts. You die.','EXIT')},
                  'help'  : {'': ('What more help do you want, flat-face? I gave you all the computers have.\nPPPThese transdimensional computations are only possible to solve in numerical riddles.\n',None)},
                  'say'   : {'fuck': ('Profanity will not be tolerated here. May you rot in that human-infested hell.','EXIT'),
                             'no'  : ('You can\'t refuse me and get away with it!\nPPP', 'EXIT'),
                             'yes' : ('Well, get on with it.', None),
                           },
                  }
furry1.init_txt = '''Very nice. We have confirmation of the baby monster sequence on our end.PPP
Good work, boss.

PPPThere aren't more than 5 foxes in the world capable of that feat.
PPPWe have one final task for you.

PPPWe think we've found something on your manifold.
PPPSomething... PPPbig.
PPPThere's a fox monopole right under your tailless ass.
PPPSearch high in the room where old hopes go to die, inked in red. PPP
PPPThere you'll find a small, fuzzy dual of the fox monopole in our realm.
PPPFind it and enter the secret numbers the trans-dimensional lift has inscribed to its buttocks.
'''

furry1.actions = {'look' : {'' : ('The fox computer nerd is waiting patiently. The audience looks on with awe. They\'re counting on you...PPP sexy.',None),
                           'computer' : ('It\'s an older computer, no match for a skilled hacker. Alas, you aren\'t even caught up on your basics.',None)
                           },
                  'say'  : {'fuck': ('Profanity will not be tolerated here. May you rot in that human-infested hell.','EXIT'),
                            'no'  : ('You can\'t refuse me and get away with it!\nPPP', 'EXIT'),
                            'yes' : ('Well, get on with it.', None),
                           },
                  'help' : {'': ('What more help do you want, flat-face? I gave you all the computers have.\nPPPThese transdimensional computations are only possible to solve in numerical riddles.\n',None)},
                  'enter_code' : {'36b5a957a8a80218c2095954bfd7c09e29f18978f6d45c62a0a9635a': ('''Very nice, that checks out...
PPP PPP
FOX KING!

'''
+ foxkingascii +
'''
PPP
Do you remember your true identity now?
PPP...PPPI told you to stay away from those conventions.
PPPWhat do you call yourselves, again? Skinnies?
PPPI don't judge what you do in your free time, but...
PPPyour human analogues, the furries...
PPPthey at least know how to keep the right amount of fur showing!PPP
PPP
HAHAHA!

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
    if parts[0].startswith('enter_'):
        parts[1] = hashlib.sha224(parts[1].encode('utf-8')).hexdigest()
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
        
