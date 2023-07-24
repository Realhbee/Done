#Loading pandas 
import pandas as pd

#Importing the dataset
Test_file = pd.read_csv('BasicCompanyData-2023-07-01-part7_7.csv')

#Checking out the dataset
Test_file.head()

#Checking the columns of in the dataset
#list(Test_file)
Test_file.columns

#Filtering the dataset for Company category that is 'Private limited company'
Test1= filtered_Test_file = Test_file[Test_file['CompanyCategory']== 'Private Limited Company']
print("Test1")
print(Test1)

#Filtering the dataset for Company status that is 'Active'
Test2= filtered_Test_file = Test_file[Test_file['CompanyStatus']== 'Active']
print("Test2")
print(Test2)

#Filtering the dataset for Account category that is 'Small and Medium'
Test3= filtered_Test_file = Test_file[(Test_file['Accounts.AccountCategory']== 'SMALL') & (Test_file['Accounts.AccountCategory'] == 'MEDIUM')]
print("Test3")
print(Test3)

#Saving each of the data query to csv files
#Test1.to_csv('Test1.csv', index=False)
#Test2.to_csv('Test2.csv', index=False)
#Test3.to_csv('Test3.csv', index=False)