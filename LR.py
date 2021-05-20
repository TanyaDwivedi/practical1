import pandas as pd
df=pd.read_csv('diabetes.csv')
df=pd.read_csv('Salary_Data.csv')
#df=pd.read_csv('/content/sample_data/salary.csv')
df
import numpy as np
dataset=list(df)
oplist=np.array(list(df[dataset[-1]])).astype('float64')
opmean=np.array([np.mean(oplist)]*len(oplist))
oplist-=opmean
nofatri=len(dataset)
mainmean=[]
coef=[]
sumXY=sumXsqr=0
for atri in dataset[:-1]:
    temp=np.array(list(df[atri])).astype('float64')
    mainmean.append(np.mean(temp))
    temp1=np.array([np.mean(temp)]*len(temp))
    temp-=temp1
    tempxoplist=np.multiply(temp,oplist)
    temp2=np.multiply(temp,temp)
    sumXY+=tempxoplist.sum()
    sumXsqr+=temp2.sum()
    coef.append(sumXY/sumXsqr)

print("coefficient array:",coef)
theconstant=opmean[0]
for i in range(len(mainmean)):
    theconstant-=(coef[i]*mainmean[i])

print("b =",theconstant)
print("y =",theconstant,"+",end=" ")
for i in range(len(coef)-1):
    print(coef[i],f"x{(i+1)}","+",end=" ")
print(coef[-1],f"x{len(coef)}")

y=theconstant
#testing for multiple regression
for i in range(len(coef)):
    if i==0:
        y+=coef[i]*1
    if i==1:
        y+=coef[i]*93
    if i==2:
        y+=coef[i]*70
    if i==3:
        y+=coef[i]*31
    if i==4:
        y+=coef[i]*0
    if i==5:
        y+=coef[i]*30.4
    if i==6:
        y+=coef[i]*0.315
    if i==7:
        y+=coef[i]*23
print("y =",y)
#testing for simple regression
#print("y =",coef[0]*2+theconstant)
#visualization of simple regression
import matplotlib.pyplot as mpl
import pandas as pd
X=df['YearsExperience']
Y=df['Salary']
mpl.scatter(X, Y)
mpl.show()