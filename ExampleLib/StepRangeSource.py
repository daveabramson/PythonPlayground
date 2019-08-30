from ExampleLib.RangeSource import RangeSource
from numpy import arange


class StepRangeSource(RangeSource):
    """
       Description: a range source that creates values in a range by step size and does not include the end-point
                    of the range. 
       Notes:       (It is a half-closed range [min,max))
    """

    #-------------------------------------------------------------------------------------------------------------
    #                                              ____I N I T____
    #-------------------------------------------------------------------------------------------------------------
    def __init__(self, min, max, step):
        """
           Purpose: Initialize the instance
           Inputs:  min - see RangeSource
                    max - see RangeSource
                    step - interval between values in the range list
           Outputs: None
           Returns: None
           Notes:   init of super will call CalculateValuesInRangeone
        """
        self.stepSize = step
        super().__init__(min, max)

    #-------------------------------------------------------------------------------------------------------------
    #                                                P U B L I C
    #-------------------------------------------------------------------------------------------------------------

    def CalculateValuesInRange(self):
        """
           Purpose: Calculate values in the range using the numpy arange way (based on a stepsize)
           Inputs:  None
           Outputs: Sets the self.rangeValues list
           Returns: None
           Notes:   None
        """
        if(self.stepSize > 0):
            self.rangeValues = arange(self.rangeMin, self.rangeMax, self.stepSize).tolist()
