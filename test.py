import unittest
import calculator

class add_test(unittest.TestCase):

    def test_add(self):
        final = calculator.add(20,10)
        self.assertEqual(final,30)

    def test_add_fail(self):
        final = calculator.add(20,10)
        self.assertEqual(final,20)


    def test_sub(self):
        final = calculator.sub(20,10)
        self.assertEqual(final,10)
    def test_sub_fail(self):
        final = calculator.sub(20,10)
        self.assertEqual(final,20)


    def test_mult(self):
        final = calculator.mult(20,10)
        self.assertEqual(final,200)
    def test_mult_fail(self):
        final = calculator.mult(20,10)
        self.assertEqual(final,20)
    

    def test_div(self):
        final = calculator.div(20,10)
        self.assertEqual(final,2)
    def test_div_fail(self):
        final = calculator.div(20,10)
        self.assertEqual(final,20)

if __name__ == '__main__':
    unittest.name()
