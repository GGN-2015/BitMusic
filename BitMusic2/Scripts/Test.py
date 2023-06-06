
###########################################
# Test.py                                 #
# THIS FILE SHOULD NOT BE EDITTED BY USER #
###########################################
import Chords
import Compile
import Methods
import TimbreSgn
import TimbreGuitar


###################################################
# test001()                                       #
# USE THIS FUNCTION TO TEST GENERATE A DEMO SONG  #
###################################################
def test001():
    #############################################################
    # acc001 ~ acc016                                           #
    #############################################################
    acc001 = Chords.Pattern002("C3")
    acc002 = Chords.Pattern002("E3")
    acc003 = Chords.Pattern002("F3")
    acc004 = Chords.Pattern002("C3")
    acc005 = Chords.Pattern002("D3")
    acc006 = Chords.Pattern002("E3")
    acc007 = Chords.Pattern002("F3")
    acc008 = Chords.Pattern002("G3")
    acc009 = Chords.Pattern002("C3")
    acc010 = Chords.Pattern002("G3")
    acc011 = Chords.Pattern002("A3")
    acc012 = Chords.Pattern002("E3")
    acc013 = Chords.Pattern002("F3")
    acc014 = Chords.Pattern002("C2")
    acc015 = Chords.Pattern002("D3")
    acc016 = Chords.Pattern002("G3")


    #############################################################
    # sub001 ~ sub016                                           #
    #############################################################
    sub001 = Chords.Pattern003("C3")
    sub002 = Chords.Pattern003("E3")
    sub003 = Chords.Pattern003("F3")
    sub004 = Chords.Pattern003("C3")
    sub005 = Chords.Pattern003("D3")
    sub006 = Chords.Pattern003("E3")
    sub007 = Chords.Pattern003("F3")
    sub008 = Chords.Pattern003("G3")
    sub009 = Chords.Pattern003("C3")
    sub010 = Chords.Pattern003("G3")
    sub011 = Chords.Pattern003("A3")
    sub012 = Chords.Pattern003("E3")
    sub013 = Chords.Pattern003("F3")
    sub014 = Chords.Pattern003("C2")
    sub015 = Chords.Pattern003("D3")
    sub016 = Chords.Pattern003("G3")


    #############################################################
    # main001 ~ main016                                         #
    #############################################################
    main = [
        [
            Methods.createNote("C5", 2), # 001
            Methods.createNote("G4", 1),
            Methods.createNote("A4", 1),
            Methods.createNote("B4", 2), # 002
            Methods.createNote("E4", 1),
            Methods.createNote("E4", 1),
            Methods.createNote("A4", 2), # 003
            Methods.createNote("G4", 1),
            Methods.createNote("F4", 1),
            Methods.createNote("G4", 2), # 004
            Methods.createNote("C4", 2),

            Methods.createNote("D4", 1.8), Methods.createNote("NULL", 0.2), # 005
            Methods.createNote("D4", 1),
            Methods.createNote("E4", 1),
            Methods.createNote("F4", 1.8), Methods.createNote("NULL", 0.2), # 006
            Methods.createNote("F4", 1),
            Methods.createNote("G4", 1),
            Methods.createNote("A4", 2), # 007
            Methods.createNote("B4", 1),
            Methods.createNote("C5", 1),
            Methods.createNote("D5", 3), # 008
            Methods.createNote("G4", 1),

            Methods.createNote("E5", 2), # 009
            Methods.createNote("D5", 1),
            Methods.createNote("C5", 1),
            Methods.createNote("D5", 2), # 010
            Methods.createNote("B4", 1),
            Methods.createNote("G4", 1),
            Methods.createNote("C5", 2), # 011
            Methods.createNote("B4", 1),
            Methods.createNote("A4", 1),
            Methods.createNote("B4", 2), # 012
            Methods.createNote("E4", 2),
            
            Methods.createNote("A4", 2), # 013
            Methods.createNote("G4", 1),
            Methods.createNote("F4", 1),
            Methods.createNote("G4", 2), # 014
            Methods.createNote("C4", 2),
            Methods.createNote("C5", 2), # 015
            Methods.createNote("B4", 1),
            Methods.createNote("A4", 1),
            Methods.createNote("G4", 3), # 016
            Methods.createNote("G4", 1),
        ]
    ]
    

    ###############################################################
    # tune                                                        #
    ###############################################################
    acc  = Methods.LinkNoteListSetArray([
        acc001, acc002, acc003, acc004, acc005, acc006, acc007, acc008,
        acc009, acc010, acc011, acc012, acc013, acc014, acc015, acc016
    ])
    sub = Methods.LinkNoteListSetArray([
        sub001, sub002, sub003, sub004, sub005, sub006, sub007, sub008,
        sub009, sub010, sub011, sub012, sub013, sub014, sub015, sub016
    ])
    TUNE_TO = "D#3"
    acc  = Methods.tuneNoteListSet(acc , Methods.distance(TUNE_TO, "C3"))
    sub  = Methods.tuneNoteListSet(sub , Methods.distance(TUNE_TO, "C3"))
    main = Methods.tuneNoteListSet(main, Methods.distance(TUNE_TO, "C3"))


    ###############################################################
    # Compile.compile()                                           #
    ###############################################################
    acc_compiled  = Compile.compileNoteListSet(acc , 0.3, TimbreSgn, 44100, 0.1)
    sub_compiled  = Compile.compileNoteListSet(sub , 0.3, TimbreSgn, 44100, 0.05)
    main_compiled = Compile.compileNoteListSet(main, 0.3, TimbreSgn, 44100, 0.2)
    music  = acc_compiled
    music += sub_compiled
    music += main_compiled
    Compile.dumpWAV(music, "./WAV/Test001.wav")


