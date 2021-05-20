import pandas as pd
df=pd.read_csv('Salary_Data.csv')
df
import matplotlib.pyplot as plt
import pandas as pd
x=df['YearsExperience']
y=df['Salary']
plt.bar(x,y, width=0.07)
plt.show()
plt.hist(x)
plt.show()
plt.hist(y)
plt.show()
plt.scatter(x,y)
plt.show()
plt.boxplot(x)
plt.show()
plt.boxplot(y)
plt.show()