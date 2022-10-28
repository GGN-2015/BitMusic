
######################
# TimbreSine.py      #
# Author: GGN_2015   #
# Date  : 2022-07-20 #
######################


##############################################################
# THIS FILE CONTAINS METHODS FOR SINE WAVE PROCESSING        #
# YOU MAY USE THIS AS A TEMPLAE FOR YOUR OWN TIMBRE          #
##############################################################
import numpy as np
def sgn(t: np.ndarray):
    ans = np.zeros(t.shape)
    for i in range(len(t)):
        if t[i] > 0:
            ans[i] = 1
        elif t[i] < 0:
            ans[i] = -1
        else:
            ans[i] = 0
    return ans


#######################################
# Y IS THE AMPLITUDE OF THE SINE WAVE #
#######################################
def y(t: np.ndarray, f: float, a: float):
    base = np.exp(- 2 * t)
    voice = a * sgn(np.sin(2 * np.pi * f * t))
    return base * voice
