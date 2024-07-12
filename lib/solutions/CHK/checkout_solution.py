def create_special_pricing(multi_prices, multi_quantities):
    def price(amount, _basket):
        result = 0
        for multi_price, quantity in zip(multi_prices, multi_quantities):
            result += (amount // quantity) * multi_price
            amount -= amount % quantity
        return result

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
    "A": create_special_pricing([200, 130, 50], [5, 3, 1]),
    "B": create_special_pricing([45, 30], [2, 1]),
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

    print(basket)
    # remember to calculate E first
    for sku in prices_check_order:
        amount = basket[sku]
        if amount <= 0:
            continue
        price_func = prices[sku]
        result += price_func(amount, basket)
        print("checking:", sku, basket, result)
    return result



