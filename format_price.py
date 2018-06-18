def format_price(price):
    if isinstance(price, float):
        price = round(price)
        formatted_price = '{:,}'.format(price).replace(',', ' ')
    elif isinstance(price, int):
        formatted_price = '{:,}'.format(price).replace(',', ' ')
    else:
        formatted_price = None
    return formatted_price


if __name__ == '__main__':
    print(format_price('dsf'))
