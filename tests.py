import unittest
import tlaciaren

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


    def test_can_picture_fit(self):
        zostatok = [5,1,8]
        obr = [3,2,1]
        self.assertFalse(tlaciaren.can_picture_fit(zostatok,obr))

    def test_substract(self):
        zostatok = [5,6,9]
        obr = [1,2,3]
        rozdiel = [4,4,6]
        self.assertEqual(rozdiel,tlaciaren.substract(zostatok,obr))
if __name__ == '__main__':
    unittest.main()
