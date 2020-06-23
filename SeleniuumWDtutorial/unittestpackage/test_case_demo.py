import unittest
class TestCaseDemo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("*#"*30)
        print("I will run once before every test")
        print("*#"*30)

    def setUp(self):
        print("I will run once before every test")

    def test_methodA(self):
        print("Running method A")

    def test_methodB(self):
        print("Running method B")

    def tearDown(self):
        print("I will run after every test case")
    @classmethod
    def tearDownClass(cls) -> None:
        print("*#"*30)
        print("I will run after every test case")
        print("*#"*30)


if __name__=='__main__':
    unittest.main(verbosity=2)

