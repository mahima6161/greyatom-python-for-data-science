# --------------
# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')


#Reading file
bank_data = pd.read_csv(path)
bank=pd.DataFrame(bank_data)

categorical_var=bank.select_dtypes(include='object')
#Code starts here
#print(categorical_var)

numerical_var=bank.select_dtypes(include = 'number')
#print(numerical_var)

#print(categorical_var.shape)
#print(numerical_var.shape)

banks=bank.drop('Loan_ID',axis=1)
#print(banks.isnull().sum())

bank_mode=banks.mode(axis=0)
#print(bank_mode)

for column in banks.columns:
    banks[column].fillna(banks[column].mode()[0], inplace=True)

#print(banks.isnull().sum().values.sum())

avg_loan_amount = banks.pivot_table(index=['Gender','Married','Self_Employed'], values=['LoanAmount'], aggfunc=[np.mean])

loan1=banks[banks["Self_Employed"]=='Yes']
loan2=loan1[banks["Loan_Status"]=='Y']

loan_approved_se=len(loan2.index)
print(loan_approved_se)

loan3=banks[banks["Self_Employed"]=='No']
loan4=loan3[banks["Loan_Status"]=='Y']

loan_approved_nse=len(loan4.index)
print(loan_approved_nse)

percentage_se=(loan_approved_se/6.14)

percentage_nse=(loan_approved_nse/6.14)
print(percentage_nse)

print(percentage_se)

loan_term = banks['Loan_Amount_Term'].apply(lambda x: x/12)

big_loan_term=len(banks[banks['Loan_Amount_Term']>=300])
print(big_loan_term)


loan_groupby=banks.groupby('Loan_Status')

print(loan_groupby)

loan_groupby=loan_groupby[['ApplicantIncome', 'Credit_History']]

mean_values=loan_groupby.agg(np.mean)

print(mean_values)




