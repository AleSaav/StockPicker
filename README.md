# StockPicker

Select stocks based on the greedy algorithm by maximizing weighted ROI depending
on the timeframe and budget inserted as arguments in the command line.

The function will run while the budget still has money left (budget > 0) this is then 
compared to verify if the amount of moeny left in the budget is enough to buy a full stock
or a fraction of a stock. 

In the case of buying a full stock, the stock name will be input into the selectedStock 
array.

In the case of buying a fraction of an array the fraction 
(which is rounded to 2 decimal places) bought and the stock name is input into the 
selectedStock array.

After buying the stocks, the stock price is removed from the budget.
