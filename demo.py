import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        print ('Test 1')
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        print ('Test 2')
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())
	
    def test_isupper321(self):
        print ('Test 3')
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_isupper2(self):
        print ('Test 4')
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        print ('Test 5')
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
	
