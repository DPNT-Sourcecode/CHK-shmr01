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


def create_E_pricing(other_sku, amount_for_offer, single_price):
    def price(amount, basket):
        reductions = amount // amount_for_offer
        basket[other_sku] -= reductions
        return amount * single_price

    return price


def create_F_pricing(group_size, single_price):
    def price(amount, _basket):
        if amount >= group_size:
            reductions = amount // group_size
            print(amount, reductions)
            amount -= reductions

        return amount * single_price

    return price


def create_group_pricing(member, single_price):
    group_members = ["Z", "Y", "S", "T", "X"]

    def price(amount, basket):
        group_counter = 0
        for member in group_members:
            group_counter += basket[member]
        member_idx = 0
        group_price = 45 * group_counter // 3

        # update basket
        while group_counter >= 3 and member_idx > len(group_members):
            print(basket)
            member = group_members[member_idx]
            if basket[member] > 0:
                basket[member] -= 1
                group_counter -= 1
                continue
            member_idx += 1
        assert member in basket
        return (single_price * basket[member]) + group_price

    return price


prices = {
    "A": create_special_pricing([200, 130, 50], [5, 3, 1]),
    "B": create_special_pricing([45, 30], [2, 1]),
    "C": create_normal_pricing(20),
    "D": create_normal_pricing(15),
    "E": create_E_pricing("B", 2, 40),
    "F": create_F_pricing(3, 10),
    "G": create_normal_pricing(20),
    "H": create_special_pricing([80, 45, 10], [10, 5, 1]),
    "I": create_normal_pricing(35),
    "J": create_normal_pricing(60),
    "K": create_special_pricing([120, 70], [2, 1]),
    "L": create_normal_pricing(90),
    "M": create_normal_pricing(15),
    "N": create_E_pricing("M", 3, 40),
    "O": create_normal_pricing(10),
    "P": create_special_pricing([200, 50], [5, 1]),
    "Q": create_special_pricing([80, 30], [3, 1]),
    "R": create_E_pricing("Q", 3, 50),
    "S": create_normal_pricing(20),
    "T": create_normal_pricing(20),
    "U": create_F_pricing(4, 40),
    "V": create_special_pricing([130, 90, 50], [3, 2, 1]),
    "W": create_normal_pricing(20),
    "X": create_normal_pricing(17),
    "Y": create_normal_pricing(20),
    "Z": create_group_pricing("Z", 21),
}

prices_check_order = [
    "A",
    "E",
    "B",
    "C",
    "D",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "N",
    "M",
    "O",
    "P",
    "R",
    "Q",
    "Z",
    "S",
    "T",
    "U",
    "V",
    "W",
    "Y",
    "X",
]


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




