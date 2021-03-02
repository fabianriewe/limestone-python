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

price = get_price("AR", min_block=123456)
```

## Data format

```
{
  price: 2.05, //as Float
  updated: '2020-11-03 16:00:00', //as Date
}
```

## Testing
```
python test_limestone.py
```