###############################################################
# test002                                                     #
###############################################################
def test002():
    #############################################################
    # acc001 ~ acc004                                           #
    #############################################################
    acc001 = Chords.Pattern006("A3", 2)
    acc002 = Chords.Pattern006("G3", 2)
    acc003 = Chords.Pattern006("F3", 2)
    acc004 = Chords.Pattern006("E3", 2)
    acc005 = Chords.Pattern006("A3", 2)
    acc006 = Chords.Pattern006("G3", 2)
    acc007 = Chords.Pattern006("F3", 2)
    acc008 = Chords.Pattern006("E3", 2)

    #############################################################
    # main001 ~ main004                                         #
    #############################################################
    main = [[
        Methods.createNote("A4", 1.0), # 001
        Methods.createNote("C5", 1.0),
        Methods.createNote("B4", 1.0),
        Methods.createNote("C5", 1.0),
        Methods.createNote("D5", 1.0),
        Methods.createNote("C5", 1.0),
        Methods.createNote("G4", 1.0), # 002
        Methods.createNote("C5", 1.0),
        Methods.createNote("B4", 1.0),
        Methods.createNote("C5", 1.0),
        Methods.createNote("D5", 1.0),
        Methods.createNote("C5", 1.0),
        Methods.createNote("F4", 1.0), # 003
        Methods.createNote("C5", 1.0),
        Methods.createNote("B4", 1.0),
        Methods.createNote("C5", 1.0),
        Methods.createNote("D5", 1.0),
        Methods.createNote("C5", 1.0),
        Methods.createNote("E4", 1.0), # 004
        Methods.createNote("F#4", 1.0),
        Methods.createNote("G#4", 1.0),
        Methods.createNote("A4", 1.0),
        Methods.createNote("B4", 1.0),
        Methods.createNote("E4", 1.0),
        Methods.createNote("A4", 1.0), # 005
        Methods.createNote("C5", 1.0),
        Methods.createNote("B4", 1.0),
        Methods.createNote("C5", 1.0),
        Methods.createNote("D5", 1.0),
        Methods.createNote("C5", 1.0),
        Methods.createNote("G4", 1.0), # 006
        Methods.createNote("C5", 1.0),
        Methods.createNote("B4", 1.0),
        Methods.createNote("C5", 1.0),
        Methods.createNote("D5", 1.0),
        Methods.createNote("C5", 1.0),
        Methods.createNote("F4", 1.0), # 007
        Methods.createNote("C5", 1.0),
        Methods.createNote("B4", 1.0),
        Methods.createNote("C5", 1.0),
        Methods.createNote("D5", 1.0),
        Methods.createNote("C5", 1.0),
        Methods.createNote("D5", 1.0), # 008
        Methods.createNote("C5", 1.0),
        Methods.createNote("D5", 1.0),
        Methods.createNote("E5", 1.0),
        Methods.createNote("B4", 2.0),
        
    ]]

    #############################################################
    # tune                                                      #
    #############################################################
    acc = Methods.LinkNoteListSetArray(
        [
            acc001, acc002, acc003, acc004, acc005, acc006, acc007, acc008
        ]
    )
    acc  = Methods.tuneNoteListSet(acc, Methods.distance("D#3", "C3"))
    main = Methods.tuneNoteListSet(main, Methods.distance("D#3", "C3"))

    #############################################################
    # Compile.compile()                                         #
    #############################################################
    acc_compiled  = Compile.compileNoteListSet(acc , 0.2, TimbreSgn, 44100, 0.1)
    main_compiled = Compile.compileNoteListSet(main, 0.2, TimbreSgn, 44100, 0.2)
    music  = acc_compiled
    music += main_compiled
    Compile.dumpWAV(music, "./WAV/Test002.wav")


###############################################################
# test003                                                     #
###############################################################
def test003():
    #############################################################
    # acc001 ~ acc008                                           #
    #############################################################
    acc001 = Chords.Pattern006("A3", 2)
    acc002 = Chords.Pattern006("E3", 2)
    acc003 = Chords.Pattern006("F3", 2)
    acc004 = Chords.Pattern006("E3", 2)
    acc005 = Chords.Pattern006("A3", 2)
    acc006 = Chords.Pattern006("F3", 2)
    acc007 = Chords.Pattern006("E3", 2)
    acc008 = Chords.Pattern006("A3", 2)

    #############################################################
    # main001 ~ main008                                         #
    #############################################################
    main = [[
        Methods.createNote("A4", 2.0), # 001
        Methods.createNote("E4", 2.0),
        Methods.createNote("C5", 2.0),
        Methods.createNote("B4", 1.0), # 002
        Methods.createNote("C5", 1.0),
        Methods.createNote("B4", 1.0),
        Methods.createNote("G4", 1.0),
        Methods.createNote("E4", 1.0),
        Methods.createNote("G4", 1.0),
        Methods.createNote("A4", 1.0), # 003
        Methods.createNote("C4", 1.0),
        Methods.createNote("G4", 1.0),
        Methods.createNote("C4", 1.0),
        Methods.createNote("F4", 1.0),
        Methods.createNote("C4", 1.0),
        Methods.createNote("G#4", 1.0), # 004
        Methods.createNote("E4", 1.0),
        Methods.createNote("A4", 1.0),
        Methods.createNote("E4", 1.0),
        Methods.createNote("B4", 1.0),
        Methods.createNote("E4", 1.0),
        Methods.createNote("A4", 1.0), # 005
        Methods.createNote("E4", 1.0),
        Methods.createNote("E4", 1.0),
        Methods.createNote("A4", 1.0),
        Methods.createNote("C5", 1.0),
        Methods.createNote("A4", 1.0),
        Methods.createNote("D5", 1.0), # 006
        Methods.createNote("E5", 1.0),
        Methods.createNote("D5", 1.0),
        Methods.createNote("C5", 1.0),
        Methods.createNote("B4", 1.0),
        Methods.createNote("G4", 1.0),
        Methods.createNote("A4", 1.0), # 007
        Methods.createNote("E4", 1.0),
        Methods.createNote("C5", 1.0),
        Methods.createNote("D5", 1.0),
        Methods.createNote("B4", 1.0),
        Methods.createNote("G4", 1.0),
        Methods.createNote("A4", 6.0), # 008
    ]]

    #############################################################
    # tune                                                      #
    #############################################################
    acc = Methods.LinkNoteListSetArray([
            acc001, acc002, acc003, acc004, acc005, acc006, acc007, acc008
    ])
    acc  = Methods.tuneNoteListSet(acc, Methods.distance("D#3", "C3"))
    main = Methods.tuneNoteListSet(main, Methods.distance("D#3", "C3"))

    #############################################################
    # Compile.compile()                                         #
    #############################################################
    acc_compiled  = Compile.compileNoteListSet(acc , 0.2, TimbreSgn, 44100, 0.1)
    main_compiled = Compile.compileNoteListSet(main, 0.2, TimbreSgn, 44100, 0.2)
    music  = acc_compiled
    music += main_compiled
    Compile.dumpWAV(music, "./WAV/Test003.wav")


