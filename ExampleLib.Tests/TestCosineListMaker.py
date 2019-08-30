import unittest
from ExampleLib.StepRangeSource import StepRangeSource
from ExampleLib.EvenCountRangeSource import EvenCountRangeSource
from math import pi
import coslist

class TestCosineListMaker(unittest.TestCase):

    def test_CosinesOfRadianRange_Given0Through2piCountRange_ReturnsCosMax0Min0Max(self):
        #Arrange
        rangeSource = EvenCountRangeSource(0, 2*pi, 5)
        cosListMaker = coslist.coslist()
        expectedCosines = [1,0,-1,0,1]

    
        #Act
        cosines, angles = cosListMaker.CosinesOfRadianRange(rangeSource)

    
        #Assert
        self.assertListEqual([0,pi/2,pi,pi*1.5,pi*2], angles)
        self.assertEqual(len(expectedCosines), len(cosines))
        for expCos, actCos in zip(expectedCosines, cosines):
            self.assertAlmostEquals(expCos, actCos, delta=0.00000000001)
    #end def
    
    def test_CosinesOfRadianRange_Given0Through2piInHalfpiSteps_ReturnsCosMax0Min0Max(self):
        #Arrange
        rangeSource = StepRangeSource(0, 2.5*pi, pi/2)
        cosListMaker = coslist.coslist()
        expectedCosines = [1,0,-1,0,1]

    
        #Act
        cosines, angles = cosListMaker.CosinesOfRadianRange(rangeSource)
    
    
        #Assert
        self.assertListEqual([0,pi/2,pi,pi*1.5,pi*2], angles)
        self.assertEqual(len(expectedCosines), len(cosines))
        for expCos, actCos in zip(expectedCosines, cosines):
            self.assertAlmostEquals(expCos, actCos, delta=0.00000000001)
    #end def
    
    def test_CosinesOfDegreeRange_Given0Through360CountRange_ReturnsCosMax0Min0Max(self):
        #Arrange
        rangeSource = EvenCountRangeSource(0, 360, 5)
        cosListMaker = coslist.coslist()
        expectedCosines = [1,0,-1,0,1]

    
        #Act
        cosines, angles = cosListMaker.CosinesOfDegreeRange(rangeSource)

    
        #Assert
        self.assertListEqual([0,90,180,270,360], angles)
        self.assertEqual(len(expectedCosines), len(cosines))
        for expCos, actCos in zip(expectedCosines, cosines):
            self.assertAlmostEquals(expCos, actCos, delta=0.00000000001)
    #end def
    

    def test_CosinesOfDegreeRange_Given0Through360In90Steps_ReturnsCosMax0Min0Max(self):
        #Arrange
        rangeSource = StepRangeSource(0, 360+90, 90)
        cosListMaker = coslist.coslist()
        expectedCosines = [1,0,-1,0,1]

    
        #Act
        cosines, angles = cosListMaker.CosinesOfDegreeRange(rangeSource)

    
        #Assert
        self.assertListEqual([0,90,180,270,360], angles)
        self.assertEqual(len(expectedCosines), len(cosines))
        for expCos, actCos in zip(expectedCosines, cosines):
            self.assertAlmostEquals(expCos, actCos, delta=0.00000000001)
    #end def

if __name__ == '__main__':
    unittest.main()
