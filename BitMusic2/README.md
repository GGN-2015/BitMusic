# BitMusic2

基于 `python` 和 `ffmpeg` 的正弦波音乐合成器。由于老版本的 `BitMusic` 功能繁琐不便于使用，新版本对功能进行了简化。

## 1. 结构定义

BitMusic2 中定义了如下几种结构用于音乐的描述与生成，所有结构均以大驼峰命名法命名。

### 1.1 乐谱的表示

- 音符 `Note`：{'Id', 'Length'}，'Id' 为一个整数，表示音名编号；'Length' 表示拍数；
- 音符列 `NoteList`：音符构成的序列；音符列中 'Id' = None 的音符表示空拍；
- 音符列集 `NoteListSet`：音符列构成的序列，每个音符列持续的拍数相同，用于描述一段音乐或和弦；
- 片段 `Segment`：{'NoteListSet', 'Timbre', 'Amplitude', 'Speed'}，NoteListSet是音符列集，Timbre为音色名，Amplitude为最大振幅，Speed为速度，表示一拍持续的秒数；

### 1.2 音色的表示

音色是振幅 $y$ 关于时间 $t$、频率 $f$、最大振幅 $a$ 的函数. 例如:
$$
y(t,f,a)=a\cdot\cos(2\pi f\cdot t)
$$

## 2.基本方法

使用音符列集构造和旋模板，使用平移方法获得和旋，使用音符列集链接构造音乐对应的音符列集，将片段导出为 WAV 文件。
