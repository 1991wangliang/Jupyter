import pandas_datareader as pdr
import datetime

start = datetime.datetime(2006, 1, 1)
end = datetime.datetime(2021, 1, 1)
start_date_str = str(start.date())
end_date_str = str(end.date())

stocks = ['MMM', 'AXP', 'AAPL', 'BA', 'CAT', 'CVX', 'CSCO', 'KO', 'DIS', 'XOM', 'GE',
          'GS', 'HD', 'IBM', 'INTC', 'JNJ', 'JPM', 'MCD', 'MRK', 'MSFT', 'NKE', 'PFE',
          'PG', 'TRV', 'UNH', 'VZ', 'WMT', 'GOOGL', 'AMZN','SPY']

for ticker in stocks:
    file_name = 'data/' + ticker + '_' + start_date_str + '_to_' + end_date_str + '.csv'
    print(file_name)
    data = pdr.DataReader(ticker, 'yahoo', start, end)
    print(data.shape)
    data.to_csv(file_name)