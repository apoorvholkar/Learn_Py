import os
import numpy as np
import pandas as pd

econList = range(110)

for econID in econList:
    try:
        filePath1 = '\\7VR7G2S\ParallelU4_Oct\ProductionData\DTD\step1' + str(econID) 
        filePath2 = "\\7VR7G2S\ParallelU4_Oct\ProductionData\DTD\step2" + str(econID)
        #filePath1 = 'X:\\ProductionData\\DTD\\step1\\' + str(econID) 
        #filePath2 = 'X:\\ProductionData\\DTD\\step2\\' + str(econID)
        
        
        l1 = [int(item[-6:]) for item in os.listdir(filePath1)]
        
        l2 = [int(item[-6:]) for item in os.listdir(filePath2)]
        
        a = []
        for item in l1:
            if item not in l2:
                a.append(item)
        
        if a != []:
            a = pd.Series(np.asarray(a))
            fileName = 'Econ' + str(econID) + '.csv'
            a.to_csv(fileName)
    except:
        print 'no Econ' + str(econID)
