# Price Formatter

The script get the price in input and format it.
  
# Usage from command line
  
Script requires python 3.5. Example on Linux (for Windows - the same):

```bash
$ python format_price.py 123987.0034

Formated price: 123 987
```

# Usage in class

```python
from format_price import format_price

price = 987256.98
print(format_price(price))
```

# Tests

You also can run tests:

```bash
$ python tests.py
.............
----------------------------------------------------------------------
Ran 13 tests in 0.000s

OK

```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
