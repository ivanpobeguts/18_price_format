import argparse


def format_price(price):
    if isinstance(price, bool):
        return None
    try:
        price = float(price)
    except (TypeError, ValueError):
        return None
    price = round(price)
    formatted_price = '{:,.0f}'.format(price).replace(',', ' ')
    return formatted_price


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('price', help='Price value')
    return parser


if __name__ == '__main__':
    price = get_parser().parse_args().price
    formated_price = format_price(price)
    if not formated_price:
        print('Incorrect value for price:', price)
    else:
        print('Formated price:', formated_price)
