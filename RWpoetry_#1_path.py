# a path generator 

import random
import textwrap
import codecs 

# diana = codecs.open('diana.txt', encoding='utf-8')
# kristen = codecs.open('kristen.txt', encoding='utf-8')
# wendi = codecs.open('wendi.txt', encoding='utf-8')

# with diana as dianaFile:
#     with kristen as kristenFile:
#             with wendi as wendiFile:
#                 routeLine = dianaFile.read().split('\n') + kristenFile.read().split('\n') + wendiFile.read().split('\n')


direction = ['over there', 'there', 'further', 'left', 'right', 'backwards', 'up', 'back', 'down', 'clockwise', 'upstairs','through']
site = ['main street', 'stone-paved road', 'marble wall', 'slope', 'big garden', 'station', 'forest', 'city', 'lake', 'starting point', 'park', 'museum', 'turnstile', 'tunnel', 'staircase','hills']
time = ['now', 'for a moment', 'every ten minutes', 'an hour later', 'a couple of years later', 'sometimes', 'one second','two seconds','three seconds']
verb = ['wait', 'see', 'look', 'stop', 'turn', 'go', 'follow', 'remember', 'close', 'pass', 'cover','walk', 'sit','watch']
adj = ['visible', 'dark', 'luxuriant', 'outbound', 'blue', 'green', 'grey', 'red', 'silver', 'tall', 'short','narrowing','swelling', 'embarrassed', 'damped-out','crowded']
obj = ['rain', 'smell of alcohol and grease', 'path', 'steps', 'leaves', 'sunlight', 'color', 'window', 'glow', 'weeds', 'ticket','bench']


emotion = ['lovely','intense pain','going to pass out','difficult','terrible']
dialogue = ['what happened?','can you see it?','oh','what does it want?','no.','can you still see it?','Do you remember what it was?','everything is gone.',"it's ok.",'would it be ok?']
 # dialogues are full sentences
subject = ['you','we','I','let us']

def subaction():
    words = random.choice(subject)
    words += " " + random.choice(verb) + " " + random.choice(direction) + "."
    return words.capitalize()

def feeling():
    words = random.choice(emotion)
    words += "."
    return words.capitalize()

def dial():
    words = random.choice(dialogue)
    return words.capitalize()

def justaction():
    words = random.choice(verb)
    words += " " + random.choice(direction) + "."
    return words.capitalize()


def timespan():
    move = random.choice(verb)
    move += ","+" " + random.choice(time) + " -"
    return move.capitalize()


def space():
    words = random.choice(site)
    adjs = random.choice(adj) 
    adjs += " " + random.choice(obj)

    words += " - " + adjs + "."
    return words.capitalize()

stanza_count = 10
for repeat in range(stanza_count):
    line_count = random.randrange(2, 6)
    for i in range(line_count):
        if i == 0:
            print(justaction())
        elif i == line_count - 3:
            print(feeling())
        elif i == line_count - 2:
            print(subaction())
        elif i == line_count - 1:
            print(' ')
            print(space())
            print(' ')
        else:
            print(timespan())
            print(dial())


