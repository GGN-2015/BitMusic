# -*- encoding: utf-8 -*-
"""
    generate
    由用户自己编写的生成器程序
"""

import makeFlag
import noteOperate

if __name__ == "__main__":
    ptC = makeFlag.getPatternByName("SimpleMajor8-6.pattern.json")
    ptF = noteOperate.getMovedPattern(ptC, +5)

    makeFlag.addPattern(ptC)
    makeFlag.addPattern(ptF)

    makeFlag.setSpeed(180)  # 开启 1.5 倍速
    makeFlag.addPattern(ptC)
    makeFlag.setVolume(0.5) # 声音增大
    makeFlag.addPattern(ptF)

    makeFlag.quickCompile() # 快速编译
