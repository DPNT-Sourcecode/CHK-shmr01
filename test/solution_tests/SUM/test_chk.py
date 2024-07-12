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
        assert checkout_solution.checkout("EE") == 80
        assert checkout_solution.checkout("EEB") == 80
        assert checkout_solution.checkout("BEE") == 80
        assert checkout_solution.checkout("EEBB") == 110
        assert checkout_solution.checkout("EEEBB") == 150
        assert checkout_solution.checkout("AEB") == 120
        assert checkout_solution.checkout("AAAAA") == 200
        assert checkout_solution.checkout("AAAAAA") == 250
        assert checkout_solution.checkout("AAAAAAA") == 300
        assert checkout_solution.checkout("AAAAAAAAAA") == 400
        assert checkout_solution.checkout("BBBB") == 90
        assert checkout_solution.checkout("ABCDECBAABCABBAAAEEAA") == 665

        """
Some requests have failed (3/40). Here are some of them:
 - {"method":"checkout","params":["AAAAAAAAAA"],"id":"CHK_R2_022"}, expected: 400, got: 630
 - {"method":"checkout","params":["BBBB"],"id":"CHK_R2_037"}, expected: 90, got: 150
 - {"method":"checkout","params":["ABCDECBAABCABBAAAEEAA"],"id":"CHK_R2_001"}, expected: 665, got: 725
        """



