import abc
#from abc import ABC

class RangeSource(abc.ABC):
    """
       Description: base class for types that create ranges in various ways and put them in a list
       Notes:       None
    """


    #-------------------------------------------------------------------------------------------------------------
    #                                              ____I N I T____
    #-------------------------------------------------------------------------------------------------------------
    def __init__(self, min, max):
        """
           Purpose: Initialize the instance
           Inputs:  min - the minimum value in the range
                    max - the maximum value in the range (implementation specific if the max is in the final 
                          range of values
           Outputs: None
           Returns: None
           Notes:   base init method sets min, max, and range values as an empty list then calls to children to 
                    actually create the values in the range
                    
                    Implementors should set values used in CalculateValuesInRange prior to calling 
                    super().__init__(...)
        """
        self.rangeMin = min
        self.rangeMax = max
        self.rangeValues = []
        self.CalculateValuesInRange()


    #-------------------------------------------------------------------------------------------------------------
    #                                              P U B L I C
    #-------------------------------------------------------------------------------------------------------------
    #
    def GetRangeBounds(self):
        """
           Purpose: get the min and max values of the range
           Inputs:  None
           Outputs: None
           Returns: min value defining range, max value defining range
           Notes:   max value is not necessarily included in the list of values for the range, that is 
                    implementation specific
        """
        return self.rangeMin, self.rangeMax


    #get the values calculated for the range
    def GetRange(self):
        """
           Purpose: get the values calculated for the range
           Inputs:  None
           Outputs: None
           Returns: list of values calculated for the range
           Notes:   raises RuntimeError if there are no values calculated for the range
        """
        if(len(self.rangeValues) == 0):
            raise RuntimeError('there are no values in the range')
            pass
        return self.rangeValues


    #-------------------------------------------------------------------------------------------------------------
    #                                        A B S T R A C T   M E T H O D S
    #-------------------------------------------------------------------------------------------------------------
    @abc.abstractmethod
    def CalculateValuesInRange(self):
        """
           Purpose: Called in base class __init__ to calculate the list of values in the range
           Inputs:  None
           Outputs: Sets the self.rangeValues list
           Returns: None
           Notes:   None
        """
        pass



#end class RangeSource