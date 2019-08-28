import math
import numpy as np
from RangeSource import RangeSource

class coslist(object):
    """get a list of cosines in a range"""

    def __init__(self):
        pass

    # NEXT - create a "rangesource" class that can make ranges by step size or by count
    #        give this class an instance to get the range of angles from
    #def cosinesOfRadInRange(self, minRad, maxRad, step):
    #    cosineList = []
    #    nprads = np.arange(minRad, maxRad, step)
    #    for rad in nprads:
    #        cosineList.append(math.cos(rad))
    #    return cosineList, nprads.tolist()

    #def cosinesOfDegInRange(self, minDeg, maxDeg, step):
    #    cosineList = []
    #    npdegs = np.arange(minDeg, maxDeg, step)
    #    for deg in npdegs:
    #        cosineList.append(math.cos(math.radians(deg)))
    #    return cosineList, npdegs.tolist()


    def CosinesOfRadianRange(self, rangeSource):
        cosineList = []
        rads = rangeSource.GetRange()
        self.__CalculateCosinesOnRangeOfAnglesInRadians(cosineList, rads)
        return cosineList, rads

    def CosinesOfDegreeRange(self, rangeSource):
        cosineList = []
        degs = rangeSource.GetRange()
        rads = list(map(lambda x:math.radians(x), degs))
        self.__CalculateCosinesOnRangeOfAnglesInRadians(cosineList, rads)
        return cosineList, degs

    def __CalculateCosinesOnRangeOfAnglesInRadians(self, cosineList, rads):
        for rad in rads:
            cosineList.append(math.cos(rad))

