import matplotlib.pyplot as plt
import numpy as np
"""
    Functions that I will be using:
"""
d=[3, 3, 6, 9, 16, 16, 16, 27, 27, 37, 48]
def uni(a):
    x=[]
    for i in a:
        if i not in x:
            x+=[i]
    return x
def listcopy(array):
    x=[]
    for i in  array:
        x+=[i]
    return x
def listdefiner(a):
    x = []
    for i in a:
        x+=[0]
    return x
def rep(count_unique,unique):
    m =max(count_unique)
    ind=[]
    for i in range(0,len(count_unique)):
        if(m==count_unique[i]):
            ind+=[i]
            count_unique[i]=0
    for i in ind:
        print(unique[i],end=",")
    print("\tcount: ",str(len(ind)),end="")
def bar_plotter(inp):
    if(inp=="y" or inp=="Y"):
        global count_unique
        global unique
        plt.bar(np.arange(len(unique)),count_unique,align="center",alpha=0.5)
        plt.xticks(np.arange(len(unique)),unique)
        plt.show()
"""
    This is where the real program starts
"""

unique=uni(d)
count_unique = listdefiner(uni(d))
print()
for i in range(0,len(unique)):
    for j in d:
        if(unique[i]==j):
            count_unique[i] +=1
ref =listcopy(count_unique)
for i in range(0,len(uni(count_unique))):
    print("Mode "+str(i+1)+" (Max count in data: "+str(max(ref))+"): ",end="")
    rep(ref,unique)
    print()
inp =  str(input("Do you want a graph: "))
bar_plotter(inp)
