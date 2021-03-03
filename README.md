# limestone-python

An api to access trusted token pricing data secured on Arweave and protected by provider's collateral.

## Installation
`pip install limestone-finance`

## Usage

### Getting the latest price
```python
from limestone_finance import get_price

price = get_price("AR")
```

### Getting price at a specific block
```python
from limestone_finance import get_price

price = get_price("AR", at_block=123456)
```

## Data format

```
{
  price: 11.74, //as Float
  updated: '2021-02-25T07:55:00.467000', //as UTC Date string
}
```

## Testing
```
python test_limestone.py
```