###############################################################
# test004                                                     #
###############################################################
import numpy as np
def test004():
    #############################################################
    # acc000 ~ acc008                                           #
    #############################################################
    acc000 = [[
        Methods.createNote("NULL", 4)
    ]]
    acc001 = Chords.Pattern007("F3", 0.5, 2)
    acc002 = Chords.Pattern007("G3", 0.5, 2)
    acc003 = Chords.Pattern007("A3", 0.5, 2)
    acc004 = Chords.Pattern007("E3", 0.5, 2)
    acc005 = Chords.Pattern007("F3", 0.5, 2)
    acc006 = Chords.Pattern007("G3", 0.5, 2)
    acc007 = Chords.Pattern007("E3", 0.5, 2)
    acc008 = Methods.LinkNoteListSet(Chords.Pattern007("D3", 0.5), Chords.Pattern007("A3", 0.5))
    acc009 = Chords.Pattern007("F3", 0.5, 2)
    acc010 = Chords.Pattern007("G3", 0.5, 2)
    acc011 = Chords.Pattern007("A3", 0.5, 2)
    acc012 = Chords.Pattern007("E3", 0.5, 2)
    acc013 = Chords.Pattern007("F3", 0.5, 2)
    acc014 = Chords.Pattern007("G3", 0.5, 2)
    acc015 = Chords.Pattern007("E3", 0.5, 2)
    acc016 = Methods.LinkNoteListSet(Chords.Pattern007("D3", 0.5), Chords.Pattern007("A3", 0.5))

    #############################################################
    # sub000 ~ sub008                                           #
    #############################################################
    sub000 = [[
        Methods.createNote("NULL", 4)
    ]]
    sub001 = Chords.Pattern007("F3")
    sub002 = Chords.Pattern007("G3")
    sub003 = Chords.Pattern007("A3")
    sub004 = Chords.Pattern007("E3")
    sub005 = Chords.Pattern007("F3")
    sub006 = Chords.Pattern007("G3")
    sub007 = Chords.Pattern007("E3")
    sub008 = Methods.LinkNoteListSet(Chords.Pattern007("D3", 0.5), Chords.Pattern007("A3", 0.5))
    sub009 = Chords.Pattern007("F3")
    sub010 = Chords.Pattern007("G3")
    sub011 = Chords.Pattern007("A3")
    sub012 = Chords.Pattern007("E3")
    sub013 = Chords.Pattern007("F3")
    sub014 = Chords.Pattern007("G3")
    sub015 = Chords.Pattern007("E3")
    sub016 = Methods.LinkNoteListSet(Chords.Pattern007("D3", 0.5), Chords.Pattern007("A3", 0.5))


    #############################################################
    # main001 ~ main008                                         #
    #############################################################
    main = [[
        Methods.createNote("NULL", 3.0), # 000
        Methods.createNote("G4", 0.5),
        Methods.createNote("G#4", 0.5),
        Methods.createNote("A4", 1.0), # 001
        Methods.createNote("D5", 1.0),
        Methods.createNote("A4", 1.0),
        Methods.createNote("G4", 0.5),
        Methods.createNote("G#4", 0.5),
        Methods.createNote("A4", 1.0), # 002
        Methods.createNote("E5", 1.0),
        Methods.createNote("A4", 1.0),
        Methods.createNote("G4", 0.5),
        Methods.createNote("G#4", 0.5),
        Methods.createNote("A4", 1.0), # 003
        Methods.createNote("C5", 1.0),
        Methods.createNote("A4", 1.0),
        Methods.createNote("G4", 1.0),
        Methods.createNote("G#4", 0.5), # 004
        Methods.createNote("F#4", 0.5),
        Methods.createNote("E4", 0.5), 
        Methods.createNote("F#4", 0.5),
        Methods.createNote("G#4", 1.0),
        Methods.createNote("G4", 0.5),
        Methods.createNote("G#4", 0.5),
        Methods.createNote("A4", 1.0), # 005
        Methods.createNote("D5", 1.0),
        Methods.createNote("A4", 1.0),
        Methods.createNote("G4", 0.5),
        Methods.createNote("G#4", 0.5),
        Methods.createNote("A4", 1.0), # 006
        Methods.createNote("E5", 1.0),
        Methods.createNote("A4", 1.0),
        Methods.createNote("G4", 0.5),
        Methods.createNote("G#4", 0.5),
        Methods.createNote("A4", 1.0), # 007
        Methods.createNote("C5", 1.0),
        Methods.createNote("D5", 1.0),
        Methods.createNote("E5", 1.0),
        Methods.createNote("D5", 0.5), # 008
        Methods.createNote("C5", 0.5),
        Methods.createNote("D5", 0.5),
        Methods.createNote("E5", 0.5),
        Methods.createNote("A4", 1.0),
        Methods.createNote("G4", 0.5),
        Methods.createNote("G#4", 0.5),
        Methods.createNote("A4", 1.0), # 009
        Methods.createNote("D5", 1.0),
        Methods.createNote("A4", 1.0),
        Methods.createNote("G4", 0.5),
        Methods.createNote("G#4", 0.5),
        Methods.createNote("A4", 1.0), # 010
        Methods.createNote("E5", 1.0),
        Methods.createNote("A4", 1.0),
        Methods.createNote("G4", 0.5),
        Methods.createNote("G#4", 0.5),
        Methods.createNote("A4", 1.0), # 011
        Methods.createNote("C5", 1.0),
        Methods.createNote("A4", 1.0),
        Methods.createNote("G4", 1.0),
        Methods.createNote("G#4", 0.5), # 012
        Methods.createNote("F#4", 0.5),
        Methods.createNote("E4", 0.5), 
        Methods.createNote("F#4", 0.5),
        Methods.createNote("G#4", 1.0),
        Methods.createNote("G4", 0.5),
        Methods.createNote("G#4", 0.5),
        Methods.createNote("A4", 1.0), # 013
        Methods.createNote("D5", 1.0),
        Methods.createNote("A4", 1.0),
        Methods.createNote("G4", 0.5),
        Methods.createNote("G#4", 0.5),
        Methods.createNote("A4", 1.0), # 014
        Methods.createNote("E5", 1.0),
        Methods.createNote("A4", 1.0),
        Methods.createNote("G4", 0.5),
        Methods.createNote("G#4", 0.5),
        Methods.createNote("A4", 1.0), # 015
        Methods.createNote("C5", 1.0),
        Methods.createNote("D5", 1.0),
        Methods.createNote("E5", 1.0),
        Methods.createNote("D5", 0.5), # 016
        Methods.createNote("C5", 0.5),
        Methods.createNote("E5", 0.5),
        Methods.createNote("G5", 0.5),
        Methods.createNote("A5", 2.0),

    ]]

    #############################################################
    # tune                                                      #
    #############################################################
    acc = Methods.LinkNoteListSetArray([
        acc000, 
        acc001, acc002, acc003, acc004, acc005, acc006, acc007, acc008,
        acc009, acc010, acc011, acc012, acc013, acc014, acc015, acc016,
    ])
    sub = Methods.LinkNoteListSetArray([
        sub000, 
        sub001, sub002, sub003, sub004, sub005, sub006, sub007, sub008,
        sub009, sub010, sub011, sub012, sub013, sub014, sub015, sub016,
    ])
    acc  = Methods.tuneNoteListSet(acc, Methods.distance("D#3", "C3"))
    sub  = Methods.tuneNoteListSet(sub, Methods.distance("D#2", "C3"))
    main = Methods.tuneNoteListSet(main, Methods.distance("D#3", "C3"))
    print(Methods.solveBPM(main, 0.2))

    #############################################################
    # Compile.compile()                                         #
    #############################################################
    acc_compiled  = Compile.compileNoteListSet(acc , 0.2, TimbreSgn, 44100, 0.1)
    sub_compiled  = Compile.compileNoteListSet(sub , 0.2, TimbreSgn, 44100, 0.1)
    main_compiled = Compile.compileNoteListSet(main, 0.2, TimbreSgn, 44100, 0.2)
    music  = acc_compiled
    music += sub_compiled
    music += main_compiled
    Compile.dumpWAV(music, "./WAV/Test004.wav")


