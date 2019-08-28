import math
from RangeSource import RangeSource

class coslist(object):
    """
       Description: A class that calculates cosines over lists of angles
       Notes:       Ranges of angles are provided by RangeSource objects
    """

    #-------------------------------------------------------------------------------------------------------------
    #                                              ____I N I T____
    #-------------------------------------------------------------------------------------------------------------
    def __init__(self):
        """
           Purpose: Initialize the instance
           Inputs:  None
           Outputs: None
           Returns: None
           Notes:   None
        """
        pass

    #-------------------------------------------------------------------------------------------------------------
    #                                                P U B L I C
    #-------------------------------------------------------------------------------------------------------------
    def CosinesOfRadianRange(self, rangeSource):
        """
           Purpose: Calculate all cosines over angles given in radians in a range
           Inputs:  rangeSource - a child of RangeSource that will provide the angles on which to calculate 
                                  cosines
           Outputs: None
           Returns: list of cosines, list of angles that cosines were calculated on
           Notes:   None
        """
        cosineList = []
        rads = rangeSource.GetRange()
        self.__CalculateCosinesOnRangeOfAnglesInRadians(cosineList, rads)
        return cosineList, rads


    def CosinesOfDegreeRange(self, rangeSource):
        """
           Purpose: Calculate all cosines over angles given in degrees in a range
           Inputs:  rangeSource - a child of RangeSource that will provide the angles on which to calculate 
                                  cosines
           Outputs: None
           Returns: list of cosines, list of angles that cosines were calculated on
           Notes:   None
        """
        cosineList = []
        degs = rangeSource.GetRange()
        rads = list(map(lambda x:math.radians(x), degs))
        self.__CalculateCosinesOnRangeOfAnglesInRadians(cosineList, rads)
        return cosineList, degs

    #-------------------------------------------------------------------------------------------------------------
    #                                            P R I V A T E
    #-------------------------------------------------------------------------------------------------------------
    def __CalculateCosinesOnRangeOfAnglesInRadians(self, cosineList, rads):
        for rad in rads:
            cosineList.append(math.cos(rad))

