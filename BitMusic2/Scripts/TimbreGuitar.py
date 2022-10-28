
######################
# TimbreGuitar.py    #
# Author: GGN_2015   #
# Date  : 2022-07-21 #
######################


#######################################
# Y IS THE AMPLITUDE OF THE SINE WAVE #
#######################################
import numpy as np
def y(t: np.ndarray, f: float, a: float):
    SamplingRate = len(t) / (t[-1] + (t[-1] - t[-2]))
    f *= 4
    f *= (2 ** (1 / 12)) ** 8
    Period = int(2 * np.pi / f * SamplingRate)
    ans = np.random.rand(len(t))
    for i in range(min(Period, len(t))):
        ans[i] -= 0.5
    for i in range(Period, len(ans)):
        ans[i] = (ans[i - Period] + ans[i - Period + 1]) * 0.5
    return ans

