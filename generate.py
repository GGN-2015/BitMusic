# -*- encoding: utf-8 -*-
"""
    generate
    由用户自己编写的生成器程序
"""

import linkCompiled
import makeFlag
import noteOperate
import compiledToWAV

if __name__ == "__main__":
    ptC  = makeFlag.getPatternByName("SimpleMajor8-6.pattern.json")
    ptCm = makeFlag.getPatternByName("SimpleMinor8-6.pattern.json")
    ptF  = noteOperate.getMovedPattern( ptC, +5)
    ptG  = noteOperate.getMovedPattern( ptC, +7)
    ptAm = noteOperate.getMovedPattern(ptCm, +9)

    makeFlag.initFlagJson()
    makeFlag.addPattern(ptC)
    makeFlag.addPattern(ptG)
    makeFlag.addPattern(ptAm)
    makeFlag.addPattern(ptF)
    makeFlag.quickCompile(compiledFileName="./compiled/bg.tmp.compiled.json", WAVFileName=None) # 制作 BG

    ptC  = makeFlag.getPatternByName("UpAndDownMajor8-6.pattern.json")
    ptCm = makeFlag.getPatternByName("UpAndDownMinor8-6.pattern.json")
    ptF  = noteOperate.getMovedPattern( ptC, +5)
    ptG  = noteOperate.getMovedPattern( ptC, +7)
    ptAm = noteOperate.getMovedPattern(ptCm, +9)

    makeFlag.initFlagJson()
    makeFlag.setSpeed(240) # 二倍速
    makeFlag.addPattern(ptC  * 2)
    makeFlag.addPattern(ptG  * 2)
    makeFlag.addPattern(ptAm * 2)
    makeFlag.addPattern(ptF  * 2)
    makeFlag.quickCompile(compiledFileName="./compiled/fg.tmp.compiled.json", WAVFileName=None) # 制作 FG
    
    linkCompiled.link(
        [
            "./compiled/fg.tmp.compiled.json",
            "./compiled/bg.tmp.compiled.json"
        ],
        "./compiled/newMusic.compiled.json"
    ) # 链接
    compiledToWAV.compile() # 编译成 wav 文件
    