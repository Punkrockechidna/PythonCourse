import unittest
import main


class TestMain(unittest.TestCase):
    def setUp(self):
        print('About to run a function')

    # ^^^^^^^ setup before each test
    def test_do_stuff(self):
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 15)  ##PASS
        # self.assertEqual(result, 10)  # FAIL

    def test_do_stuff2(self):
        test_param = 'sadfohusaidufg'
        result = main.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)  # PASS

    def test_do_stuff3(self):
        test_param = None
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'Please enter number')  # PASS

    def test_do_stuff4(self):
        test_param = ''
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'Please enter number')  # PASS

    def test_do_stuff5(self):
        test_param = 0
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'Please enter number that is not 0')  # PASS

    def tearDown(self):
        print('Cleaning up')


# Added isinstance ^ to match ValueErrors/changed assertEqual to assertTrue
# assertTrue changed to assertIsInstance
if __name__ == '__main__':
    unittest.main()

# Usually do in command line "python -m unittest  is file that I want to run"
# -v is verbose, adds more info to test results
# add comments by putting on single line with three ''' '''
