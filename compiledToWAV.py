# -*- encoding: utf-8 -*-
"""
    compiledToWAV
    将 .compiled.json 文件 编译成可以播放的 .wav 文件
"""

import json
import numpy as np
import scipy.io.wavfile as wf

import toneMgr # 音色管理器 (可能需要进行拓展)

def compile(fileName = './compiled/newMusic.compiled.json', WAVFileName = './wav/newMusic.wav', simplingRate = 44100): 
                                                   # 编译一个 .compiled.json 文件
    with open(fileName, "r") as fin:               # 读取 .compiled.json 文件
        compiledJson = json.load(fin)
    musicLength = compiledJson["length"]           # 乐曲持续的秒数
    musicData   = compiledJson["data"]             # 乐曲的所有音符数据
    arrayLength = int(simplingRate * musicLength)  # 临时储存振幅的数组的总长度
    music       = np.zeros(arrayLength)            # 临时储存振幅的数组
    for note in musicData:        # 枚举每一个音符
        freq     = note["freq"]   # 音符频率
        begin    = note["begin"]  # 音符起始秒数
        span     = note["span"]   # 音符持续秒数
        volumn   = note["volume"] # 音符振幅 0 ~ 1 之间的实数
        tone     = note["tone"]   # 音色名称
        arrBegin = int(begin * simplingRate)          # 数组中的起始下标
        arrEnd   = int((begin + span) * simplingRate) # 数组中的结束位置下标
        if arrBegin < arrayLength and span > 0:       # 音符仍在歌曲时间范围内
            arrEnd   = min(arrEnd, arrayLength)       # 音符在数组中对应的区间是 [arrBegin, arrEnd)
                                                      # 获取对应的音色波形，默认响度为最大，反回值类型为 np.ndarray
            noteWav  = toneMgr.getToneWAV(tone, freq, arrEnd - arrBegin, simplingRate)
            if 0 <= volumn and volumn <= 1:
                noteWav *= volumn                     # 调整响度到实际响度
            for i in range(arrBegin, arrEnd):         # 将音色波形叠加到 music 振幅序列上
                music[i] += noteWav[i - arrBegin]
    maxValue = np.max(np.abs(music))                  # 最大振幅校验，如果最大振幅超过了 1, 说明可能有截断风险
    if maxValue > 1:                                  # 可能会导致频率失真
        print("[compiledToWAV] warning: maxValue = %f > 1." % maxValue)
    music *= (2 ** 15)
    music = music.astype(np.int16)
    wf.write(WAVFileName, simplingRate, music)        # 写入到 WAV 文件中
    print("[compiledToWAV] compile success, outputFile: %s" % WAVFileName)
