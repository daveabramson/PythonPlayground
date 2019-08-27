import abc
#from abc import ABC

class RangeSource(abc.ABC):
    """base class for types that create ranges in various ways"""



    #base init method sets min, max, and range values as an empty list
    #then calls to children to actually create the values in the range
    #
    #NOTE: Implementors should set values used in CalculateValuesInRange
    #      prior to calling super.__init__()
    def __init__(self, min, max):
        self.rangeMin = min
        self.rangeMax = max
        self.rangeValues = []
        self.CalculateValuesInRange()


    #get the min and max values of the range
    def GetRangeBounds(self):
        return self.rangeMin, self.rangeMax


    #get the values calculated for the range
    def GetRange(self):
        if(len(self.rangeValues) == 0):
            raise RuntimeError('there are no values in the range')
            pass
        return self.rangeValues


    @abc.abstractmethod
    def CalculateValuesInRange(self):
        pass



#end class RangeSource