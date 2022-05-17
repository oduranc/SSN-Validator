import unittest
import principal

class TestPrincipal(unittest.TestCase):

    def test_checkFirst(self):
        #Positive Scenarios
        self.assertEqual(principal.checkFirst("005"), True)
        self.assertEqual(principal.checkFirst("868"), True)

        #Negative Scenarios
        self.assertEqual(principal.checkFirst("8688"), False)
        self.assertEqual(principal.checkFirst("000"), False)
        self.assertEqual(principal.checkFirst("666"), False)
        self.assertEqual(principal.checkFirst("945"), False)

    def test_checkSecond(self):
        #Positive Scenarios
        self.assertEqual(principal.checkSecond("23"), True)
        self.assertEqual(principal.checkSecond("76"), True)

        #Negative Scenarios
        self.assertEqual(principal.checkSecond("df"), False)
        self.assertEqual(principal.checkSecond("657"), False)
        self.assertEqual(principal.checkSecond("00"), False)

    def test_checkThird(self):
        #Positive Scenarios
        self.assertEqual(principal.checkThird("2002"), True)
        self.assertEqual(principal.checkThird("2457"), True)

        #Negative Scenarios
        self.assertEqual(principal.checkThird("257"), False)
        self.assertEqual(principal.checkThird("0000"), False)

if __name__ == "__main__":
    unittest.main()