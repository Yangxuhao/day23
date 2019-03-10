def add(x,y):
    return x+y

def sub(x,y):
    return x-y

import unittest

class mytest(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def testsum(self):
        self.assertEquals(add(1,2),3,"加法错误")
    def testsub(self):
        self.assertEquals(sub(11,3),8,"减法错误")

if __name__=="__main__":
    unittest.main()