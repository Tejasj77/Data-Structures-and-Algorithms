import unittest
from Password_Cracker import attempt_1

class MyTestCase(unittest.TestCase):
    def test_something(self):
        passwords = ['fjrg','ckcapp','zhhwync','cgwkpsuzy','prnqnyek','tgfx','rxiydd','pgkujtpp','lxhwbxi','exsfzd']
        loginattempt = 'fjrgfjrgprnqnyekexsfzdlxhwbxilxhwbxizhhwynccgwkpsuzy'

        self.assertEqual(attempt_1.execution(), "".join())


if __name__ == '__main__':
    unittest.main()
