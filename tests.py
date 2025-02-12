import surfshop
import unittest

class SamTests(unittest.TestCase):
    
    def setUp(self):
        self.cart = surfshop.ShoppingCart()

    # Testing add_surf_boards
    def test_add_surf_boards(self):
        for num in [2, 3, 4]:
            with self.subTest(num):
                self.cart = surfshop.ShoppingCart()
                result = self.cart.add_surfboards(num)
                expected = f"Successfully added {num} surfboards to cart!"
                self.assertEqual(result, expected)

    @unittest.skip
    def test_add_surf_boards_five(self):
        with self.assertRaises(surfshop.TooManyBoardsError):
            self.cart.add_surfboards(5)

    # Testing apply_locals_discount
    def test_apply_locals_discount(self):
        self.assertTrue(self.cart.apply_locals_discount() == True)

unittest.main()