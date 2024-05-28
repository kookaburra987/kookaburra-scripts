import unittest

from encryption import caesarEncrypt


class EncryptTest(unittest.TestCase):
    def test_encrypt_str(self):
        key = "9876543210abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        cyper_text = caesarEncrypt.encrypt_str("All digits 0123456789; and characters a to z and A to Z.", key)
        self.assertEqual("aLL DIGITS 9876543210; AND CHARACTERS A TO Z AND a TO z.", cyper_text)  # add assertion here


if __name__ == '__main__':
    unittest.main()
