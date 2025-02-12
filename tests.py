import surfshop
import unittest

class SamTests(unittest.TestCase):
    
    def setUp(self):
        self.cart = surfshop.ShoppingCart()

    def test_add_surf_boards(self):
        self.assertEquals(self.cart.add_surfboards(1), "Successfully added 1 surfboard to cart!")


unittest.main()