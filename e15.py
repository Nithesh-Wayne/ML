import numpy as np
from math import sqrt
import matplotlib.pyplot as plt
from matplotlib import style
from collections import Counter
import warnings
style.use('fivethirtyeight')



dataset = {'k':[[1,2],[2,3],[3,1]],'r':[[6,7],[7,7],[8,6]]}
new_features=[5,7]



##for i in dataset:
##    for ii in dataset[i]:
##        [plt.scatter(ii[o],ii[1],s=100,color=i)]

        #OR

##[[plt.scatter(ii[0],ii[1],s=100,color=i) for ii in dataset[i]]for i in dataset]
##plt.scatter(new_features[0],new_features[1])
##plt.show()

def k_nearest_neighbors(data,predict,k=3):
    if(len(data)>=3):
        warnings.warn('You are an idiot the data is greater than k')

    knnalgos
    return vote_result



#plot1=[1,3]
#plot2=[2,5]

#eucledian_distance=sqrt((plot1[0]-plot2[0])**2 + (plot1[1]-plot2[1])**2 )
#print(eucledian_distance)
