import unittest
import numberprettifier as np

class NumberPrettifierTest(unittest.TestCase):
    
    def setUp(self):
        self.pn1 = np.PrettyNumber(1000000)
        self.pn2 = np.PrettyNumber(2500000.34)
        self.pn3 = np.PrettyNumber(532)
        self.pn4 = np.PrettyNumber(1123456789)
        self.pn5 = np.PrettyNumber(9487634567534)
        self.pn6 = np.PrettyNumber(9950000)

    def test_NumberPrettifier_countsDigits(self):
        self.assertEqual(self.pn1._countDigits(),7)
        self.assertEqual(self.pn2._countDigits(),7)
        self.assertEqual(self.pn3._countDigits(),3)
        self.assertEqual(self.pn4._countDigits(),10)
        self.assertEqual(self.pn5._countDigits(),13)
        self.assertEqual(self.pn6._countDigits(),7)
        self.assertEqual(np.PrettyNumber(999999.99)._countDigits(), 6)
    
    def test_NumberPrettifier_noPrettify(self):
        self.assertEqual(str(self.pn3), "532")
        pn2 = np.PrettyNumber(999999.99)
        pn3 = np.PrettyNumber(999990000000000)
        pn4 = np.PrettyNumber(1000000000000000)
        self.assertEqual(str(pn2),"999999.99")
        self.assertEqual(str(pn3), "999990000000000")
        self.assertEqual(str(pn4), "1000000000000000")

    def test_NumberPrettifier_changeScale(self):
        pn1 = np.PrettyNumber(999999000)
        pn2 = np.PrettyNumber(999990000000)
        self.assertEqual(str(pn1),"1B")
        self.assertEqual(str(pn2), "1T")

    def test_NumberPrettifier_singles(self):
        self.assertEqual(str(self.pn1),"1M")
        self.assertEqual(str(self.pn2), "2.5M")
        self.assertEqual(str(self.pn4), "1.1B")
        self.assertEqual(str(self.pn5), "9.5T")

    def test_NumberPrettifier_tens(self):
        pn1 = np.PrettyNumber(9950000)
        pn2 = np.PrettyNumber(68100697000)
        pn3 = np.PrettyNumber(51760000000000.99)
        self.assertEqual(str(pn1),"10M")
        self.assertEqual(str(pn2),"68.1B")
        self.assertEqual(str(pn3), "51.8T")

    def test_NumberPrettifier_hundreds(self):
        pn1 = np.PrettyNumber(700790000000)
        pn2 = np.PrettyNumber(169005003)
        pn3 = np.PrettyNumber(302346002666111)
        self.assertEqual(str(pn1), "700.8B")
        self.assertEqual(str(pn2), "169M")
        self.assertEqual(str(pn3), "302.3T")


if __name__ == '__main__':
    unittest.main()



