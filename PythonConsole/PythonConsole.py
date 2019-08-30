from math import pi
import numpy as np     # installed with matplotlib
#import matplotlib.pyplot as plt
from ExampleLib.coslist import coslist
from ExampleLib.StepRangeSource import StepRangeSource
from ExampleLib.EvenCountRangeSource import EvenCountRangeSource


def main():
    
    # Calculate cosines of some angles given in radians
    cosListMaker = coslist()
    radCosList, radAngles = cosListMaker.CosinesOfRadianRange(StepRangeSource(0, 2.5*pi, pi/2))

    # Calculate cosines of some angles given in degrees
    degCosListMaker = coslist()
    #degCosList, degAngles = cosListMaker.CosinesOfDegreeRange(EvenCountRangeSource(0, 360, 5))
    degCosList, degAngles = degCosListMaker.CosinesOfDegreeRange(EvenCountRangeSource(0, 360, 37))


    print("cosines of angles in radians")
    i = 0
    for cosine in radCosList:
         print("cos(%f):%f" %(radAngles[i], cosine))
         i += 1

    i = 0
    print("cosines of angles in degrees")
    for cosine in degCosList:
         print("cos(%i):%f" %(degAngles[i], cosine))
         i += 1

    #x = np.arange(0, radians(1800), radians(12))
    #plt.plot(x, np.cos(x), 'b')
    #plt.show()

main()