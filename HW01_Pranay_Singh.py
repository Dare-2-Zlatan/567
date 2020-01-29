from math import sqrt
import unittest 
def classifyTriangle(a,b,c):
    x = sqrt(a**2 + b**2)
    y = a+b+c
    if y < (2*a) or y < (2*b) or y < (2*c):
        return "NotATriangle"
    if x==c:
        return "Right"

    if a==b==c:
        return "Equilateral"
    elif a==b or b==c or c==a:
        return "Isoceles"
    else:
        return "Scalene"
    
def runClassifyTriangle(a, b , c):
    print('classifyTriangle(',a, ',', b, ',', c, ')=',classifyTriangle(a,b,c),sep="")
    


def main():
    runClassifyTriangle(3,4,5)
    runClassifyTriangle(1,1,1)
 

class TestTriangles(unittest.TestCase):
    def testSet1(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')
        
    def testMyTestSet2(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
        self.assertNotEqual(classifyTriangle(10,10,10),'Isoceles','Should be Equilateral')
        self.assertEqual(classifyTriangle(10,15,30),'NotATriangle','Should be not be a Triangle')
        


if __name__ == '__main__':
    main()
    unittest.main(exit=False, verbosity=2)