#############################################################
# Test005                                                   #
#############################################################
def test005():
    #############################################################
    # acc                                                       #
    #############################################################
    acc001 = Chords.Pattern007("E3", 0.5, 2)
    acc002 = Chords.Pattern007("A3", 0.5, 2)
    acc003 = Chords.Pattern007("F3", 0.5, 2)
    acc004 = Chords.Pattern007("E4", 0.5, 2)
    acc005 = Chords.Pattern007("E3", 0.5, 2)
    acc006 = Chords.Pattern007("A3", 0.5, 2)
    acc007 = Chords.Pattern007("D3", 0.5, 2)
    acc008 = Methods.LinkNoteListSet(Chords.Pattern007("E4", 0.5), Chords.Pattern007("A4", 0.5))
    acc009 = Chords.Pattern007("E3", 0.5, 2)
    acc010 = Chords.Pattern007("A3", 0.5, 2)
    acc011 = Chords.Pattern007("F3", 0.5, 2)
    acc012 = Chords.Pattern007("E4", 0.5, 2)
    acc013 = Chords.Pattern007("E3", 0.5, 2)
    acc014 = Chords.Pattern007("A3", 0.5, 2)
    acc015 = Chords.Pattern007("D3", 0.5, 2)
    acc016 = Methods.LinkNoteListSet(Chords.Pattern007("E4", 0.5), Chords.Pattern007("A4", 0.5))

    ##############################################################
    # sub                                                        #
    ##############################################################
    sub001 = Chords.Pattern007("E3")
    sub002 = Chords.Pattern007("A3")
    sub003 = Chords.Pattern007("F3")
    sub004 = Chords.Pattern007("E4")
    sub005 = Chords.Pattern007("E3")
    sub006 = Chords.Pattern007("A3")
    sub007 = Chords.Pattern007("D3")
    sub008 = Methods.LinkNoteListSet(Chords.Pattern007("E4", 0.5), Chords.Pattern007("A4", 0.5))
    sub009 = Chords.Pattern007("E3")
    sub010 = Chords.Pattern007("A3")
    sub011 = Chords.Pattern007("F3")
    sub012 = Chords.Pattern007("E4")
    sub013 = Chords.Pattern007("E3")
    sub014 = Chords.Pattern007("A3")
    sub015 = Chords.Pattern007("D3")
    sub016 = Methods.LinkNoteListSet(Chords.Pattern007("E4", 0.5), Chords.Pattern007("A4", 0.5))

    #############################################################
    # main                                                      #
    #############################################################
    main = [[
        Methods.createNote("E5", 1), # 001
        Methods.createNote("E5", 0.5),
        Methods.createNote("F#5", 0.5),
        Methods.createNote("G#5", 0.5),
        Methods.createNote("A5", 0.5),
        Methods.createNote("E5", 1),
        Methods.createNote("A5", 1), # 002
        Methods.createNote("A5", 0.5),
        Methods.createNote("B5", 0.5),
        Methods.createNote("C#6", 0.5),
        Methods.createNote("D6", 0.5),
        Methods.createNote("A5", 1),
        Methods.createNote("D5", 0.5), # 003
        Methods.createNote("D6", 0.5),
        Methods.createNote("C5", 0.5),
        Methods.createNote("C6", 0.5),
        Methods.createNote("B4", 0.5),
        Methods.createNote("B5", 0.5),
        Methods.createNote("A4", 0.5),
        Methods.createNote("A5", 0.5),
        Methods.createNote("G#4", 0.5), # 004
        Methods.createNote("G#5", 0.5),
        Methods.createNote("A4", 0.5),
        Methods.createNote("A5", 0.5),
        Methods.createNote("B4", 2), 
        Methods.createNote("E5", 1), # 005
        Methods.createNote("E5", 0.5),
        Methods.createNote("F#5", 0.5),
        Methods.createNote("G#5", 0.5),
        Methods.createNote("A5", 0.5),
        Methods.createNote("E5", 1),
        Methods.createNote("A5", 1), # 006
        Methods.createNote("A5", 0.5),
        Methods.createNote("B5", 0.5),
        Methods.createNote("C#6", 0.5),
        Methods.createNote("D6", 0.5),
        Methods.createNote("A5", 1),
        Methods.createNote("D5", 0.5), # 007
        Methods.createNote("D6", 0.5),
        Methods.createNote("C5", 0.5),
        Methods.createNote("C6", 0.5),
        Methods.createNote("B4", 0.5),
        Methods.createNote("B5", 0.5),
        Methods.createNote("A4", 0.5),
        Methods.createNote("A5", 0.5),
        Methods.createNote("G#4", 0.5), # 008
        Methods.createNote("G#5", 0.5),
        Methods.createNote("B4", 0.5),
        Methods.createNote("B5", 0.5),
        Methods.createNote("A4", 2.0), 
    ]]
    main = Methods.LinkNoteListSet(main, Methods.tuneNoteListSet(main, Methods.distance("C2", "C3")))
    
    #############################################################
    # tune                                                      #
    #############################################################
    acc = Methods.LinkNoteListSetArray([
        acc001, acc002, acc003, acc004, acc005, acc006, acc007, acc008,
        acc009, acc010, acc011, acc012, acc013, acc014, acc015, acc016,
    ])
    sub = Methods.LinkNoteListSetArray([
        sub001, sub002, sub003, sub004, sub005, sub006, sub007, sub008,
        sub009, sub010, sub011, sub012, sub013, sub014, sub015, sub016,
    ])
    main = Methods.tuneNoteListSet(main, Methods.distance("D#3", "C3"))
    acc  = Methods.tuneNoteListSet(acc, Methods.distance("D#3", "C3"))
    sub  = Methods.tuneNoteListSet(sub, Methods.distance("D#2", "C3"))
    # print(Methods.solveBPM(main, 0.2))

    #############################################################
    # Compile.compile()                                         #
    #############################################################
    acc_compiled  = Compile.compileNoteListSet(acc , 0.2, TimbreSgn, 44100, 0.1)
    sub_compiled  = Compile.compileNoteListSet(sub , 0.2, TimbreSgn, 44100, 0.14)
    main_compiled = Compile.compileNoteListSet(main, 0.2, TimbreSgn, 44100, 0.2)
    music  = acc_compiled
    music += sub_compiled
    music += main_compiled
    Compile.dumpWAV(music, "./WAV/Test005.wav")


