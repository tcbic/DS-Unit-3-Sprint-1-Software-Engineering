import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)
    
    def test_default_flammability(self):
        """Test default flammability being 0.5."""
        prod = Product('Test Product')
        self.assertEqual(prod.flammability, 0.5)

    def test_stealability_explode(self):
        """Builds an object with different values to ensure stealability
        and explode methods function."""
        #Create instances to test.
        not_so_stealable = Product(name="test1", price=2, weight=5)
        kinda_stealable = Product(name="test2", price=6, weight=10)
        very_stealable = Product(name="test3", price=25, weight=5)
        fizzle = Product(name="test4", flammability=2, weight=4)
        boom = Product(name="test5", flammability=4, weight=8 )
        baboom = Product(name="test6", flammability=5, weight=12)
        #Test the instances.
        self.assertEqual(not_so_stealable.stealability(), "Not so stealable...")
        self.assertEqual(kinda_stealable.stealability(), "Kinda stealable.")
        self.assertEqual(very_stealable.stealability(), "Very stealable!")
        self.assertEqual(fizzle.explode(), "...fizzle.")
        self.assertEqual(boom.explode(), "...boom!")
        self.assertEqual(baboom.explode(), "...BABOOM!")

class AcmeReportTests(unittest.TestCase):

    def test_default_num_products(self):
        """Checks that it really does receive a list of length 30."""
        list_of_products = generate_products()
        self.assertEqual(len(list_of_products), 30)

    def test_legal_names(self):
        """Checks that the generated names for a default batch of products
        are all  valid possible names to generate."""
        list_of_products = generate_products()
        

if __name__ == '__main__':
    unittest.main()