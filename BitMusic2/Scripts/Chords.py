
#######################
# Chords.py           #
# Author: GGN_2015    #
# Date  : 2022-07-20  #
#######################


import Methods
#!#################################!#
#! ALL PATTERNS ARE NOTE_LIST_SET  !#
#!#################################!#


####################################
# Pattern001_Major(C)              #
# 8 Beats, slow, 4/4               #
####################################
Pattern001_Major_C3 = [
    [
        Methods.createNote("C3", 1),
        Methods.createNote("G3", 1),
        Methods.createNote("C4", 1),
        Methods.createNote("D4", 1),
        Methods.createNote("E4", 1),
        Methods.createNote("D4", 1),
        Methods.createNote("C4", 1),
        Methods.createNote("G3", 1)
    ]
]
def Pattern001_Major(baseNoteName:str, length = 1.0, repeat = 1):
    tmp = Methods.tuneNoteListSet(Pattern001_Major_C3, Methods.distance(baseNoteName, "C3"))
    tmp = Methods.changeSpeed(tmp, length)
    if repeat > 1:
        tmp = Methods.LinkNoteListSetArray([tmp] * repeat)
    return tmp


####################################
# Pattern001_Minor(C)              #
# 8 Beats, slow, 4/4               #
####################################
Pattern001_Minor_C3 = [
    [
        Methods.createNote("C3" , 1),
        Methods.createNote("G3" , 1),
        Methods.createNote("C4" , 1),
        Methods.createNote("D4" , 1),
        Methods.createNote("D#4", 1),
        Methods.createNote("D4" , 1),
        Methods.createNote("C4" , 1),
        Methods.createNote("G3" , 1)
    ]
]
def Pattern001_Minor(baseNoteName:str, length = 1.0, repeat = 1):
    tmp = Methods.tuneNoteListSet(Pattern001_Minor_C3, Methods.distance(baseNoteName, "C3"))
    tmp = Methods.changeSpeed(tmp, length)
    if repeat > 1:
        tmp = Methods.LinkNoteListSetArray([tmp] * repeat)
    return tmp


####################################
# Pattern002                       #
# 4 Beats, slow, 4/4               #
####################################
Pattern002_C3 = [
    [
        Methods.createNote("C3" , 1),
        Methods.createNote("G3" , 1),
        Methods.createNote("C4" , 2)
    ]
]
def Pattern002(baseNoteName:str, length = 1.0, repeat = 1):
    tmp = Methods.tuneNoteListSet(Pattern002_C3, Methods.distance(baseNoteName, "C3"))
    tmp = Methods.changeSpeed(tmp, length)
    if repeat > 1:
        tmp = Methods.LinkNoteListSetArray([tmp] * repeat)
    return tmp


####################################
# Pattern003                       #
# 4 Beats, fast, 4/4               #
####################################
Pattern003_C3 = [
    [
        Methods.createNote("C3" , 0.5),
        Methods.createNote("G3" , 0.5),
        Methods.createNote("C4" , 0.5),
        Methods.createNote("G3" , 0.5),
        Methods.createNote("C4" , 0.5),
        Methods.createNote("G3" , 0.5),
        Methods.createNote("C4" , 0.5),
        Methods.createNote("G3" , 0.5),
    ]
]
def Pattern003(baseNoteName:str, length = 1.0, repeat = 1):
    tmp = Methods.tuneNoteListSet(Pattern003_C3, Methods.distance(baseNoteName, "C3"))
    tmp = Methods.changeSpeed(tmp, length)
    if repeat > 1:
        tmp = Methods.LinkNoteListSetArray([tmp] * repeat)
    return tmp


####################################
# Pattern004_Major                 #
# 4 Beats, slow, 4/4               #
####################################
Pattern004_Major_C3 = [
    [
        Methods.createNote("C3" , 1),
        Methods.createNote("G3" , 1),
        Methods.createNote("C4" , 1),
        Methods.createNote("E4" , 1)
    ]
]
def Pattern004_Major(baseNoteName:str, length = 1.0, repeat = 1):
    tmp = Methods.tuneNoteListSet(Pattern004_Major_C3, Methods.distance(baseNoteName, "C3"))
    tmp = Methods.changeSpeed(tmp, length)
    if repeat > 1:
        tmp = Methods.LinkNoteListSetArray([tmp] * repeat)
    return tmp


