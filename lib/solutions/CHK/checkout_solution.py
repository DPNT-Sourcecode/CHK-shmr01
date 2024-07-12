def create_special_pricing(multi_prices, multi_quantities):
    def price(amount, _basket):
        result = 0
        for multi_price, quantity in zip(multi_prices, multi_quantities):
            # print("calculating price", multi_price, quantity, amount)
            result += (amount // quantity) * multi_price
            # print("result", result)
            if amount >= (amount // quantity) * quantity:
                amount -= (amount // quantity) * quantity
        return result

    return price


def create_normal_pricing(single_price):
    return lambda amount, _basket: amount * single_price


def create_E_pricing(other_sku, single_price):
    def price(amount, basket):
        reductions = amount // 2
        basket[other_sku] -= reductions
        return amount * single_price

    return price


def create_F_pricing():
    def price(amount, _basket):
        if amount >= 3:
            reductions = amount // 3
            print(amount, reductions)
            amount -= reductions

        return amount * 10

    return price


prices = {
    "A": create_special_pricing([200, 130, 50], [5, 3, 1]),
    "B": create_special_pricing([45, 30], [2, 1]),
    "C": create_normal_pricing(20),
    "D": create_normal_pricing(15),
    "E": create_E_pricing(),
    "F": create_F_pricing(),
    "G": create_normal_pricing(20),
    "H": create_special_pricing([80, 45, 10], [10, 5, 1]),
    "I": create_normal_pricing(35),
    "J": create_normal_pricing(60),
    "K": create_special_pricing([150, 80], [2, 1]),
    "L": create_normal_pricing(80),
    "M": create_normal_pricing(15),
    "N": c,
}

prices_check_order = ["E", "A", "B", "C", "D", "F"]


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

    # print(basket)
    # remember to calculate E first
    for sku in prices_check_order:
        amount = basket[sku]
        if amount <= 0:
            continue
        price_func = prices[sku]
        result += price_func(amount, basket)
        # print("checking:", sku, basket, result)
    return result



