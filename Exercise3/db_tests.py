import unittest
import main


class MyTestCase(unittest.TestCase):
    def test_salt_length(self):
        self.assertEqual(len(main.generate_salt(10)), 10)

    def test_login_length(self):
        self.assertEqual(len(main.generate_login(8)), 8)

    def test_password_verification_true(self):
        self.assertTrue(main.ver_passwd("strong#20#PassWd21"))

    def test_password_verification_false(self):
        self.assertFalse(main.ver_passwd("weakpassword"))

    def test_hashing(self):
        self.assertIsNotNone(main.hash_salted_password())

    def test_hashing_2(self):
        self.assertIsInstance(main.hash_salted_password_2(), str)

    def test_creating_connection(self):
        self.assertIsNotNone(main.create_connection())


if __name__ == '__main__':
    unittest.main()
