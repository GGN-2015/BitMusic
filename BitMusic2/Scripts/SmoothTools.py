##############
# 2022-10-28 #
# 平滑函数    #
##############

########################
# 对一段序列进行线性平滑 #
########################
def LinearSmooth(FullMusicRail, SplitPoints, WINDOW_HALF_LEN):
    for i in range(len(SplitPoints)):
        if SplitPoints[i] == 1 and i - WINDOW_HALF_LEN >= 0  and i + WINDOW_HALF_LEN < len(SplitPoints):
            leftPos    = i - WINDOW_HALF_LEN
            rightPos   = i + WINDOW_HALF_LEN
            leftValue  = FullMusicRail[leftPos]
            rightValue = FullMusicRail[rightPos]

            k = (rightValue - leftValue) / (rightPos - leftPos)
            for j in range(leftPos + 1, rightPos):
                FullMusicRail[j] = leftValue + k * (j - leftPos) # linear smooth


####################################################
# Sigmoid(0) = 0, Sigmoid(0.5)=0.5, Sigmoid(1) = 1 #
####################################################
import math
def Sigmoid(k):
    if k <= 0:
        return 0
    if k >= 1:
        return 1
    return 1.0 / (math.exp(-6*(k - 0.5)) + 1)


###########################################
# Smooth the front and the tail of a note #
###########################################
def SmoothEdge(ampList, winLen, SmoothMethod=lambda x:x):
    for i in range(0, winLen):
        ampList[i] = ampList[i] * SmoothMethod(i / winLen)
    for i in range(-winLen, 0):
        ampList[i] = ampList[i] * SmoothMethod((abs(i) - 1) / winLen)
    return ampList
