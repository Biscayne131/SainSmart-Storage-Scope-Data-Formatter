# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 11:33:24 2016

@author: Can_
"""
import numpy as np
import matplotlib.pylab as plt
"""import scipy as scipy """
"""import function """
arrays = [np.array(map(str, line.split())) for line in open(r'C:\Users\Can_\Desktop\2016_2_11_H2so4_2kHz_PtElectrode2_2data.txt')]
n=0
z=1
v=[]
"""First column formatting(v is formatted output)"""
for n in range(len(arrays)):
    m=len(arrays[n][0])
    a=list(arrays[n][0])
    a[m-1]=""
    f="".join(a)
    q=f.replace("-,","-0,")
    v.append(q) 
    n=n+1
for z in range(len(v)):
    if len(v[z])==0:
        z=z+1
    elif v[z][0]==",":
        x=list(v[z])
        x[0]="0,"
        v[z]="".join(x)
        z=z+1
z=z+1   
del n, z
v1=[]
n=0
""" Second Column Formatting(v1 is the formatted output)"""
for n in range(len(arrays)):
    if len(arrays[n])==1:
        v1.append(0)
        n=n+1
    elif arrays[n][1][0]=="-":
        f1=arrays[n][1]
        q1=f1.replace("-,","-0,")
        v1.append(q1)
        n=n+1
    elif arrays[n][1][0]==",":
        a2=(arrays[n][1])
        q2=a2.replace(",","0,")
        v1.append(q2)
        n=n+1
    else:
        v1.append(arrays[n][1])
        n=n+1
z=0
""" "," to "." and also remove no data rows """
for z in range(len(v)):
    if v[z]==0 or v1[z]==0:
        v[z]=[]
        v1[z]=[]
        z=z+1

    else:
        v[z]=v[z].replace(",",".")
        v1[z]=v1[z].replace(",",".")
        z=z+1

del n,z
""" Float converter"""
z=0
for z in range(len(v)):
    if v[z]==[] or v1[z]==[] or v[z]=="" or v1[z]=="":
        v[z]=np.pi
        v1[z]=np.pi
        z=z+1

    else:
        v[z]=float(v[z])
        v1[z]=float(v1[z])
        z=z+1
""" nd.array conversion; a is the output"""       
n=0
b=0
a=np.ndarray([len(v),2])
for n in range(len(v)):

        a[n][0]=v[n]
        n=n+1
for b in range(len(v)):

        a[b][1]=v1[b]
        b=b+1 
""" removing pi"""         
c=0
c1=1
totalnodelrow=0
while c1>0:
    c1=0
    for c in range(len(a)):
        if a[c][1]==np.pi and a[c][0]==np.pi:
            c1=c1+1
            c=c+1
        else:
            c=c+1
        c2=0   
    for c2 in range(len(a)-c1):
            if a[c2][1]==np.pi and a[c2][0]==np.pi:
                a=np.delete(a, (c2), axis=0)
                c2=c2+1
                totalnodelrow=totalnodelrow+1
            else:
                c2=c2+1
"""625e3 is the sampling rate"""
time=len(a)/625e3
scale=np.linspace(1,len(a), num=len(a)) 
timescale=time*scale
plt.plot(timescale,a[:,0])   
plt.show()
plt.plot( timescale,a[:,1],)  
plt.show()          
plt.scatter(a[:,0],a[:,1])
plt.show()
np.savetxt("formatteddata.txt",a)
