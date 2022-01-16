# -*- encoding: utf-8 -*-
"""
    makeFlag
    生成 .flag.json 文件的相关算法
"""

import json

flagJson = {"data": [], "length": -1} # length = -1 表示自动推断乐曲持续时间

def initFlagJson(length = -1): # 设置歌曲的长度
    flagJson["length"] = length
    flagJson["data"]   = []

def getPatternByName(patternName): # 根据 patternName 得到 pattern
    with open("./patterns/" + patternName, "r") as f:
        pattern = json.load(f)
    return pattern

def setSpeed(newSpeed: int): # 设置新的速度
    flagJson["data"].append({
        "type": "setSpeed",
        "data": newSpeed
    })

def setVolume(newVolume: float): # 设置新的音量
    flagJson["data"].append({
        "type": "setVolume",
        "data": newVolume
    })

def setTone(newTone: str): # 设置新的音色
    flagJson["data"].append({
        "type": "setTone",
        "data": newTone
    })

def addNote(note: list): # 添加一个音符
    names   = note[0]
    beatCnt = note[1]
    flagJson["data"].append({
            "type": "note",
            "data": {
                "names"  : names,
                "beatCnt": beatCnt
            }
        }
    )

def addPattern(pattern): # pattern 其实就是 note 序列
    for note in pattern:
        addNote(note)

def saveToFile(fileName = "./flags/newMusic.flag.json"): # 保存到 .flag.json 文件
    with open(fileName, "w") as fout:
        json.dump(flagJson, fout)

def quickCompile(): # 一键编译到 WAV 文件，仅用于调试
    print("[makeFlag] quickCompile: (deprecated) only use this function when debugging.")
    import flagToCompiled
    import compiledToWAV
    saveToFile()             # 生成 .flag.json     标记文件
    flagToCompiled.compile() # 生成 .compiled.json 音轨文件
    compiledToWAV.compile()  # 生成 .was           波形文件
