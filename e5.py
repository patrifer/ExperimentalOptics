'''
@author="Patricia Fernandez de Cos"
@date="05-03-2019"
The aim of this porgram is to perform all the calculations needed throughout the experiment 5
Inputs: 6 alpha values in degrees
Outputs: average value of alpha, standard deviation of alpha, variance of alpha, variance of the average of alpha,
 d and/or lambda and its standard deviation
'''
import numpy as np 
import statistics as stats
import math as mp
 
#Values of alpha --- abs(xd-xi)/2 (degrees)
muestra=[(35.8/2.0), (35.766666667/2.0),(35.76666667/2.0), (35.733333333/2.0), (35.766666667/2.0), (35.733333333/2.0)]
avg=float(stats.mean(muestra))
print("Media=",avg)
stdv= float (stats.pstdev(muestra))
print("Ds=",stdv)
print("Vz=", stdv*stdv)
stdvavg=float((stdv*stdv)/6.0)
print("Stdvav=", stdvavg)

#Computation of d  (nm)
#All this block except stdvavdrad should be removed for the computation of lambda
#If you wish to perform the calculation using another wavelength the value 480 should be modified
d= float ((480.0)/(2*mp.sin(mp.radians(avg))))
print("d=",d)
den =float ((mp.sin(mp.radians(avg)))*(mp.sin(mp.radians(avg))))
num=float(480.0*mp.cos(mp.radians(avg)))
ang=((num)/(2.0*den))
stdvavdrad=float(stdvavg*( ((2*(mp.pi))*(2*(mp.pi)))/ (360.0*360.0)))
sigmad=float(mp.sqrt(stdvavdrad*ang*ang))
print("sigmad=", sigmad)



#Computation of the unknown wavelength (nm)
#Note that the hash key preceding d and sigmad should be removed 
#and the values previosuly obtained for d and sigmad should be written there
#d=0000
#sigmad=0000
l=float(2*d*(mp.sin(mp.radians(avg))))
sum1= float(2*(mp.sin(mp.radians(avg))))
sum2=float(2*d*(mp.cos(mp.radians(avg))))
sigmalambda=float(mp.sqrt(sum1*sum1*sigmad*sigmad+sum2*sum2*stdvavdrad))
print("lambda=", l)
print("sigmalambda=", sigmalambda)