####################################
# Pattern004_Minor                 #
# 4 Beats, slow, 4/4               #
####################################
Pattern004_Minor_C3 = [
    [
        Methods.createNote("C3" , 1),
        Methods.createNote("G3" , 1),
        Methods.createNote("C4" , 1),
        Methods.createNote("D#4" , 1)
    ]
]
def Pattern004_Minor(baseNoteName:str, length = 1.0, repeat = 1):
    tmp = Methods.tuneNoteListSet(Pattern004_Minor_C3, Methods.distance(baseNoteName, "C3"))
    tmp = Methods.changeSpeed(tmp, length)
    if repeat > 1:
        tmp = Methods.LinkNoteListSetArray([tmp] * repeat)
    return tmp


####################################
# Pattern005_Major                 #
# 8 Beats, slow, 4/4               #
####################################
Pattern005_Major_C3 = [
    [
        Methods.createNote("G2" , 1),
        Methods.createNote("C3" , 1),
        Methods.createNote("E3" , 1),
        Methods.createNote("C3" , 1),
        Methods.createNote("G3" , 1),
        Methods.createNote("C3" , 1),
        Methods.createNote("E3" , 1),
        Methods.createNote("C3" , 1)
    ]
]
def Pattern005_Major(baseNoteName:str, length = 1.0, repeat = 1):
    tmp = Methods.tuneNoteListSet(Pattern005_Major_C3, Methods.distance(baseNoteName, "C3"))
    tmp = Methods.changeSpeed(tmp, length)
    if repeat > 1:
        tmp = Methods.LinkNoteListSetArray([tmp] * repeat)
    return tmp


####################################
# Pattern005_Minor                 #
# 8 Beats, slow, 4/4               #
####################################
Pattern005_Minor_C3 = [
    [
        Methods.createNote("G2"  , 1),
        Methods.createNote("C3"  , 1),
        Methods.createNote("D#3" , 1),
        Methods.createNote("C3"  , 1),
        Methods.createNote("G3"  , 1),
        Methods.createNote("C3"  , 1),
        Methods.createNote("D#3" , 1),
        Methods.createNote("C3"  , 1)
    ]
]
def Pattern005_Minor(baseNoteName:str, length = 1.0, repeat = 1):
    tmp = Methods.tuneNoteListSet(Pattern005_Minor_C3, Methods.distance(baseNoteName, "C3"))
    tmp = Methods.changeSpeed(tmp, length)
    if repeat > 1:
        tmp = Methods.LinkNoteListSetArray([tmp] * repeat)
    return tmp


####################################
# Pattern006                       #
# 3 Beats, slow, 3/4               #
####################################
Pattern006_C3 = [
    [
        Methods.createNote("C3" , 1),
        Methods.createNote("G3" , 1),
        Methods.createNote("G3" , 1)
    ],
    [
        Methods.createNote("NULL" , 1),
        Methods.createNote("C4" , 1),
        Methods.createNote("C4" , 1)
    ]
]
def Pattern006(baseNoteName:str, length = 1.0, repeat = 1):
    tmp = Methods.tuneNoteListSet(Pattern006_C3, Methods.distance(baseNoteName, "C3"))
    tmp = Methods.changeSpeed(tmp, length)
    if repeat > 1:
        tmp = Methods.LinkNoteListSetArray([tmp] * repeat)
    return tmp
def Pattern006_dim(baseNoteName:str, length = 1.0, repeat = 1):
    tmp = Pattern006(baseNoteName, length, repeat)
    tmp[0][1] = Methods.tuneNote(tmp[0][1], -1)
    tmp[0][2] = Methods.tuneNote(tmp[0][2], -1)
    return tmp

####################################
# Pattern007                       #
# 4 Beats, slow, 4/4               #
####################################
Pattern007_C3 = [
    [
        Methods.createNote("C3" , 1),
        Methods.createNote("G3" , 1),
        Methods.createNote("C4" , 1),
        Methods.createNote("G3" , 1)
    ]
]
def Pattern007(baseNoteName:str, length = 1.0, repeat = 1):
    tmp = Methods.tuneNoteListSet(Pattern007_C3, Methods.distance(baseNoteName, "C3"))
    tmp = Methods.changeSpeed(tmp, length)
    if repeat > 1:
        tmp = Methods.LinkNoteListSetArray([tmp] * repeat)
    return tmp
