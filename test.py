import unittest, os

from lambda_function import unsubscribe


class TestUnsubscribe(unittest.TestCase):
    def test_unsubscribe(self):
        email = os.environ['USERNAME']
        unsubscribe(email)

if __name__ == '__main__':
    unittest.main()