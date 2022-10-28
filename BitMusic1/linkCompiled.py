# -*- encoding: utf-8 -*-
"""
    linkCompiled
    将两个 .compiled.json 音轨直接叠加，得到新的 .compiled.json。
"""

import json
import noteOperate

def merge(
        fileNameList = ["./compiled/A.compiled.json", "./compiled/B.compiled.json"],
        fileNameTo = "./compiled/newLinked.compiled.json"
    ):                                            # 将 fileNameList 中提到的所有文件全部连接起来得到新的文件
    newCompiledJson = {"length": -1, "data": []}  # 新生成的数据文件
    for fileName in fileNameList:                 # 枚举所有文件名
        with open(fileName, "r") as fin:          # 从文件中读取 json
            fileJson = json.load(fin)
        newCompiledJson["length"] = max(newCompiledJson["length"], fileJson["length"])
        newCompiledJson["data"] += fileJson["data"]
    if fileNameTo != None:                        # fileNameTo = None 时不生成文件，而是返回一个 dict 作为计算结果
        with open(fileNameTo, "w") as fout:       # 将得到的数据输出到 fout
            json.dump(newCompiledJson, fout)
        print("[linkCompiled] merge success at %s" % fileNameTo)
    else:
        print("[linkCompiled] fileNameTo = None, return a DICT as result")
        return newCompiledJson

def connect(
        fileNameList = ["./compiled/A.compiled.json", "./compiled/B.compiled.json"],
        fileNameTo = "./compiled/newLinked.compiled.json"
    ):
    newCompiledJson = {"length": 0, "data": []}
    preLengthNow = 0
    for fileName in fileNameList:                 # 枚举所有文件名
        if type(fileName) == str:
            with open(fileName, "r") as fin:          # 从文件中读取 json
                fileJson = json.load(fin)
        else:
            fileJson = noteOperate.listDeepCopy(fileName)
        newCompiledJson["length"] += fileJson["length"] # 计算歌曲的总长度，总长度为每一部分的长度之和
        for item in fileJson["data"]:
            newItem = noteOperate.listDeepCopy(item)
            newItem["begin"] += preLengthNow            # 起始时间要偏移 preLengthNow 的时间
            newCompiledJson["data"].append(newItem)
        preLengthNow += fileJson["length"]
    if fileNameTo != None:
        with open(fileNameTo, "w") as fout:             # 将得到的数据输出到 fout
            json.dump(newCompiledJson, fout)
        print("[linkCompiled] connect success at %s" % fileNameTo)
    else:
        print("[linkCompiled] connect success, return a DICT as result")
        return newCompiledJson
