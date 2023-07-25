# Test_files
**Brief Summary**

**The process**


# Task 1

The pandas library is used to create a data frame from the smallest company house data file

Pandas filter is use to filter the data frame based on the required columns 

The results are then save into csv files.



# Task 2
**Funtions**

Namsor_api_calling: for calling the namsor API. It includes a GET request for receiving data from the Namsor site. It is called by the main function

**Main function** 
It contains code for accessing the excel file containing the names; The name list is iterated through, and for each name the api calling function is called to receive the diaspora information from the Namsor repository. The Ethnicity and EthnicityAlt values are extracted and saved as variable which are eventually stored into dataframe and saved as a file. This file is eventually converted into excel format.

**Output files**
The ouput files are in xlsx format for the (First Name, Last Name, Ethnicity, Alternate Ethnicity) task and the txt format contains  each Full name  

Updated_List.xlsx

Output/forename_surname.txt

