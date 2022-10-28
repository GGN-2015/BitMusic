# -*- encoding: utf-8 -*-
"""
    noteOperate
    音名调整相关的算法。
"""

import json

with open("./NoteFreq.json", "r") as fin: # 读取 音名 => 频率 映射
    NoteFreq = json.load(fin)

AllNoteNames = []
for name in NoteFreq:
    AllNoteNames.append(name) # 所有音符构成的名字序列

def getIdByNoteName(name):
    for i in range(len(AllNoteNames)):
        if AllNoteNames[i] == name:
            return i
    return -1

def getNoteNameById(noteId):
    if 0 <= noteId and noteId < len(AllNoteNames):
        return AllNoteNames[noteId]
    else:
        return "NN" # NN 表示一个空拍

def getMovedName(name, move): # 升或者降低若干个音
    return getNoteNameById(getIdByNoteName(name) + move)

def listDeepCopy(val): # 对嵌套的 list/dict 进行递归的完全深拷贝
    if type(val) == list:
        return [listDeepCopy(x) for x in val]
    elif type(val) == dict:
        newDict = {}
        for x in val:
            newDict[x] = listDeepCopy(val[x])
        return newDict
    else:
        return val

def getMovedPattern(pattern, move): # 升高或降低一个 pattern
    newPattern = listDeepCopy(pattern)  # 必须在拷贝后得到的 list 进行操作
    for i in range(len(pattern)):
        newNameList = []
        for name in pattern[i][0]:
            newNameList.append(getMovedName(name, move))
        newPattern[i][0] = newNameList
    return newPattern