###############################################################
# test006                                                     #
###############################################################
def test006():
    #############################################################
    # acc                                                       #
    #############################################################
    acc001 = Chords.Pattern006("A3")
    acc002 = Chords.Pattern006("D3")
    acc003 = Chords.Pattern006("G3")
    acc004 = Chords.Pattern006("C4")
    acc005 = Chords.Pattern006("F3")
    acc006 = Chords.Pattern006_dim("B3")
    acc007 = Chords.Pattern006("E3")
    acc008 = Chords.Pattern006("E3")
    acc009 = Chords.Pattern006("A3")

    #############################################################
    # main                                                      #
    #############################################################
    main = [[
        Methods.createNote("A5", 0.5), # 001
        Methods.createNote("B5", 0.5),
        Methods.createNote("C6", 0.5),
        Methods.createNote("E5", 0.5),
        Methods.createNote("G5", 0.5),
        Methods.createNote("F5", 0.5),
        Methods.createNote("F5", 2.0), # 002
        Methods.createNote("D5", 1.0),
        Methods.createNote("G5", 0.5), # 003
        Methods.createNote("A5", 0.5),
        Methods.createNote("B5", 0.5),
        Methods.createNote("D5", 0.5),
        Methods.createNote("F5", 0.5),
        Methods.createNote("E5", 0.5),
        Methods.createNote("E5", 2.0), # 004
        Methods.createNote("C5", 1.0),
        Methods.createNote("F5", 0.5), # 005
        Methods.createNote("G5", 0.5),
        Methods.createNote("A5", 0.5),
        Methods.createNote("C5", 0.5),
        Methods.createNote("E5", 0.5),
        Methods.createNote("D5", 0.5),
        Methods.createNote("D5", 2.0), # 006
        Methods.createNote("B4", 0.5),
        Methods.createNote("C5", 0.5),
        Methods.createNote("D5", 0.5), # 007
        Methods.createNote("F5", 0.5),
        Methods.createNote("E5", 0.5),
        Methods.createNote("D5", 0.5),
        Methods.createNote("E5", 0.5),
        Methods.createNote("F#5", 0.5),
        Methods.createNote("G#5", 2.0), # 008
        Methods.createNote("E5", 1.0),
        Methods.createNote("A5", 0.5), # 009
        Methods.createNote("B5", 0.5),
        Methods.createNote("C6", 0.5),
        Methods.createNote("E5", 0.5),
        Methods.createNote("G5", 0.5),
        Methods.createNote("F5", 0.5),
        Methods.createNote("F5", 2.0), # 010
        Methods.createNote("D5", 1.0),
        Methods.createNote("G5", 0.5), # 011
        Methods.createNote("A5", 0.5),
        Methods.createNote("B5", 0.5),
        Methods.createNote("D5", 0.5),
        Methods.createNote("F5", 0.5),
        Methods.createNote("E5", 0.5),
        Methods.createNote("E5", 2.0), # 012
        Methods.createNote("C5", 1.0),
        Methods.createNote("F5", 0.5), # 013
        Methods.createNote("G5", 0.5),
        Methods.createNote("A5", 0.5),
        Methods.createNote("C5", 0.5),
        Methods.createNote("E5", 0.5),
        Methods.createNote("D5", 0.5),
        Methods.createNote("D5", 2.0), # 014
        Methods.createNote("B4", 0.5),
        Methods.createNote("C5", 0.5),
        Methods.createNote("E5", 0.5), # 015
        Methods.createNote("D5", 0.5),
        Methods.createNote("C5", 0.5),
        Methods.createNote("D5", 0.5),
        Methods.createNote("C5", 0.5),
        Methods.createNote("B4", 0.5),
        Methods.createNote("A4", 3.0), # 016
    ]]

    #############################################################
    # tune                                                      #
    #############################################################
    acc = Methods.LinkNoteListSetArray([
        acc001, acc002, acc003, acc004, acc005, acc006, acc007, acc008,
        acc001, acc002, acc003, acc004, acc005, acc006, acc007, acc009,
    ])
    acc  = Methods.tuneNoteListSet(acc, Methods.distance("D#3", "C3"))
    main = Methods.tuneNoteListSet(main, Methods.distance("D#3", "C3"))

    #############################################################
    # Compile.compile()                                         #
    #############################################################
    
    import TimbreSine
    acc_compiled  = Compile.compileNoteListSet(acc , 0.6, TimbreSine, 44100, 0.1)
    main_compiled = Compile.compileNoteListSet(main, 0.6, TimbreSine, 44100, 0.2)
    music  = acc_compiled
    music += main_compiled
    Compile.dumpWAV(music, "./WAV/Test006.wav")


