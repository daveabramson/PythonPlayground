import unittest
from StepRangeSource import StepRangeSource

class MyTestClass(unittest.TestCase):

    def test_GetRange_GivenStepSize0_RaisesRuntimeError(self):
        #Arrange
        stepRange = StepRangeSource(0, 10, 0)
    
    
        #Act / Assert
        self.assertRaises(RuntimeError, stepRange.GetRange)


        #Assert (another one)
        #self.assertEqual('there are no values in the range', str(context.exception))

    #end def
    

    def test_GetRange_GivenStepSize0_GivesProperMessageInRuntimeError(self):
        #Arrange
        stepRange = StepRangeSource(0, 10, 0)
    
    
        #Act
        with self.assertRaises(RuntimeError) as context:
            rangeVals = stepRange.GetRange()

    
        #Assert
        self.assertEqual('there are no values in the range', str(context.exception))
    #end def


    def test_GetRange_GivenMin0Max10Step1_Returns0Through9(self):
        #Arrange
        stepRange = StepRangeSource(0, 10, 1)
        expected = [0,1,2,3,4,5,6,7,8,9]
        
    
        #Act
        rangeVals = stepRange.GetRange()

    
        #Assert
        self.assertListEqual(expected, rangeVals)
    #end def
    

    def test_GetRangeBound_WhenCalled_ReturnsMinAndMax(self):
        #Arrange
        expectedMin = 3
        expectedMax = 9
        stepRange = StepRangeSource(expectedMin, expectedMax, 1)

    
        #Act
        actualMin, actualMax = stepRange.GetRangeBounds()
    

        #Assert
        self.assertEqual(expectedMin, actualMin)
        self.assertEqual(expectedMax, actualMax)
    #end def
    
    

if __name__ == '__main__':
    unittest.main()


