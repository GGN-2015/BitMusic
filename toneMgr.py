# -*- encoding: utf-8 -*-
"""
    toneMgr
    音色管理器，根据音色名获取 numpy.ndarray 波形数据。
"""

import numpy as np

def getToneWAV(toneName, freq, arrLength, simplingRate):      # 根据音色生成对应的波形
    times = np.linspace(0, arrLength/simplingRate, arrLength) # 最开始将数组初始化成从 0 开始的浮点数等差数列，数值为音符演奏开始到当前取样点的秒数
                                                              # ---------- 在此处拓展实现音色管理器 ----------
    if toneName == "MuteNote":
        return np.zeros(arrLength)                            # MuteNote 表示没有声音的音符，频率无所谓
    else:
        sound = np.sin(2 * np.pi * freq * times)              # 找不到对应的音色，默认返回正弦波
        return sound
