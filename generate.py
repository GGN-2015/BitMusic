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
    ptC  = makeFlag.getPatternByName("SimpleLyricMajor4-4.pattern.json")
    ptCm = makeFlag.getPatternByName("SimpleLyricMinor4-4.pattern.json")
    ptC  = noteOperate.getMovedPattern(ptC,  -12)
    ptCm = noteOperate.getMovedPattern(ptCm, -12) # 降低 8 度
    ptF  = noteOperate.getMovedPattern( ptC, +5)
    ptG  = noteOperate.getMovedPattern( ptC, +7)
    ptAm = noteOperate.getMovedPattern(ptCm, +9)

    makeFlag.initFlagJson()
    makeFlag.setTone("Square")
    # makeFlag.setSpeed(240)
    makeFlag.addPattern(ptC )
    makeFlag.addPattern(ptG )
    makeFlag.addPattern(ptAm)
    makeFlag.addPattern(ptF )
    makeFlag.quickCompile(compiledFileName="./compiled/bg.tmp.compiled.json", WAVFileName=None) # 制作 BG 1

    ptC  = makeFlag.getSegmentByName("DairyPart01C.pattern.json")
    ptF  = makeFlag.getSegmentByName("DairyPart01F.pattern.json")
    ptG  = makeFlag.getSegmentByName("DairyPart01G.pattern.json")
    ptAm = makeFlag.getSegmentByName("DairyPart01Am.pattern.json")

    makeFlag.initFlagJson()
    makeFlag.setTone("Z")
    makeFlag.addPattern(ptC )
    makeFlag.addPattern(ptG )
    makeFlag.addPattern(ptAm)
    makeFlag.addPattern(ptF )
    makeFlag.quickCompile(compiledFileName="./compiled/fg.tmp.compiled.json", WAVFileName=None) # 制作 FG 1

    tmpCompiledFile1 = linkCompiled.merge(
        [
            "./compiled/fg.tmp.compiled.json", 
            "./compiled/bg.tmp.compiled.json"
        ],
        # fileNameTo = None
        fileNameTo = "./compiled/Dairy01.compiled.json"
    ) # 叠加

    ptC  = makeFlag.getPatternByName("T1213121Major4-4.pattern.json")
    ptCm = makeFlag.getPatternByName("T1213121Minor4-4.pattern.json")
    ptC  = noteOperate.getMovedPattern(ptC,  -12)
    ptCm = noteOperate.getMovedPattern(ptCm, -12) # 降低八度
    ptF  = noteOperate.getMovedPattern(ptC,  +5 )
    ptG  = noteOperate.getMovedPattern(ptC,  +7 )
    ptAm = noteOperate.getMovedPattern(ptCm, +9 )

    makeFlag.initFlagJson()
    makeFlag.setTone("Square")
    # makeFlag.setSpeed(240)
    makeFlag.addPattern(ptC )
    makeFlag.addPattern(ptG )
    makeFlag.addPattern(ptAm)
    makeFlag.addPattern(ptF )
    makeFlag.quickCompile(compiledFileName="./compiled/bg.tmp.compiled.json", WAVFileName=None) # 制作 BG 2

    ptC  = makeFlag.getSegmentByName("DairyPart02C.pattern.json")
    ptF  = makeFlag.getSegmentByName("DairyPart02F.pattern.json")
    ptG  = makeFlag.getSegmentByName("DairyPart02G.pattern.json")
    ptAm = makeFlag.getSegmentByName("DairyPart02Am.pattern.json")

    makeFlag.initFlagJson()
    makeFlag.setTone("Z")
    makeFlag.addPattern(ptC )
    makeFlag.addPattern(ptG )
    makeFlag.addPattern(ptAm)
    makeFlag.addPattern(ptF )
    makeFlag.quickCompile(compiledFileName="./compiled/fg.tmp.compiled.json", WAVFileName=None) # 制作 FG 2

    tmpCompiledFile2 = linkCompiled.merge(
        [
            "./compiled/fg.tmp.compiled.json", 
            "./compiled/bg.tmp.compiled.json"
        ],
        # fileNameTo = None
        fileNameTo = "./compiled/Dairy02.compiled.json"
    ) # 叠加

    tmpCompiledFile = linkCompiled.connect(
        [
            "./compiled/Dairy01.compiled.json", 
            "./compiled/Dairy01.compiled.json", 
            "./compiled/Dairy02.compiled.json",
            "./compiled/Dairy02.compiled.json",
        ], None
    ) # 重复两遍

    compiledToWAV.compile(tmpCompiledFile) # 编译得到单声道音乐
