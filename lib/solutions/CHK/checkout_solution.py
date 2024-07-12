def create_special_pricing(single_price, multi_price, multi_quantity):
    def price(amount):
        return (amount / multi_quantity) * multi_price + (
            amount % multi_quantity
        ) * single_price

    return price


def create_normal_pricing(single_price):
    return lambda x: x * single_price


prices = {
    "A": create_special_pricing(50, 130, 3),
    "B": create_special_pricing(30, 45, 2),
    "C": create_normal_pricing(20),
    "D": create_normal_pricing(15),
}


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    # need to deploy to check how the string is encoded :/
    basket = {sku: 0 for sku in prices.keys()}
    last_amount = 0
    for sku in skus:
        # if it's a single
        if last_amount == 0:
            if sku not in prices:
                return -1

            basket[sku] += last_amount
            last_amount = 0
        else:
            assert int(sku) > 0
            last_amount = int(sku)
