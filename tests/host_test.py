import unittest
import testinfra


class Test(unittest.TestCase):

    def setUp(self):
        self.host = testinfra.get_host("http://localhost")

if __name__ == "__main__":
    unittest.main()
