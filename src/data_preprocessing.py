import pandas as pd
#Creates a function named load_data

#Reads the CSV file that contains customer data and loads it into a DataFrame
def load_data():
    customers = pd.read_csv(r"C:\Users\DELL\OneDrive\Desktop\Projects\Customer churn prediction\Customer churn prediction Ecommerce\data\raw\olist_customers_dataset.csv")

#Sends the loaded data back so it can be used in other files.
    return customers



#The r means raw string, which avoids issues with backslashes (\) in Windows paths.