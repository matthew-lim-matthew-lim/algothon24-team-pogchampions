
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
    if (nt < 15):
        return np.zeros(nins)
    
    # The SMA from sma_padded is 1 dimension but a dataframe is 2 dimensions
    # Also, it needs to be a numpy array (using np.array), otherwise 
    # the rpos calculation will not work
    sma_df = np.array([sma_padded(prcSoFar[i], 15) for i in range(nins)])

    # We use the last value of the SMA to determine our position
    sma_last_pos = sma_df[:, -1]

    # Adjust the position sizing multiplier
    multiplier = 1500
    
    # Calculate momentum (rate of change) and scale positions accordingly
    momentum = 100 * (prcSoFar[:, -1] - prcSoFar[:, -2]) / prcSoFar[:, -2]
    if (nt < 15):
        momentum = np.ones(nins)
    print("Momentum: ", momentum[:5])
    rpos = np.array([int(multiplier * (sma_last_pos[i] - prcSoFar[i, -1]) / sma_last_pos[i] * momentum[i]) for i in range(nins)])
    
    # Smooth out position changes to avoid drastic fluctuations
    rpos = np.clip(rpos, -50, 50)
    currentPos = currentPos + rpos

    # currentPos = np.array([int(x) for x in rpos])
    print("SMA Last Pos: ", sma_last_pos[:5])
    print("Prev Real Pos: ", prcSoFar[:, -1][:5])
    print("New Pos: ", currentPos[:5])
    return currentPos
