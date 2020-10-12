#Madlibs Generator
import random
import copy
#Madlibs story
madlibs=(
    "Hello my name is astronaut {}.I am on my way "+
    "to {}.I will be going for {} "+
    "days.I am very {} about the trip but I will miss my "+
    "{}.I have heard that the atmosphere there is "+
    "{}.Luckily my {} packed me a jacket to "+
    "keep me {} When I land on the planet I will "+
    "{} for joy.I am {} to walk on "+
    "another planet.I could notbe more {} for the trip!!!"
)
#Dictionary that consists of words that can be added within the madlibs story
global_dict={
    'Name':['Mayuri','Nehal','Samarth','Mandar','Gauri','Bhakti'],
    'Planet':['Mercury','Venus','Mars','Jupiter','Saturn','Uranus','Neptune','Milky Way'],
    'Days':['10','11','12','13','14','15'],
    'Adjective':['excited','nervous','afraid','confused','dry','cold','weird','rainy','snowy','warm','happy','safe','harsh'],
    'Noun':['room','friend','pet','home-town','bookshelf','video-game'],
    'Relative':['Uncle','Sister','Brother','Aunty','Cousin','Bestfriend','Colleague'],
    'Verb':['go','run','adapt','shout','wave','laugh']
}
#Selects a random word from global dictionary
def add_word(type,local_dict):
    words = local_dict[type]
    count = len(words)-1
    index = random.randint(0,count)
    return local_dict[type].pop(index)
#Creating a local dictionary of words that are once used in story and not affecting the global dictionary
def madlibs_generator():
    local_dict = copy.deepcopy(global_dict)
    return madlibs.format(
        add_word('Name',local_dict),
        add_word('Planet',local_dict),
        add_word('Days',local_dict),
        add_word('Adjective',local_dict),
        add_word('Noun',local_dict),
        add_word('Adjective',local_dict),
        add_word('Relative',local_dict),
        add_word('Adjective',local_dict),
        add_word('Verb',local_dict),
        add_word('Adjective',local_dict),
        add_word('Adjective',local_dict)
        )
print('Hey! the story is ready...')
print(madlibs_generator())
