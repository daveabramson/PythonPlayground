import unittest
from ExampleLib.EvenCountRangeSource import EvenCountRangeSource

class TestEvenCountRangeSource(unittest.TestCase):

    def test_GetRange_GivenCountOf0_ThrowsException(self):
        #Arrange
        evenCountRange = EvenCountRangeSource(0, 10, 0)
        
        
        #Act - and Assert
        with self.assertRaises(RuntimeError) as context:
            rangeVals = evenCountRange.GetRange()


        #Assert (another one)
        self.assertEqual('there are no values in the range', str(context.exception))
    #end def



    def test_GetRange_GivenCountOf10AndHalfOpenRange0To10_Returns0Through9(self):
        #Arrange
        evenCountRange = EvenCountRangeSource(0, 10, 10, False)
        expected = [0,1,2,3,4,5,6,7,8,9]
        

        #Act 
        rangeVals = evenCountRange.GetRange()


        #Assert (another one)
        self.assertListEqual(expected, rangeVals)

    #end def



    def test_GetRange_GivenCountOf11AndClosedRange0To10_Returns0Through10(self):
        #Arrange
        evenCountRange = EvenCountRangeSource(0, 10, 11)
        expected = [0,1,2,3,4,5,6,7,8,9,10]
        

        #Act 
        rangeVals = evenCountRange.GetRange()


        #Assert (another one)
        self.assertListEqual(expected, rangeVals)

    #end def



if __name__ == '__main__':
    unittest.main()
