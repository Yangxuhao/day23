import unittest
import 软件测试.myclass

class mytest(unittest.TestCase):
    def setUp(self):
        self.tclass=软件测试.myclass.data()
    def tearDown(self):
        pass
    def testsum(self):
        self.assertEquals(self.tclass.add(1,2),3,"错误")
    def testsub(self):
        self.assertEquals(self.tclass.sub(3,1),2,"错误")
if __name__=="__main__":
    unittest.main()