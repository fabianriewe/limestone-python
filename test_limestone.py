from limestone_finance import _query, get_price


def test__query():
    price = _query("data-latest", "AR", version="0.005", max_block=None)
    print(price)


def test_get_price():
    # get latest price for AR
    price = get_price("AR")
    print(price)

    # get price at a specific block height
    price = get_price("AR", at_block=633737)
    print(price)


if __name__ == "__main__":
    test__query()
    test_get_price()
