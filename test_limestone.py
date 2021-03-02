from limestone_finance import _query, get_price


def test__query():
    _query("data-latest", "AR", version="0.005", min_block=0)


def test_get_price():
    # get latest price for AR
    price = get_price("AR")
    print(price)


if __name__ == "__main__":
    test__query()
    test_get_price()
