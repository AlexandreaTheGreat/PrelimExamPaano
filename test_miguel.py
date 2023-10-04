#Create a unittest to check if the name is equal to MIGUEL.

import unittest

def name():
    x = 'miguel'
    return x.upper()

class Check(unittest.TestCase):

    def test(self):
        self.assertEqual(name(),'MIGUEL')

if __name__ == '__main__':
    unittest.main()