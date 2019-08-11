# -*- coding: utf-8 -*-
"""
Created on Wed May 22 13:51:27 2019

@author: daizh
"""
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import statistics as st

#p = ['0.0001', '0.0005', '0.001', '0.005','0.008', '0.01', '0.05']
# N=5000
#p = ['0.00001','0.00003','0.00005','0.00008','0.0001','0.00015','0.0002','0.0003','0.00035','0.0004','0.0005','0.0006','0.0007','0.00074','0.0008','0.0009','0.001','0.005','0.008', '0.01', '0.05']
# N=1000
#p = ['0.0001','0.0003','0.0005','0.0008','0.001','0.0013','0.0015','0.0018','0.002','0.0023','0.0025','0.0028','0.003','0.0033','0.0035','0.0038','0.004','0.005','0.006','0.008','0.01']
# N = 3000
p = ['0.0001','0.00015','0.0002','0.00025','0.0003','0.00033','0.00035','0.00038','0.0004','0.00045','0.0005','0.0006','0.00065','0.0007','0.00075','0.0008','0.00085','0.0009','0.00095','0.001','0.0015','0.002','0.0025','0.003','0.004','0.005','0.008','0.01']
listOfLists = [[] for i in range(len(p))]
dy = list()

for i in range(0,len(p)):
        f = open("result_p%s.txt" % p[i], "r")
        listOfLists[i] = list(f)
        for j in range(0,len(listOfLists[i])):
            listOfLists[i][j] = float(listOfLists[i][j].rstrip("\n"))
            #print (listname[i][j])
f.close()            
result = []
for number in listOfLists:
    final = sorted(number)
    final = [item for item in final if item < 0]
    #final = final[1:len(number)-1]
    SD = st.stdev(final)/np.sqrt(len(final)-1)
    dy.append(SD)
    result.append(np.mean(final))                
    print(len(final))
plt.title('Expoential Fitting for Autocorrelation Funciton: y = a*exp(bx) ')
plt.xlabel('Probability P')
plt.ylabel('b')
plt.errorbar([float(number) for number in p], result, yerr=dy, fmt='o', color='blue',
             ecolor='red', elinewidth=3, capsize=0)
#plt.plot(float(p[6]), result[6], 'g*')
#plt.plot(float(p[13]), result[13], 'bo')
plt.legend(title='N=3000')
plt.xscale('log')
plt.savefig("N=3000_errorbar_nosq.png", dpi=1500)
plt.show()