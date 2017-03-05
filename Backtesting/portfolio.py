import numpy as np
import pandas as pd

class Portfolio:
    
    def __init__(self, symbol, data, signals, initial_cash):
        self.initial_cash = initial_cash
        self.symbol = symbol
        self.data = data
        self.positions = self.generate_positions(signals)
        self.performance = self.backtest_portfolio()
        self.roi = self.calculate_roi()
        self.sharpe_ratio = self.calculate_sharpe_ratio()
        self.baseline_roi = self.calculate_baseline_roi()
        self.baseline_sharpe = self.calculate_baseline_sharpe()
    
    def generate_positions(self,signals):
        # Transact 100 shares on a signal
        positions = pd.DataFrame(index=signals.index).fillna(0.0)
        positions[self.symbol] = 100 * signals['signal'] 
        return positions
        
    def backtest_portfolio(self):
        portfolio = pd.DataFrame(index=self.positions.index)
        portfolio['position'] = self.positions
        pos_diff = portfolio['position'].diff()

        #Total (value) of the portfolio is a combination of holdings (position in stock) and cash
        portfolio['holdings'] = (self.positions[self.symbol] * self.data)
        portfolio['cash'] = self.initial_cash - (pos_diff*self.data).cumsum()
        portfolio['total'] = portfolio['cash'] + portfolio['holdings']
        
        portfolio['returns'] = portfolio['total'].pct_change()
        return portfolio
    
    def calculate_roi(self):
        roi = (self.performance.total[-1] - self.initial_cash)/self.initial_cash
        return roi
    
    def calculate_sharpe_ratio(self):
        sharpe = self.roi/self.performance.returns.std()
        return sharpe
    
    def calculate_baseline_roi(self):
        base_roi = (self.data[-1] - self.data[0])/self.data[0]
        return base_roi
    
    def calculate_baseline_sharpe(self):
        base_sharpe = base_returns = self.baseline_roi/self.data.pct_change().std()
        return base_sharpe