import unittest

from caesar_cipher import caesarCipher

class TestCaesarCipher(unittest.TestCase):

    def test_cipher(self):
        self.assertEqual(caesarCipher("abc",1),"bcd")
        self.assertEqual(caesarCipher("ABC",1),"BCD")
        self.assertEqual(caesarCipher("xyz",1),"yza")

        
if __name__ == '__main__':
    unittest.main()
