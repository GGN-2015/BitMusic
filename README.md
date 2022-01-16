# BitMusic 正弦波音乐合成器

作者: GGN_2015

有一说一，做的烂得一批，而且功能也很少，效率有差，不过可拓展性应该还是比较可观的。希望有大佬愿意帮忙做拓展。

## 工具程序

| 程序名称                       | 程序功能                                                     |
| ------------------------------ | ------------------------------------------------------------ |
| compiledToWAV.py               | 将 .compiled.json 编译成 .wav 音频文件。                     |
| flagToCompiled.py              | 将 .flag.json 编译成 .compiled.json 文件。                   |
| - generate.py (unfinished)     | 由用户自己编写的生成器程序。                                 |
| - linkCompiled.py (unfinished) | 将两个 .compiled.json 音轨直接叠加，得到新的 .compiled.json。 |
| noteOperate.py                 | pattern 中音高调整相关算法，实现和弦复用。                   |
| makeFlag.py                    | 生成 .flag.json 文件的相关算法。                             |
| toneMgr.py                     | 音色管理器，根据音色名获取 numpy.ndarray 波形数据。          |

## 文件类型

| 文件类型       | 备注                                                         |
| -------------- | ------------------------------------------------------------ |
| .compiled.json | 编译得到的 “频率-时间” 乐谱文件，可由 compiledToWAV.py 编译成 .wav 音频文件。 |
| .flag.json     | 带变速标志乐谱，可由 flagToCompiled.py 编译成 .compiled.json。 |

### .compiled.json

文件本身包含一个 dict，至少包含 "length"、"data" 数据域。"length" 域储存音乐的总时间（浮点数，单位为秒，没演奏完的部分会被截断），"data" 域储存编译得到的音符 list。每个音符用一个 dict 表示，至少包含 "freq"、"begin"、"span"、"volume"、"tone"，分别表示音符的频率、开始时刻、持续时间以及响度。这里的响度是一个介于 0 ~ 1 之间的实数，如果亲自动手编写 .compiled.json，务必保证每一时刻，同时发声的每个音符的响度之和严格小于 1。"tone" 域为一个字符串，指出音符的音色，需要在**音色拓展管理器**(toneMgr.py)上进行查找，找到该音色对应的波形生成算法，找不到响应音色或没有**音色拓展管理器**默认使用正弦波替代。

### .flag.json

文件本身包含一个 dict，至少包含 "length"、"data" 数据域。**如果没有 "length" 数据域**，编译成 .compiled.json 前会进行乐曲长度自动推断。"data" 数据域是一个 list，里面按照时间顺序排列了所有“标志”。一个标志可能是一个音符，也肯能是一个变速记号，也可能是一个响度记号。如果最初不指出音符的响度和速度，默认响度为 0.1，默认速度为 120 bpm，即每拍 0.5s。“标志”是一个 dict，包含 "type"、"data" 两个数据域。type 域的值可能为 "setSpeed" / "setVolume" / "setTone" / "note"，表示这个“标志”的类别。为 "note" 时，"data" 域 储存一个 dict 包含 "names", "beatCnt"。 "names" 域 是一个 list of str, 里面存储着一个或多个音名(如 "C3" 或 "A#4")，"beatCnt" 域是一个浮点数，表示这个音符持续的拍数。

### .note.json

一个音符，形如 ``[[str, ...], float]`` 其中 str 是一个音符对应的音名， float 是这个音符持续的拍数。

### .pattern.json

与音色、速度均无关的纯旋律，存储在 ``./patterns`` 目录中。文件本身是一个 list, list 中每个元素形如 ``[[str, ...], float]`` 其中 str 是一个音符对应的音名， float 是这个音符持续的拍数。pattern.json 用来存储常用的伴奏模式，一般要求该旋律适应 C major/C minor 二者之一。



