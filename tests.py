import surfshop
import unittest

class SamTests(unittest.TestCase):
    
    def setUp(self):
        self.cart = surfshop.ShoppingCart()

    def test_add_surf_boards_one(self):
        self.assertEqual(self.cart.add_surfboards(1), "Successfully added 1 surfboard to cart!")
    
    def test_add_surf_boards_two(self):
        self.assertEqual(self.cart.add_surfboards(2), "Successfully added 2 surfboards to cart!")

    def test_add_surf_boards_five(self):
        with self.assertRaises(surfshop.TooManyBoardsError):
            self.cart.add_surfboards(5)

unittest.main()