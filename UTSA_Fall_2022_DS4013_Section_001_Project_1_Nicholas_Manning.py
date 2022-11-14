#!/usr/bin/env python
# coding: utf-8

# In[47]:


# UTSA - Fall 2022 - DS4013 - Section 001 - Project 1 - Written by NICHOLAS MANNING


# In[48]:


# Section 1


# In[49]:


# Include a prompt to the user to enter the number of counties.
# Won't exceed 10 counties.


# In[50]:


# This function is the code for the input list of county results
# It will take input from the user for: amount of counties, names of the counties, and the number of positive test results.


def county_results_info():
    
    global county_names
    
    county_names = {}
    
    global posi_test_cnt 
    
    posi_test_cnt = {}
    
    global county_cnt 
    
    global names
    
    county_cnt = int(input("Please, enter the number of counties: \n"))
    
    print("List of County Results: \n")
    
    while len(county_names) < county_cnt:
        
        names = input("\nPlease, enter the county name: \n\n")
        
        posi_test_cnt = int(input("\nPlease enter the number of positive tests: \n\n"))
        
        county_names[names] = posi_test_cnt
        
    print("\nList of County Results: \n")
    
    for key, value in county_names.items():
        
        print(key, "County positive tests: ", value)
        
        print()


# In[51]:


# This cell is the code for the modifying results option
# The function will prompt the user with which county to change by name
# it will then ask for the new number of positive test results from the user
# The user inputs the new amount and the program will print out the new list of results
# If the user inputs an invalid county, it will ask for a valid county name.

def modify_results():
    
    global county_names
    
    global posi_test_cnt
    
    global names
    
    county_name_for_change = input("Please provide the name of the county: ")
    
    print()
    
    if county_name_for_change not in county_names:
        
        print("Invalid County, please resubmit: ")
        
    else:
        
        new_test_results = int(input("\nPlease provide the new test results: "))
        
        print()
        
        posi_test_cnt = new_test_results
        
        county_names[county_name_for_change] = posi_test_cnt
        
        for key, value in county_names.items():
        
            print(key, "County's results are: ", value)
        
            print()


# In[52]:


# Section 2


# In[53]:


# The program presents a menu to the user, with 4 options.
#
# List County Results
# Report of Status
# Modify County Results
# Exit Program


# In[54]:


# This cell is the code for displaying the status of each county
# The status is based on the amount of positive test results
# If more than 300, the status of the county will print red
# If between 100 and 299, the status of the county will print yellow
# If less than 100, the status of the county will print green

def status_report():
    
    global posi_test_cnt
    
    global county_names
    
    print("\nReport of Status\n")
    
    status_green = "Green"
    
    status_red = "Red"
    
    status_yellow = "Yellow"
    
    for key, value in county_names.items():
        
        county_names.get(value)
        
        if value > 300:
        
            print(f"{key}: {status_red}")
            
            print()
        
        elif value >= 100 and value <= 299:
        
            print(f"{key}: {status_yellow}")
            
            print()
        
        else:
        
            print(f"{key}: {status_green}")
            
            print()


# In[55]:


# This cell is the code for the menu prompt and where the user will select which option
# There are 4 options: modify, input list results, display status, and exit
# If the user inputs a number out of the range (1, 4) and error will occur and the user will have to resubmit a new number

def user_menu():
    
    user_option = int(input("Select an Option: \n\n1 - List County Results\n2 - Report of Status\n3 - Modify County Results\n4 - Exit Program \n\n"))
    
    if user_option == 1 or 2 or 3 or 4:
    
        if user_option == 1:

            county_results_info()
            
            user_menu()

        if user_option == 2:

            status_report()
            
            user_menu()

        if user_option == 3:

            modify_results()
            
            user_menu()

        if user_option > 4 or user_option < 1:
            
            print("\nValue is out of range, please resubmit: ")
            
            user_menu()
            
        if user_option == 4:

            print('\nThank you. This program is brought to by Python Expert: NICHOLAS MANNING.')


# In[56]:


if __name__ == '__main__':
    
    user_menu()





