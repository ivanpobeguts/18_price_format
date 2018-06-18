def format_price(price):
    try:
        price = float(price)
    except:
        return None
    price = round(price)
    formatted_price = '{:,}'.format(price).replace(',', ' ')
    return formatted_price


if __name__ == '__main__':
    print(format_price('567839'))
