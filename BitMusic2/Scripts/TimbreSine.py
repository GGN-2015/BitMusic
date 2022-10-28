
######################
# TimbreSine.py      #
# Author: GGN_2015   #
# Date  : 2022-09-21 #
######################
import numpy as np


#######################################
# Y IS THE AMPLITUDE OF THE SINE WAVE #
#######################################
def y(t: np.ndarray, f: float, a: float):
    voice = a * np.sin(2 * np.pi * f * t)
    return voice
