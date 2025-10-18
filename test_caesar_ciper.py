import unittest

from caesar_cipher import caesarCipher

class TestCaesarCipher(unittest.TestCase):

    def test_cipher(self):
        self.assertEqual(caesarCipher("abc",1),"bcd")
        self.assertEqual(caesarCipher("ABC",1),"BCD")
        self.assertEqual(caesarCipher("xyz",1),"yza")
        self.assertEqual(caesarCipher("XYZ",1),"YZA")
        self.assertEqual(caesarCipher("abc",-1),"zab")
        self.assertEqual(caesarCipher("z",1),"a")
        self.assertEqual(caesarCipher("Z",1),"A")
        self.assertEqual(caesarCipher("a",-1),"z")
        self.assertEqual(caesarCipher("A",-1),"Z")
        self.assertEqual(caesarCipher("Hello Internet",5),"Mjqqt Nsyjwsjy")
        self.assertEqual(caesarCipher("Mjqqt Nsyjwsjy",-5),"Hello Internet")
        self.assertEqual(caesarCipher("1234567890",1),"1234567890")
        self.assertEqual(caesarCipher("!@#$%^&*()_+-=",1),"!@#$%^&*()_+-=")
        self.assertEqual(caesarCipher("[]',./",1),"[]',./")
        self.assertEqual(caesarCipher('{}"|<>?',1),'{}"|<>?')
        self.assertEqual(caesarCipher("\\",1),"\\")
        
if __name__ == '__main__':
    unittest.main()
