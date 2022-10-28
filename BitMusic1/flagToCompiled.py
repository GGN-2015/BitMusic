# -*- encoding: utf-8 -*-
"""
    flagToCompiled.py
    将 .flag.json 编译成 .compiled.json 文件
"""

import json
import noteOperate
import constant

with open("NoteFreq.json", "r") as fin: # 读入 音名 => 频率 映射
    noteFreq = json.load(fin)

speed    = constant.DEFAULT_SPEED  # 默认速度 120 bpm
volume   = constant.DEFAULT_VOLUME # 默认音量 1%
tone     = constant.DEFAULT_TONE   # 默认音色是正弦波
timeNow  = 0                       # 记录当前相对于乐曲首部的时刻，单位秒
compiled = {"length": constant.NO_LENGTH, "data": []}

def setVolumeMethod(data):
    global volume
    volume = max(min(data, constant.MAX_VOLUME), constant.MIN_VOLUME)    # 保证最终数据在 0 ~ 1 范围之内

def setToneMethod(data):        # 设置音色
    global tone
    tone = data

def setSpeedMethod(data):       # 设置速度 bpm
    global speed
    speed = data

def addNoteMethod(dt):
    global timeNow
    names   = dt['names']              # 音符名称列表
    beatCnt = dt['beatCnt']            # 持续拍数
    for name in names:
        if noteFreq.get(name) != None: # 可以找到对应的音符（找不到视为空拍）
            freq = noteFreq[name]
            compiled["data"].append({
                "freq"  : freq, 
                "begin" : timeNow, 
                "span"  : beatCnt * constant.getBeatLengthBySpeed(speed),
                "volume": volume,
                "tone"  : tone
            })
    timeNow += beatCnt * constant.getBeatLengthBySpeed(speed)  # 经过了一个音符的时间

getMethodByType = {
    "setVolume": setVolumeMethod,
    "setTone"  : setToneMethod,
    "setSpeed" : setSpeedMethod,
    "note"     : addNoteMethod
}

def compile(fileNameOrDict = "./flags/newMusic.flag.json", compiledFileName = "./compiled/newMusic.compiled.json"):
    global timeNow
    timeNow = 0                                # 记录当前相对于乐曲首部的时刻，单位秒
    if type(fileNameOrDict) == str:            # 支持文件输入和变量输入两种模式
        with open(fileNameOrDict, "r") as fin: # 读入 .flag.json 文件
            flagJson = json.load(fin)
    else:
        flagJson = noteOperate.listDeepCopy(fileNameOrDict)
    if flagJson.get("length") != None:
        length = flagJson["length"] # 音乐总时间长度（单位：秒）
    else:
        length = -1                 # flag.json 中的 length = -1 表示乐曲长度需要推断
    global compiled
    compiled = {"length": length, "data": []}
    data     = flagJson["data"]     # 音乐中的 flag 数据 list
    for flag in data:
        tp = flag["type"]                # 类型信息
        dt = flag["data"]                # 数据内容
        method = getMethodByType.get(tp) # 根据 类型信息推断处理算法
        if method != None:
            method(dt)                   # 使用处理算法进行处理
        else:
            print("[flagToCompiled] warning: flag type<%s> unknown." % tp)
    if length < 0:
        compiled["length"] = timeNow     # 推断乐曲演奏时间长度
    if compiledFileName != None:
        with open(compiledFileName, "w") as fout:
            json.dump(compiled, fout)
        print("[flagToCompiled] finished compiled to %s." % compiledFileName) # 编译完成
    else:
        print("[flagToCompiled] finished compiled, return DICT as result.")   # 编译完成，返回计算结果
        return compiled
