from solutions.CHK import checkout_solution


class TestCheckout:
    def test_checkout(self):
        assert checkout_solution.checkout("A") == 50
        assert checkout_solution.checkout("AA") == 100
        assert checkout_solution.checkout("AAA") == 130
        assert checkout_solution.checkout("AAAA") == 180
        assert checkout_solution.checkout("B") == 30
        assert checkout_solution.checkout("X") == -1
        assert checkout_solution.checkout("BX") == -1
        assert checkout_solution.checkout("BA") == 80

    def test_checkout_r2(self):
        assert checkout_solution.checkout("E") == 40
        # assert checkout_solution.checkout("EE") == 80
        # assert checkout_solution.checkout("EEB") == 80
        # assert checkout_solution.checkout("BEE") == 80
        # assert checkout_solution.checkout("EEBB") == 110
        # assert checkout_solution.checkout("EEEBB") == 150
        # assert checkout_solution.checkout("AEB") == 120
        # assert checkout_solution.checkout("AAAAA") == 200




