from RangeSource import RangeSource
from numpy import linspace

class EvenCountRangeSource(RangeSource):
    """a range source that creates n evenly spaced values in a range"""

    #init the class 
    #init of super will call CalculateValuesInRange
    def __init__(self, min, max, count, isClosedInterval=True):
        self.countOfValues = count
        self.isClosedInterval = isClosedInterval
        super().__init__(min, max)
        

    #override range value calculations
    def CalculateValuesInRange(self):
        if(self.countOfValues > 0):
            self.rangeValues = linspace(self.rangeMin, self.rangeMax, self.countOfValues, self.isClosedInterval).tolist()