###############################################################
# test007                                                     #
###############################################################
def test007():
    #############################################################
    # acc                                                       #
    #############################################################
    acc = [[
        Methods.createNote("E4", 1), # 001
        Methods.createNote("G4", 1),
        Methods.createNote("E4", 1),
        Methods.createNote("B3", 1),
        Methods.createNote("C4", 1), # 002
        Methods.createNote("B3", 0.5),
        Methods.createNote("A3", 0.5),
        Methods.createNote("B3", 1),
        Methods.createNote("E3", 1),
        Methods.createNote("C4", 1), # 003
        Methods.createNote("B3", 0.5),
        Methods.createNote("A3", 0.5),
        Methods.createNote("B3", 1),
        Methods.createNote("E3", 1),
        Methods.createNote("G4", 1), # 004
        Methods.createNote("A4", 1),
        Methods.createNote("F#4", 2),
        Methods.createNote("E4", 1), # 005
        Methods.createNote("G4", 1),
        Methods.createNote("E4", 1),
        Methods.createNote("B3", 1),
        Methods.createNote("C4", 1), # 006
        Methods.createNote("B3", 0.5),
        Methods.createNote("A3", 0.5),
        Methods.createNote("B3", 1),
        Methods.createNote("E3", 1),
        Methods.createNote("C4", 1), # 007
        Methods.createNote("B3", 0.5),
        Methods.createNote("A3", 0.5),
        Methods.createNote("B3", 1),
        Methods.createNote("E4", 1),
        Methods.createNote("F#4", 1), # 008
        Methods.createNote("G4", 1),
        Methods.createNote("E4", 2),
    ]]

    #############################################################
    # main                                                      #
    #############################################################
    main = [[
        Methods.createNote("G5", 0.5), # 001
        Methods.createNote("F#5", 0.5),
        Methods.createNote("E5", 0.5),
        Methods.createNote("G5", 0.5),
        Methods.createNote("A5", 0.5),
        Methods.createNote("G5", 0.5),
        Methods.createNote("F#5", 0.5),
        Methods.createNote("D5", 0.5),
        Methods.createNote("E5", 0.5), # 002
        Methods.createNote("A5", 0.5),
        Methods.createNote("G5", 0.5),
        Methods.createNote("F#5", 0.5),
        Methods.createNote("G5", 0.5),
        Methods.createNote("A5", 0.5),
        Methods.createNote("B5", 0.5),
        Methods.createNote("C6", 0.5),
        Methods.createNote("A5", 0.5), # 003
        Methods.createNote("E5", 0.5),
        Methods.createNote("E5", 0.5),
        Methods.createNote("C4", 0.5),
        Methods.createNote("G5", 0.5),
        Methods.createNote("F#5", 0.5),
        Methods.createNote("G5", 0.5),
        Methods.createNote("E5", 0.5),
        Methods.createNote("B4", 0.5), # 004
        Methods.createNote("C5", 0.5),
        Methods.createNote("D5", 1),
        Methods.createNote("B4", 2),
        Methods.createNote("G5", 0.5), # 005
        Methods.createNote("F#5", 0.5),
        Methods.createNote("E5", 0.5),
        Methods.createNote("G5", 0.5),
        Methods.createNote("A5", 0.5),
        Methods.createNote("G5", 0.5),
        Methods.createNote("F#5", 0.5),
        Methods.createNote("D5", 0.5),
        Methods.createNote("E5", 0.5), # 006
        Methods.createNote("A5", 0.5),
        Methods.createNote("G5", 0.5),
        Methods.createNote("F#5", 0.5),
        Methods.createNote("G5", 0.5),
        Methods.createNote("A5", 0.5),
        Methods.createNote("B5", 0.5),
        Methods.createNote("C6", 0.5),
        Methods.createNote("A5", 0.5), # 007
        Methods.createNote("E5", 0.5),
        Methods.createNote("E5", 0.5),
        Methods.createNote("C4", 0.5),
        Methods.createNote("G5", 0.5),
        Methods.createNote("F#5", 0.5),
        Methods.createNote("G5", 0.5),
        Methods.createNote("E5", 0.5),
        Methods.createNote("D5", 0.5), # 008
        Methods.createNote("C5", 0.5),
        Methods.createNote("B4", 0.5),
        Methods.createNote("F#4", 0.5),
        Methods.createNote("E5", 2),
    ]]

    #############################################################
    # tune                                                      #
    #############################################################
    # acc  = Methods.tuneNoteListSet(acc, Methods.distance("A3", "E3"))
    # main = Methods.tuneNoteListSet(main, Methods.distance("A3", "E3"))

    #############################################################
    # compiled                                                  #
    #############################################################
    acc_compiled  = Compile.compileNoteListSet(acc , 0.4, TimbreSgn, 44100, 0.2)
    main_compiled = Compile.compileNoteListSet(main, 0.4, TimbreSgn, 44100, 0.2)
    music = acc_compiled + main_compiled
    Compile.dumpWAV(music, "./WAV/test007.wav")
    
