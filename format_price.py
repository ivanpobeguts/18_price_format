import sys

def format_price(price):
    if isinstance(price, bool):
        return None
    try:
        price = float(price)
    except TypeError:
        return None
    price = round(price)
    formatted_price = '{:,}'.format(price).replace(',', ' ')
    return formatted_price


if __name__ == '__main__':
    price = [1, 2, 3]
    print(format_price(price))
