import pandas as pd
import numpy as np
from math import log
import io
df = pd.read_csv('data.csv')
print(df)
df.set_index('ID', inplace=True)
df.head()
info = 0
vc = df['Class'].value_counts(normalize=True)
for item in df['Class'].unique():
    info += -(vc[item] * log(vc[item], 2))
print(info)

ll = list(df.columns)
ll.pop(-1)
print(ll)

for aa in ll: # Attributes
    info_smol = 0 # small info
    vc_class = df.groupby(aa)['Class'].value_counts(normalize=True) # Class value counts, target class
    vc_attr = vc = df[aa].value_counts(normalize=True)
# Attribute value counts, the one in aa
    for item in df[aa].unique():
# Unique values in attribute, eg. youth middle and old
        for target in vc_class[item].index:
            info_smol += -vc_attr[item]*vc_class[item][target]*log(vc_class[item][target], 2)
            
            ig = info - info_smol
    print("Attribute: ", aa)
    #print(vc)
    print("IG = ", ig, "\nInfo = ", info_smol)