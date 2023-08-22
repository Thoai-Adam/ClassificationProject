import os
import pandas as pd
import acquire
import prepare


# Load the CSV data into a DataFrame
df = pd.read_csv("telco.csv")

# Clean the data: Remove rows with missing values
df = df.dropna()



# Save the cleaned and transformed data to a new CSV file
df.to_csv("cleaned_data.csv", index=False)

print("Data wrangling completed!")
