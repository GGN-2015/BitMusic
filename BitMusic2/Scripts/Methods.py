import os
import DirUtils

########################
# Methods.py           #
# Author: GGN_2015     #
# Date  : 2022-07-20   #
########################


#############################################################
# THIS FILE CONTAINS METHODS FOR NOTES PROCESSING           #
# YOU MAY IMPORT THIS FILE TO YOUR OWN SCRIPT               #
#############################################################
import json
try:
    with open(os.path.join(DirUtils.DATA_DIR, 'Notes.json'), 'r') as f:
        Notes = json.load(f)
except:
    print("Error: Notes.json not found")
    exit()


#############################################################
# getNoteNameById(noteId)                                   #
# Returns the note name of the note with the given id       #
# If the id is invalid, it returns "NULL"                   #
#############################################################
def getNoteNameById(noteId: int):
    if noteId is None or noteId < 1 or noteId > Notes['NoteCount']:
        return "NULL"
    else:
        return Notes['NoteFreq'][noteId-1]['Name']


#############################################################
# getNoteFreqById(noteId)                                   #
# Returns the frequency of the note with the given id       #
# If the id is invalid, it returns "0"                      #
#############################################################
def getNoteFreqById(noteId: int):
    if noteId < 1 or noteId > Notes['NoteCount']:
        return 0
    else:
        return Notes['NoteFreq'][noteId-1]['Freq']


#############################################################
# getNoteIdByName(noteName)                                 #
# Returns the id of the note with the given name            #
# If the name is invalid, it returns "0"                    #
#############################################################
def getNoteIdByName(noteName: str):
    if noteName is None or noteName == "NULL":
        return None
    for note in Notes['NoteFreq']:
        if note['Name'] == noteName:
            return note['Id']
    return None


#############################################################
# getNoteFreqByName(noteName)                               #
# Returns the frequency of the note with the given name     #
# If the name is invalid, it returns "0"                    #
#############################################################
def getNoteFreqByName(noteName: str):
    for note in Notes['NoteFreq']:
        if note['Name'] == noteName:
            return note['Freq']
    return 0


#############################################################
# createNote(noteId, noteLength)                            #
# Returns a Note ['Id', 'Length']                           #
# nodeId = None means that the note is an empty note        #
#############################################################
def createNote(noteId: int, noteLength: float):
    if type(noteId) == str:
        noteId = getNoteIdByName(noteId)
    return {
        'Id': noteId,
        'Length': noteLength
    }


#############################################################
# deepCopy(value)                                           #
# Returns a deep copy of the given value                    #
#############################################################
import json
def deepCopy(value: dict):
    return json.loads(json.dumps(value))


################################################################
# getNpTimeList                                                #
# THIS FUNCTION IS A BASIC FUNCION FOR COMPILING A NoteListSet #
################################################################
import numpy as np
def getNpTimeList(ArrayLength, SamplingRate):
    return np.linspace(0, ArrayLength/SamplingRate, ArrayLength)


#################################
# Get BEATS COUNT IN A NoteList #
#################################
def getLengthOfNoteList(NoteList):
    Length = 0
    for Note in NoteList:
        Length += Note['Length']
    return Length


####################################
# GET BEATS COUNT IN A NoteListSet #
####################################
def getLengthOfNoteListSet(NoteListSet):
    TotalLength = 0
    for NoteList in NoteListSet:
        Length = getLengthOfNoteList(NoteList)
        TotalLength = max(TotalLength, Length)
    return Length


#############################################################
# LinkNoteListSet(NoteListSetA, NoteListSetB)               #
#! WE ASSUME NOTE_LIST_SET HAS THE SAME track count         #
#############################################################
def LinkNoteListSet(NoteListSetA, NoteListSetB):
    NoteListSetA = deepCopy(NoteListSetA)
    NoteListSetB = deepCopy(NoteListSetB)
    if(len(NoteListSetA) != len(NoteListSetB)):
        print("Error: NoteListSetA and NoteListSetB have different track count")
        exit()
    total_len = getLengthOfNoteListSet(NoteListSetA)
    for i in range(len(NoteListSetA)):
        length = getLengthOfNoteList(NoteListSetA[i])
        if length < total_len:
            NoteListSetA[i].append(createNote(0, total_len - length))

    #############################################################
    # NOW EVERY NOTE_LIST in NoteListSetA HAS THE SAME LENGTH   #
    #############################################################
    for i in range(len(NoteListSetA)):
        NoteListSetA[i] += NoteListSetB[i]
    return NoteListSetA


#############################################################
# tuneNoteListSet(NoteListSet, Tuning)                      #
# change the base frequency of the NoteListSet              #
#############################################################
def tuneNote(Note, Tuning):
    Note = deepCopy(Note)
    if Note['Id'] is not None:
        Note['Id'] += Tuning
    return Note

def tuneNoteListSet(NoteListSet, Tuning):
    NoteListSet = deepCopy(NoteListSet)
    for i in range(len(NoteListSet)):
        for j in range(len(NoteListSet[i])):
            if NoteListSet[i][j]['Id'] is not None:
                NoteListSet[i][j]['Id'] += Tuning
    return NoteListSet


#############################################################
# distance(noteNameA, noteNameB)                            #
# solve the id distance between two notes                   #
#############################################################
def distance(noteNameA:str, noteNameB:str):
    return getNoteIdByName(noteNameA) - getNoteIdByName(noteNameB)


#############################################################
# LinkNoteListSetArray(ListOfNoteListSet:list)              #
# Link two or more NoteListSet together                     #
#############################################################
def LinkNoteListSetArray(ListOfNoteListSet:list):
    if len(ListOfNoteListSet) == 0:
        return []
    if len(ListOfNoteListSet) == 1:
        return ListOfNoteListSet[0]
    else:
        return LinkNoteListSet(ListOfNoteListSet[0], LinkNoteListSetArray(ListOfNoteListSet[1:]))


#############################################################
# changeSpeed(NoteListSet:list, factor:float)               #
# CHANGE THE SPEED OF A NOTE_LIST_SET                       #
#############################################################
def changeSpeed(NoteListSet:list, factor:float):
    NoteListSet = deepCopy(NoteListSet)
    if factor > 0 and factor != 1:
        for i in range(len(NoteListSet)):
            for j in range(len(NoteListSet[i])):
                NoteListSet[i][j]['Length'] *= factor
    return NoteListSet

#############################################################
# getNoteCntOfNoteListSet(NoteListSet:list)                 #
# GET THE COUNT OF NOTE IN A NOTE_LIST_SET                  #
# METHOD FOR music GAME                                     #
#############################################################
def getNoteCntOfNoteListSet(NoteListSet:list):
    NoteCnt = 0
    for i in range(len(NoteListSet)):
        for j in range(len(NoteListSet[i])):
            if NoteListSet[i][j]['Id'] is not None:
                NoteCnt += 1
    return NoteCnt


#############################################################
# solve BPM for a NoteListSet                               #
# this method is for the music game                         #
#############################################################
def solveBPM(NoteListSet:list, speed:float):
    Length  = getLengthOfNoteListSet(NoteListSet)
    NoteCnt = getNoteCntOfNoteListSet(NoteListSet)
    time    = Length * speed
    return NoteCnt / (time / 60)
