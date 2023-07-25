# Test_files
Brief Summary

        
The process
Funtions		
Namsor_api_calling: for calling the namsor API. It includes a GET request for receiving data from the Namsor site. It is called by the main function

Main function: 
It contains code for accessing the excel file containing the names; The name list is iterated through, and for each name the api calling function is called to receive the diaspora information from the Namsor repository. The Ethnicity and EthnicityAlt values are extracted and saved as variable which are eventually stored into dataframe and saved as a file. This file is eventually converted into excel format.

Output files
Updated_List.xlsx
Output/forename_surname.txt
![image](https://github.com/Realhbee/Test_files/assets/105416839/142853f6-31e8-4f5c-9818-8c5083f86c95)
