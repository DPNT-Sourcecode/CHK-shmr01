def create_special_pricing(single_price, multi_price, multi_quantity):
    def price(amount):
        return (amount / multi_quantity) * multi_price + (
            amount % multi_quantity
        ) * single_price
    return price

def create_normal_pricing(single_price):
    return lambda x: x*single_price

prices = {"A": create_special_pricing(50, 130, 3), "B" : create_special_pricing(30, 45, 2),
          "C"}


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    raise NotImplementedError()

