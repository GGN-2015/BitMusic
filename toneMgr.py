# -*- encoding: utf-8 -*-
"""
    toneMgr
    音色管理器，根据音色名获取 numpy.ndarray 波形数据。
"""

import numpy as np

def sgn(arr): # 序列上的 sgn 函数
    newArr = arr.copy()
    for i in range(len(newArr)):
        if newArr[i] > 0:
            newArr[i] = 2 ** -0.5
        elif newArr[i] < 0:
            newArr[i] = - 2 ** -0.5
    return newArr

def floatMod(arr, val): # 浮点数模运算
    if val == 0:
        return arr * 0
    newArr = arr.copy()
    for i in range(len(newArr)):
        newArr[i] = newArr[i] - int(newArr[i] / val) * val
    return newArr

# ---------- 在此处拓展实现音色管理器 ----------

MuteNoteTransform = lambda freq, times: times * 0
SineTransform     = lambda freq, times: np.sin(2 * np.pi * freq * times)
SquareTransform   = lambda freq, times: sgn(SineTransform(freq, times)) / 2
ZTransform        = lambda freq, times: (floatMod(times, (1.0 / freq)) - ((1.0 / freq) / 2)) / ((1.0 / freq) / 2) / 2

getTransformByName = {
    "MuteNote": MuteNoteTransform,
    "Sine"    : SineTransform,
    "Square"  : SquareTransform,
    "Z"       : ZTransform
}

def getToneWAV(toneName, freq, arrLength, simplingRate):      # 根据音色生成对应的波形
    times = np.linspace(0, arrLength/simplingRate, arrLength) # 最开始将数组初始化成从 0 开始的浮点数等差数列，数值为音符演奏开始到当前取样点的秒数                                                     
    if getTransformByName.get(toneName) != None:
        return getTransformByName[toneName](freq, times)      # MuteNote 表示没有声音的音符，频率无所谓
    else:
        sound = SineTransform(freq, times)                    # 找不到对应的音色，默认返回正弦波
        return sound
