
import numpy as np

##### TODO #########################################
### RENAME THIS FILE TO YOUR TEAM NAME #############
### IMPLEMENT 'getMyPosition' FUNCTION #############
### TO RUN, RUN 'eval.py' ##########################

nInst = 50
currentPos = np.zeros(nInst)


# Simple Moving Average
def sma(data, window):
    # weights array is an array of '1/window'. Multiplying it with the data array will give us the 
    # moving average since '1/window * data' describes the average of each datapoint
    weights = np.repeat(1.0, window)/window
    smas = np.convolve(data, weights, 'valid')
    return smas

def getMyPosition(prcSoFar):
    global currentPos
    (nins, nt) = prcSoFar.shape
    # If the window is too small, don't make a play (don't have enough data to know)
    if (nt < 20):
        return np.zeros(nins)
    lastRet = np.log(prcSoFar[:, -1] / prcSoFar[:, -2])
    lNorm = np.sqrt(lastRet.dot(lastRet))
    lastRet /= lNorm
    rpos = np.array([int(x) for x in 5000 * lastRet / prcSoFar[:, -1]])
    currentPos = np.array([int(x) for x in currentPos+rpos])
    return currentPos
