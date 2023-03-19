def getDataPoint(quote):
    """Given a stock quote string (e.g. "AAPL:123.45:125.67"), return a tuple of
    the stock symbol (e.g. "AAPL"), bid price (e.g. 123.45), ask price (e.g. 125.67),
    and price (e.g. 124.56, the average of the bid and ask prices).
    """
    symbol, bid_price, ask_price = quote.split(":")
    price = (float(bid_price) + float(ask_price)) / 2
    return (symbol, float(bid_price), float(ask_price), price)


def getRatio(price_a, price_b):
    """Given the prices of two stocks, return the ratio of their prices."""
    if price_b == 0:
        return 0
    return price_a / price_b


def main():
    """Connect to the data feed, process the feed to compute the ratio of the
    two stocks, and print the results to stdout.
    """
    # stocks we want to monitor
    stocks = {"AAPL": 0, "MSFT": 0}

    # initialize prices dictionary with initial data point for each stock
    prices = {}
    for stock in stocks.keys():
        prices[stock] = getDataPoint(quote=next(getQuotes(stock)))

    while True:
        # get the latest prices for each stock and update the prices dictionary
        for stock in stocks.keys():
            prices[stock] = getDataPoint(quote=next(getQuotes(stock)))

        # compute the ratio of the two stocks and print the results
        ratio = getRatio(prices["AAPL"][3], prices["MSFT"][3])
        print("Ratio AAPL/MSFT: {:.2f}".format(ratio))
