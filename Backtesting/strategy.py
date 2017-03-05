import talib as ta
import numpy as np
import pandas as pd

class TradingStrategy:
    
    def __init__(self, data):
        self.data = np.array(data)
        self.bars = data.index
        self.short = 20
        self.long = 50
        self.signals = self._generate_signals()
        
        
    def _generate_signals(self):
        '''This is truly the most important part.
        This piece will change everytime we want 
        to test a different strategy
        '''
        # Create DataFrame and initialise signal series to zero
        signals = pd.DataFrame(index=self.bars)
        signals['signal'] = 0
        
        # Create the short/long simple moving averages
        signals['short_mavg'] = ta.SMA(self.data, self.short)
        signals['long_mavg'] = ta.SMA(self.data, self.long)
        
        # When the short SMA exceeds the long SMA, set the ‘signals’ Series to 1 (else 0)
        signals['signal'][self.short:] = \
        np.where(signals['short_mavg'][self.short:] > \
        signals['long_mavg'][self.short:], 1, 0)
        
        # Take the difference of the signals in order to generate actual trading orders
        signals['order'] = signals['signal'].diff()
        return signals