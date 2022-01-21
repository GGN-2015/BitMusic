# -*- encoding: utf-8 -*-
"""
    constant
    储存各种常量，保证常量的统一性
"""

DEFAULT_SPEED   = 120    # 默认速度
DEFAULT_TONE    = "Sine" # 默认音色
DEFAULT_VOLUME  = 0.02   # 默认音量
MAX_VOLUME      = 1.0    # 最大音量
MIN_VOLUME      = 0.0    # 最小音量
NO_LENGTH       = -1     # 用来表示当前音乐没有长度的标记

def getBeatLengthBySpeed(speed): # 根据当前的速度，计算每一拍的长度
    return 60 / speed