# create sine wave
def TestSine():
    import TimbreSine
    main = [
        [
            Methods.createNote("C4", 8),
        ],
        [
            Methods.createNote("E4", 8),
        ],
        [
            Methods.createNote("G4", 8),
        ],
        [
            Methods.createNote("C5", 8),
        ]
    ]
    main_compiled = Compile.compileNoteListSet(main, 0.4, TimbreSine, 44100, 0.2)
    music = main_compiled
    Compile.dumpWAV(music, "./WAV/TestSine.wav")

###############################################################
# test008                                                     #
###############################################################
def test008():
    #############################################################
    # acc                                                       #
    #############################################################
    acc001 = Chords.Pattern007("C2")
    acc002 = Chords.Pattern007("G2")
    acc003 = Chords.Pattern007("A2")
    acc004 = Chords.Pattern007("E2")
    acc005 = Chords.Pattern007("F2")
    acc006 = Chords.Pattern007("C2")
    acc007 = Chords.Pattern007("D2")
    acc008 = Chords.Pattern007("G2")
    acc009 = Chords.Pattern007("C2")
    acc010 = Chords.Pattern007("G2")
    acc011 = Chords.Pattern007("A2")
    acc012 = Chords.Pattern007("E2")
    acc013 = Chords.Pattern007("F2")
    acc014 = Chords.Pattern007("C2")
    acc015 = Chords.Pattern007("G2")
    acc016 = Chords.Pattern007("C2")
    acc  = Methods.LinkNoteListSetArray([
        acc001, acc002, acc003, acc004, acc005, acc006, acc007, acc008,
        acc009, acc010, acc011, acc012, acc013, acc014, acc015, acc016
    ])

    #############################################################
    # main                                                      #
    #############################################################
    main = [[
        Methods.createNote("E4", 2),
        Methods.createNote("G4", 1),
        Methods.createNote("E4", 1),
        Methods.createNote("D4", 2),
        Methods.createNote("G3", 2),

        Methods.createNote("C4", 2),
        Methods.createNote("E4", 1),
        Methods.createNote("C4", 1),
        Methods.createNote("B3", 2),
        Methods.createNote("E3", 2),
        
        Methods.createNote("A3", 2),
        Methods.createNote("G3", 1),
        Methods.createNote("F3", 1),
        Methods.createNote("G3", 2),
        Methods.createNote("C3", 2),

        Methods.createNote("A3", 1),
        Methods.createNote("B3", 1),
        Methods.createNote("C4", 1),
        Methods.createNote("E4", 1),
        Methods.createNote("D4", 2),
        Methods.createNote("C4", 1),
        Methods.createNote("D4", 1),

        Methods.createNote("E4", 2),
        Methods.createNote("G4", 1),
        Methods.createNote("E4", 1),
        Methods.createNote("D4", 2),
        Methods.createNote("G4", 2),

        Methods.createNote("A4", 1),
        Methods.createNote("B4", 1),
        Methods.createNote("C5", 1),
        Methods.createNote("A4", 1),
        Methods.createNote("G4", 4),

        
        Methods.createNote("A4", 1),
        Methods.createNote("G4", 1),
        Methods.createNote("F4", 1),
        Methods.createNote("A4", 1),
        Methods.createNote("G4", 1),
        Methods.createNote("E4", 1),
        Methods.createNote("D4", 1),
        Methods.createNote("C4", 1),

        Methods.createNote("D4", 2),
        Methods.createNote("D4", 1),
        Methods.createNote("E4", 1),
        Methods.createNote("C4", 4),
    ]]

    #############################################################
    # tune                                                      #
    #############################################################
    acc  = Methods.tuneNoteListSet(acc, Methods.distance("A3", "E3"))
    main = Methods.tuneNoteListSet(main, Methods.distance("A3", "E3"))

    #############################################################
    # compiled                                                  #
    #############################################################
    acc_compiled  = Compile.compileNoteListSet(acc , 0.4, TimbreSgn, 44100, 0.2)
    main_compiled = Compile.compileNoteListSet(main, 0.4, TimbreSgn, 44100, 0.2)

    music = acc_compiled + main_compiled
    Compile.dumpWAV(music, "./WAV/test008.wav")

###############################################################
# test009                                                     #
###############################################################
def test009():
    main = [[
        Methods.createNote("C4", 0.2),
        Methods.createNote("E4", 0.2),
        Methods.createNote("G4", 0.2),
        Methods.createNote("C5", 0.2),
        Methods.createNote("NULL", 0.2),
    ]]

    main_compiled = Compile.compileNoteListSet(main, 0.4, TimbreSgn, 44100, 0.2)
    music = main_compiled
    Compile.dumpWAV(music, "./WAV/test009-C.wav")

###############################################################
# test010                                                     #
###############################################################
def test010():
    main = [[
        Methods.createNote("C5", 0.2),
        Methods.createNote("G4", 0.2),
        Methods.createNote("E4", 0.2),
        Methods.createNote("C4", 0.2),
        Methods.createNote("NULL", 0.2),
    ]]

    main_compiled = Compile.compileNoteListSet(main, 0.4, TimbreSgn, 44100, 0.2)
    music = main_compiled
    Compile.dumpWAV(music, "./WAV/test010-C-down.wav")

