from solutions.CHK import checkout_solution


class TestCheckout:
    def test_checkout(self):
        assert checkout_solution.checkout("A") == 50
        assert checkout_solution.checkout("AA") == 100
        assert checkout_solution.checkout("AAA") == 130
        assert checkout_solution.checkout("AAAA") == 180
        assert checkout_solution.checkout("B") == 30
        assert checkout_solution.checkout("x") == -1
        assert checkout_solution.checkout("Bx") == -1
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

    def test_checkout_r3(self):
        assert checkout_solution.checkout("F") == 10
        assert checkout_solution.checkout("FF") == 20
        assert checkout_solution.checkout("FFF") == 20
        assert checkout_solution.checkout("FFFF") == 30
        assert checkout_solution.checkout("FFFFFF") == 40

    def test_checkout_r4(self):
        assert checkout_solution.checkout("L") == 90
        assert checkout_solution.checkout("ABCDEFGHIJKLMNOPQRSTUVWXYZ") == 965
        assert (
            checkout_solution.checkout(
                "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
            )
            == 1880
        )
        """
    {"method":"checkout","params":["L"],"id":"CHK_R4_014"}, expected: 90, got: 80
     - {"method":"checkout","params":["ABCDEFGHIJKLMNOPQRSTUVWXYZ"],"id":"CHK_R4_033"}, expected: 965, got: 955
     - {"method":"checkout","params":["ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"],"id":"CHK_R4_139"}, expected: 1880, got: 1860
        """

