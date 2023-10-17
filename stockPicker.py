
import csv
import sys

""""
Select stocks based on the greedy algorithm by maximizing weighted ROI depending
on the timeframe inserted as argument 

The function will run while the budget still has money left (budget > 0) this is then 
compared to verify if the amount of moeny left in the budget is enough to buy a full stock
or a fraction of a stock. 

In the case of buying a full stock, the stock name will be input into the selectedStock 
array.

In the case of buying a fraction of an array the fraction 
(which is rounded to 2 decimal places) bought and the stock name is input into the 
selectedStock array

after buying the stocks, the stock price is removed from the budget
"""

def stockPicker(stockData, budget:float, timeframe:str) :
    selectedStocks = []

    while float(budget) > 0:

        weighted_return_max = max(stockData, key=lambda x: float(x[timeframe]) / float(x['price']))
        stock_price = float(weighted_return_max['price'])

        if stock_price > float(budget):
            fract = round(budget/stock_price, 2)
            budget -= fract
            fract = str(fract)
            selectedStocks.append(fract + ' ' + weighted_return_max['name'])
            break

        else:
            selectedStocks.append(weighted_return_max['\ufeffname'])
            #'\ufeffname' is used instead of 'name' because the program isn't throwing
            # the key correctly as 'name' so it's accounting for the error
            budget -= stock_price
            stockData.remove(weighted_return_max)

    # Print the selected stocks
    print(selectedStocks)

# Check if the correct number of command-line arguments is provided
if len(sys.argv) > 1:

    # Parse command-line arguments
    budget = float(sys.argv[1])
    timeframe = sys.argv[2]

    valid_timeframes = ['1m', '6m', '1y', '5y']
    index=0

    # Check if the roi timeframes input are valid
    for timeF in valid_timeframes:
        if timeframe != valid_timeframes[index]:
            index = index+1
        else:
            # change the timeframe to uppercase letters to account to the keys input by
            # the csv file as these are input in lowercase in the command line arguments
            timeframe = valid_timeframes[index].upper()
            break

    with open('stocks.csv', 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)  # Read the header row

        stockData = []
        for row in reader:
            record = {}
            for i, value in enumerate(row):
                record[headers[i]] = value
            stockData.append(record)

    '''
        Run the stockPicker function with the stockData dictionary and 
        the command line arguments <budget>, <timeframe>
    '''
    stockPicker(stockData, budget, timeframe)