###############################################################
# test011                                                     #
###############################################################
def test011():
    sub = [[
        Methods.createNote("F3", 1),
        Methods.createNote("E3", 1),
        Methods.createNote("D#3", 1),
        Methods.createNote("D3", 4),
    ]]
    main = [[
        Methods.createNote("B3", 1),
        Methods.createNote("A#3", 1),
        Methods.createNote("A3", 1),
        Methods.createNote("G#3", 4),
    ]]

    sub_compiled  = Compile.compileNoteListSet(sub, 0.4, TimbreSgn, 44100, 0.2)
    main_compiled = Compile.compileNoteListSet(main, 0.4, TimbreSgn, 44100, 0.2)
    music = sub_compiled + main_compiled
    Compile.dumpWAV(music, "./WAV/test011.wav")

###############################################################
# test012                                                     #
###############################################################
def test012():
    sub = [[
        Methods.createNote("A2", 16),
        Methods.createNote("G2", 16),
        Methods.createNote("F2", 16),
        Methods.createNote("E2", 16),
    ],[
        Methods.createNote("E2", 16),
        Methods.createNote("D2", 16),
        Methods.createNote("C2", 16),
        Methods.createNote("B2", 16),
    ]]
    main = [[
        Methods.createNote("A3", 2),
        Methods.createNote("A3", 2),
        Methods.createNote("G3", 2),
        Methods.createNote("A3", 2),
        Methods.createNote("A3", 1),
        Methods.createNote("G3", 1),
        Methods.createNote("A3", 2),
        Methods.createNote("C4", 2),
        Methods.createNote("D4", 2),

        Methods.createNote("A3", 2),
        Methods.createNote("A3", 2),
        Methods.createNote("G3", 2),
        Methods.createNote("A3", 2),
        Methods.createNote("A3", 1),
        Methods.createNote("G3", 1),
        Methods.createNote("A3", 2),
        Methods.createNote("G3", 2),
        Methods.createNote("E3", 2),

        Methods.createNote("A3", 2),
        Methods.createNote("A3", 2),
        Methods.createNote("G3", 2),
        Methods.createNote("A3", 2),
        Methods.createNote("A3", 1),
        Methods.createNote("G3", 1),
        Methods.createNote("A3", 2),
        Methods.createNote("C4", 2),
        Methods.createNote("D4", 2),

        Methods.createNote("E4", 4),
        Methods.createNote("G4", 2),
        Methods.createNote("D4", 2),
        Methods.createNote("E4", 8),
    ]]

    #############################################################
    # tune                                                      #
    #############################################################
    sub  = Methods.tuneNoteListSet(sub, Methods.distance("A3", "E3"))
    main = Methods.tuneNoteListSet(main, Methods.distance("A3", "E3"))

    sub_compiled  = Compile.compileNoteListSet(sub, 0.1, TimbreSgn, 44100, 0.2)
    main_compiled = Compile.compileNoteListSet(main, 0.1, TimbreSgn, 44100, 0.2)
    music = sub_compiled + main_compiled
    Compile.dumpWAV(music, "./WAV/test012.wav")

###############################################################
# test013                                                     #
###############################################################
def test013():
    main = [[
        Methods.createNote("D4", 0.2),
        Methods.createNote("F#4", 0.2),
        Methods.createNote("A4", 0.2),
        Methods.createNote("D5", 0.2),
        Methods.createNote("NULL", 0.2),
    ]]

    main_compiled = Compile.compileNoteListSet(main, 0.4, TimbreSgn, 44100, 0.2)
    music = main_compiled
    Compile.dumpWAV(music, "./WAV/test013-D.wav")

###############################################################
# test014                                                     #
###############################################################
def test014():
    main = [[
        Methods.createNote("E4", 0.2),
        Methods.createNote("G#4", 0.2),
        Methods.createNote("B4", 0.2),
        Methods.createNote("E5", 0.2),
        Methods.createNote("NULL", 0.2),
    ]]

    main_compiled = Compile.compileNoteListSet(main, 0.4, TimbreSgn, 44100, 0.2)
    music = main_compiled
    Compile.dumpWAV(music, "./WAV/test014-E.wav")

###############################################################
# test015                                                     #
###############################################################
def test015():
    main = [[
        Methods.createNote("F4", 0.2),
        Methods.createNote("A4", 0.2),
        Methods.createNote("C5", 0.2),
        Methods.createNote("F5", 0.2),
        Methods.createNote("NULL", 0.2),
    ]]

    main_compiled = Compile.compileNoteListSet(main, 0.4, TimbreSgn, 44100, 0.2)
    music = main_compiled
    Compile.dumpWAV(music, "./WAV/test015-F.wav")

###############################################################
# test016                                                     #
###############################################################
def test016():
    acc = [[
        Methods.createNote("A3", 0.4),
        Methods.createNote("C4", 0.4),
        Methods.createNote("F4", 0.4),
        Methods.createNote("B3", 0.4),
        Methods.createNote("D4", 0.4),
        Methods.createNote("G4", 0.4),
        Methods.createNote("C4", 0.4),
        Methods.createNote("E4", 0.4),
        Methods.createNote("G4", 0.4),
        Methods.createNote("C4", 0.4),
        Methods.createNote("NULL", 0.2),
    ]]
    main = [[
        Methods.createNote("F4", 0.4),
        Methods.createNote("A4", 0.4),
        Methods.createNote("C5", 0.4),
        Methods.createNote("G4", 0.4),
        Methods.createNote("B4", 0.4),
        Methods.createNote("D5", 0.4),
        Methods.createNote("C5", 1.6),
        Methods.createNote("NULL", 0.2),
    ]]

    acc_compiled = Compile.compileNoteListSet(acc, 0.5, TimbreSgn, 44100, 0.15)
    main_compiled = Compile.compileNoteListSet(main, 0.5, TimbreSgn, 44100, 0.2)
    length = min(len(main_compiled), len(acc_compiled))
    music = main_compiled[:length] + acc_compiled[:length]
    Compile.dumpWAV(music, "./WAV/test016.wav")

if __name__ == "__main__":
    test016()