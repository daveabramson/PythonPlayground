import math
import numpy as np

class coslist(object):
    """get a list of cosines in a range"""

    cosineList = []

    def __init__(self):
        pass

    # NEXT - create a "rangesource" class that can make ranges by step size or by count
    #        give this class an instance to get the range of angles from
    #        use this as an oppurtunity to learn TDD in python
    def cosinesOfRadInRange(self, minRad, maxRad, step):
        cosineList = []
        nprads = np.arange(minRad, maxRad, step)
        for rad in nprads:
            cosineList.append(math.cos(rad))
        return cosineList, nprads.tolist()

    def cosinesOfDegInRange(self, minDeg, maxDeg, step):
        cosineList = []
        npdegs = np.arange(minDeg, maxDeg, step)
        for deg in npdegs:
            cosineList.append(math.cos(math.radians(deg)))
        return cosineList, npdegs.tolist()

