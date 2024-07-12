def create_special_pricing(single_price, multi_price, multi_quantity):
    def price(amount, _basket):
        return (amount // multi_quantity) * multi_price + (
            amount % multi_quantity
        ) * single_price

    return price


def create_normal_pricing(single_price):
    return lambda amount, _basket: amount * single_price

def create_E_pricing():
    def price(amount, basket):
        return (amount // ) * multi_price + (
            amount % multi_quantity
        ) * single_price

    return price

prices = {
    "A": create_special_pricing(50, 130, 3),
    "B": create_special_pricing(30, 45, 2),
    "C": create_normal_pricing(20),
    "D": create_normal_pricing(15),
    "E": create_E_pricing()
}


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    # need to deploy to check how the string is encoded :/
    basket = {sku: 0 for sku in prices.keys()}
    for sku in skus:
        if sku not in prices:
            return -1
        basket[sku] += 1

    result = 0
    for sku, amount in basket.items():
        price_func = prices[sku]
        result += price_func(amount)
    return result



