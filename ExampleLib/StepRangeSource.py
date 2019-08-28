from RangeSource import RangeSource
from numpy import arange


class StepRangeSource(RangeSource):
    """a range source that creates values in a range by step size and does not include the
       end-point of the range. (It is a half-closed range [min,max) )"""

    #init the class 
    #init of super will call CalculateValuesInRange
    def __init__(self, min, max, step):
        self.stepSize = step
        super().__init__(min, max)

    #override range value calculations
    def CalculateValuesInRange(self):
         if(self.stepSize > 0):
            self.rangeValues = arange(self.rangeMin, self.rangeMax, self.stepSize).tolist()
