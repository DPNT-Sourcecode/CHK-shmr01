def create_special_pricing(single_price, multi_prices, multi_quantities):
    def price(amount, _basket):
        result = 0
        for multi_price, quantity in zip(multi_prices, multi_quantities):
            result += (amount // quantity) * multi_price
            amount -= amount % quantity
        return (amount // multi_quantity) * multi_price + (
            amount % multi_quantity
        ) * single_price

    return price


def create_normal_pricing(single_price):
    return lambda amount, _basket: amount * single_price


def create_E_pricing():
    def price(amount, basket):
        reductions = amount // 2
        for _ in range(reductions):
            basket["B"] -= 1
        return amount * 40

    return price


prices = {
    "A": create_special_pricing(50, 130, 3),
    "B": create_special_pricing(30, 45, 2),
    "C": create_normal_pricing(20),
    "D": create_normal_pricing(15),
    "E": create_E_pricing(),
}

prices_check_order = ["E", "A", "B", "C", "D"]


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
    # remember to calculate E first
    for sku in prices_check_order:
        amount = basket[sku]
        if amount <= 0:
            continue
        price_func = prices[sku]
        result += price_func(amount, basket)
    return result

