
######################
# Compile.py         #
# Author: GGN_2015   #
# Date  : 2022-07-20 #
######################


##############################################################
# COMPILER FOR SINE WAVE PROCESSING                          #
# INPUT A Segment and OUTPUT a WAV file                      #
##############################################################
import numpy as np


########################
# compileNoteListSet   #
# Speed       : second #
# SamplingRate: Hz     #
########################
import Methods
import SmoothTools

def compileNoteListSet(NoteListSet, Speed, Timbre, SamplingRate = 44100, MaxAmp = 0.2):
    WINDOW_LEN = round(SamplingRate * 0.05) # 0.05s window

    TotalLength   = Methods.getLengthOfNoteListSet(NoteListSet)
    TimeSpan      = TotalLength * Speed
    RailLength    = int(TimeSpan * SamplingRate)
    FullMusicRail = np.zeros(RailLength)
    SplitPoints   = np.zeros(RailLength) # Record The position of the SplitPoints
    for NoteList in NoteListSet:
        MusicRail = np.zeros(RailLength)
        PosNow = 0
        for Note in NoteList:
            Id        = Note['Id']
            ArrLength = int(Note['Length'] * Speed * SamplingRate)
            if Methods.getNoteNameById(Id) != "NULL":
                TimeRail  = Methods.getNpTimeList(ArrLength, SamplingRate)
                Freq      = Methods.getNoteFreqById(Id)
                NoteRail  = SmoothTools.SmoothEdge(Timbre.y(TimeRail, Freq, MaxAmp), WINDOW_LEN)
                maxPos    = -1
                for i in range(0, ArrLength): # FLOAT POINT ERROR
                    if PosNow + i < RailLength:
                        MusicRail[PosNow + i] = NoteRail[i]
                        maxPos                = PosNow + i
                SplitPoints[PosNow] = 1     # Need to modify at the beginning 
                if maxPos != -1: 
                    SplitPoints[maxPos] = 1 # Need to modify at the end
            PosNow += ArrLength
        FullMusicRail += MusicRail
    return FullMusicRail


###########################################################################
# dumpWAV(FullMusicRail: np.ndarray, WAVFileName = "a.wav", SamplingRate) #
#! SamplingRate must be same with MusicRail                               #
###########################################################################
import scipy.io.wavfile as wf
def dumpWAV(FullMusicRail: np.ndarray, WAVFileName = "a.wav", SamplingRate = 44100):
    FullMusicRail = np.array((FullMusicRail * (2 ** 15)), dtype = np.int16)
    wf.write(WAVFileName, SamplingRate, FullMusicRail)
