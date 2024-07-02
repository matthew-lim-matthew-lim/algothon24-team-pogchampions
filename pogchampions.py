
import numpy as np

##### TODO #########################################
### RENAME THIS FILE TO YOUR TEAM NAME #############
### IMPLEMENT 'getMyPosition' FUNCTION #############
### TO RUN, RUN 'eval.py' ##########################

nInst = 50
currentPos = np.zeros(nInst)


# Padded Simple Moving Average
def sma_padded(data, window):
    # We pad (window - 1) and (0) (meaning that the SMA extends over the entire
    # data set)
    padded_data = np.pad(data, (window-1, 0), mode='edge')
    weights = np.repeat(1.0, window) / window
    smas = np.convolve(padded_data, weights, 'valid')
    return smas

def getMyPosition(prcSoFar):
    global currentPos
    (nins, nt) = prcSoFar.shape
    # If the window is too small, don't make a play (don't have enough data to know).
    # I mean, technically it works now we use the padded SMA, but it's not a good idea
    # since the SMA will be very inaccurate with so little data.
    if (nt < 20):
        return np.zeros(nins)
    
    # The SMA from sma_padded is 1 dimension but a dataframe is 2 dimensions
    # Also, it needs to be a numpy array (using np.array), otherwise 
    # the rpos calculation will not work
    sma_df = np.array([sma_padded(prcSoFar[i], 20) for i in range(nins)])

    # We use the last value of the SMA to determine our position
    sma_last_pos = sma_df[:, -1]

    # If the actual is SMA is larger than Current Price, we buy
    rpos = np.array([int(x) for x in 1000 * (abs(sma_last_pos) - abs(prcSoFar[:, -1]))/(abs(sma_last_pos))])
    currentPos = np.array([int(x) for x in currentPos + rpos])
    # currentPos = np.array([int(x) for x in rpos])
    print(sma_last_pos[:5])
    print(prcSoFar[:, -1][:5])
    print(currentPos[:5])
    return currentPos
