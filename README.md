# Algos to Try

- Exponential Moving Average
    - Moving averages might be limited, according to a friend. 
- Range breakout
    - Not sure if we have enough data for it. Could be cool though.
- Mean Reversion Algorithm
- Pairs Trading
    - Could be a safe strategy as it was outlined in Seminar 2.
    - https://github.com/KidQuant/Pairs-Trading-With-Python/blob/master/PairsTrading.ipynb

# Algos We Have

## 28-06-default-algo

```
mean(PL): -18.2
return: -0.00095
StdDev(PL): 276.21
annSharpe(PL): -1.04 
totDvolume: 4796462 
Score: -45.77
```

## 30-06-padded-sma-v1.py
- Uses a Padded Simple Moving Average.
- Beats the default! 
- Needs tweaking with amount to buy/sell.
- Definitely a basic algo, but this current implementation can definitely be optimised to perform better.

```
mean(PL): -0.3
return: -0.00101
StdDev(PL): 1.81
annSharpe(PL): -2.37 
totDvolume: 67317 
Score: -0.45
```

Some ideas:
- Buy/Sell only when the percentage absolute difference of the SMA and Current Price is greater than a specific threshold (eg. 5%).
- Different window sizes depending on how volatile a stock is.
- Different Buy/Sell amounts depending on how volatile a stock is.

Future:
- Train a model with machine learning and use that