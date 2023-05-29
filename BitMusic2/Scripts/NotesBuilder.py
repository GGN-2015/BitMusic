import os
import DirUtils

######################
# NotesBuilder.py    #
# Author: GGN_2015   #
# Date  : 2022-07-20 #
######################

message = """
############################################################
# THIS FILS IS ONLY USED WHEN BUILDING THE DATA            #
# DO NOT RUN THIS FILE WHEN Notes.json EXIST               #
# LOAD THE DATA IN NoteFreq.json AND CREATE Notes.json     #
############################################################
"""

from pathlib import Path
my_file = Path(os.path.join(DirUtils.DATA_DIR, "Notes.json"))
if my_file.is_file():
    print(message)
    exit()


###############################################################
# YOU CAN ONLY RUN THIS FILE IF THE DATA IS NOT ALREADY BUILT #
###############################################################
import json

try:
    with open(os.path.join(DirUtils.DATA_DIR, 'NoteFreq.json'), 'r') as f:
        data = json.load(f)
except:
    print("Error: NoteFreq.json not found")
    exit()

mem = {
    'NoteCount': 0,
    'NoteFreq': []
}


############################################################
# mem IS THE VALUE OF JSON: Notes.json                     #
# IT CONTAINS A MAP FROM NoteName TO FREQUENCY             #
############################################################
cnt = 0
for note in data:
    cnt += 1
    mem['NoteFreq'].append(
        {
            'Id'  : cnt,
            'Name': note,
            'Freq': data[note]
        }
    )
    mem['NoteCount'] += 1

json.dump(mem, 
    open(os.path.join(DirUtils.DATA_DIR,'Notes.json'), 'w'), indent=4)
