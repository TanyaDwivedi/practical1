import numpy as np
import pandas as pd
import apriori
from mlxtend.frequent_patterns import association_rules

#Reading Data From UCI Repository
myretaildata = pd.read_excel('http://archive.ics.uci.edu/ml/machine-learningdatabases/00352/Online%20Retail.xlsx')
myretaildata.head()

#Data Cleaning
myretaildata['Description'] = myretaildata['Description'].str.strip()
myretaildata.dropna(axis=0, subset=['InvoiceNo'], inplace=True)
myretaildata['InvoiceNo'] = myretaildata['InvoiceNo'].astype('str')
myretaildata = myretaildata[~myretaildata['InvoiceNo'].str.contains('C')]
myretaildata.head()
myretaildata['Country'].value_counts()

#Choosing Germany
mybasket = (myretaildata[myretaildata['Country'] =="Germany"]
    .groupby(['InvoiceNo', 'Description'])['Quantity']
    .sum().unstack().reset_index().fillna(0)
    .set_index('InvoiceNo'))
mybasket.head()

#Encoding
def my_encode_units(x):
    if x <= 0:
        return 0
    if x >= 1:
        return 1

my_basket_sets = mybasket.applymap(my_encode_units)
my_basket_sets.drop('POSTAGE', inplace=True, axis=1)

#Generatig frequent itemsets
my_frequent_itemsets = apriori(my_basket_sets, min_support=0.07, use_colnames=True)

#generating rules
my_rules = association_rules(my_frequent_itemsets, metric="lift", min_threshold=1)

#viewing top 100 rules
my_rules.head(100)

#making recommendations
my_basket_sets['ROUND SNACK BOXES SET OF4 WOODLAND'].sum()
my_basket_sets['SPACEBOY LUNCH BOX'].sum()

#Filtering Rules based on a condition
my_rules[ (my_rules['lift'] >= 3) &
    (my_rules['confidence'] >= 0.3) ]