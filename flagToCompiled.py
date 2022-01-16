# -*- encoding: utf-8 -*-
"""
    flagToCompiled.py
    将 .flag.json 编译成 .compiled.json 文件
"""

import json

def compile(fileName = "./flags/newMusic.flag.json", compiledFileName = "./compiled/newMusic.compiled.json"):
    with open(fileName, "r") as fin:        # 读入 .flag.json 文件
        flagJson = json.load(fin)
    with open("NoteFreq.json", "r") as fin: # 读入 音名 => 频率 映射
        noteFreq = json.load(fin)
    speed    = 120                  # 默认速度 120 bpm
    volume   = 0.1                  # 默认音量 10%
    tone     = "Sine"               # 默认音色是正弦波
    if flagJson.get("length") != None:
        length = flagJson["length"] # 音乐总时间长度（单位：秒）
    else:
        length = -1                 # -1 表示需要推断
    data     = flagJson["data"]     # 音乐中的 flag 数据 list
    compiled = {"length": length, "data": []}
    timeNow = 0                     # 记录当前相对于乐曲首部的时刻，单位秒
    for flag in data:
        tp = flag["type"] # 类型信息
        dt = flag["data"] # 数据内容
        if tp == "setVolume":
            volume = max(min(dt, 1.0), 0.0)    # 保证最终数据在 0 ~ 1 范围之内
        elif tp == "setSpeed":
            speed = dt                         # 设置乐曲速度
        elif tp == "setTone":                  # 设置乐曲音色
            tone = dt
        elif tp == "note":
            names   = dt['names']              # 音符名称列表
            beatCnt = dt['beatCnt']            # 持续拍数
            for name in names:
                if noteFreq.get(name) != None: # 可以找到对应的音符（找不到视为空拍）
                    freq = noteFreq[name]
                    compiled["data"].append({
                        "freq"  : freq, 
                        "begin" : timeNow, 
                        "span"  : beatCnt * (60 / speed),
                        "volume": volume,
                        "tone"  : tone
                    })
            timeNow += beatCnt * (60 / speed)  # 经过了一个音符的时间
        else:
            print("[flagToCompiled] warning: flag type<%s> unknown." % tp)
    if length < 0:
        compiled["length"] = timeNow # 推断乐曲演奏时间长度
    with open(compiledFileName, "w") as fout:
        json.dump(compiled, fout)
    print("[flagToCompiled] finished compiled to %s." % compiledFileName) # 编译完成
