from datetime import datetime
from portfolio import Portfolio
from data_manager import data_manager
from strategy import TradingStrategy

start = datetime(2013, 1, 1)
end = datetime(2017, 2, 28)

feed = data_manager('SPY',start, end)
stock_data = feed.get_close('SPY')

#Create strategy and signals
myStrategy = TradingStrategy(stock_data)
signals = myStrategy.signals

# Create a portfolio of SPY with $10,000 initial capital
# This will also test the porfolio performance based on the signals we 
# created with the trading strategy
portfolio = Portfolio('SPY',stock_data, signals, 10000.0)

# Print performance
print("Return: " + str(portfolio.roi))
print("My sharpe ratio: " + str(portfolio.sharpe_ratio))

print("Base Return: " + str(portfolio.baseline_roi))
print("Base sharpe ratio: " + str(portfolio.baseline_sharpe))


#Plotter functions to follow. Have raw code in notebook