from math import pi
import numpy as np     # installed with matplotlib
#import matplotlib.pyplot as plt
from coslist import coslist


def main():
    
    # Calculate cosines of some angles given in radians
    cosListMaker = coslist()
    radCosList, radAngles, = cosListMaker.cosinesOfRadInRange(0, pi*2+.02, .01)

    # Calculate cosines of some angles given in degrees
    degCosListMaker = coslist()
    degCosList, degAngles, = cosListMaker.cosinesOfDegInRange(0, 380, 20)



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