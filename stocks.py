with open('prices.csv', 'r') as file:
    prices = file.read()

print(prices)

import pandas as pd

price_df = pd.read_csv('prices.csv', names=['ticker', 'date', 'open', 'high', 'low',
                                             'close', 'volume', 'adj_close', 'adj_volume'])
"""
That's what we're looking for! However, we don't want to run the groupby function each time
 we make an operation. We could save the GroupBy object by
 doing price_df_ticker_groups = price_df.groupby('ticker'). This limits us to the operations
 of GroupBy objects. There's the GroupBy.apply, but then we lose out on performance. The true
 problem is the way the data is represented.
"""

price_df.groupby('ticker').median()


"""
In our case, our third dimensions are "open", "high", "low", "close", "volume", "adj_close",
and "adj_volume". We'll use the DataFrame.pivot function to generate these DataFrames.
"""

open_prices = price_df.pivot(index='date', columns='ticker', values='open')
high_prices = price_df.pivot(index='date', columns='ticker', values='high')
low_prices = price_df.pivot(index='date', columns='ticker', values='low')
close_prices = price_df.pivot(index='date', columns='ticker', values='close')
volume = price_df.pivot(index='date', columns='ticker', values='volume')
adj_close_prices = price_df.pivot(index='date', columns='ticker', values='adj_close')
adj_volume = price_df.pivot(index='date', columns='ticker', values='adj_volume')

open_prices.mean()

"""
It doesn't matter whether date is the index and tickers are the colums or the other
 way around. It's always a transpose away. Since we're going to do a lot of operations
  across dates, we will stick with date as the index and tickers as the colums
  throughtout this program.
"""

open_prices.T.mean()


def csv_to_close(csv_filepath, field_names):
    """Reads in data from a csv file and produces a DataFrame with close data.

    Parameters
    ----------
    csv_filepath : str
        The name of the csv file to read
    field_names : list of str
        The field names of the field in the csv file

    Returns
    -------
    close : DataFrame
        Close prices for each ticker and date
    """

    # TODO: Implement Function

    return pd.read_csv(csv_filepath, names=field_names).pivot(index='date', columns='ticker', values='close')
