from ExampleLib.RangeSource import RangeSource
from numpy import linspace

class EvenCountRangeSource(RangeSource):
    """
       Description: a range source that creates n evenly spaced values in a range
       Notes:       Inclusion of max value is controlled by isClosedInterval in __init__
    """

    #-------------------------------------------------------------------------------------------------------------
    #                                              ____I N I T____
    #-------------------------------------------------------------------------------------------------------------
    def __init__(self, min, max, count, isClosedInterval=True):
        """
           Purpose: Initialize the instance
           Inputs:  min - see RangeSource
                    max - see RangeSource
                    count - the number of values to put into the range list
                    isClosedInterval - make true to include max in the range list, false to exclude it
           Outputs: None
           Returns: None
           Notes:   init of super will call CalculateValuesInRangeone
        """
        self.countOfValues = count
        self.isClosedInterval = isClosedInterval
        super().__init__(min, max)
        

    #-------------------------------------------------------------------------------------------------------------
    #                                                P U B L I C
    #-------------------------------------------------------------------------------------------------------------

    def CalculateValuesInRange(self):
        """
           Purpose: Calculate values in the range using the numpy linspace way (based on a count)
           Inputs:  None
           Outputs: Sets the self.rangeValues list
           Returns: None
           Notes:   list will include the max value specified in __init__ if a closed interval was also specified
        """
        if(self.countOfValues > 0):
            self.rangeValues = linspace(self.rangeMin, self.rangeMax, self.countOfValues, self.isClosedInterval)\
                               .tolist()
