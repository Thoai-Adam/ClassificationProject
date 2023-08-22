import pandas as pd

def acquire_telco_data():

    url = 'telco.csv'
    df = pd.read_csv(url)
    return df

def clean_telco_data(df):

    # Drop unnecessary columns
    columns_to_drop = ['Unnamed: 0', 'payment_type_id', 'internet_service_type_id', 'contract_type_id', 'customer_id']
    df = df.drop(columns=[columns_to_drop])
    df_cleaned = df_cleaned.dropna()
    return df

    # Convert data types if needed
    df['total_charges'].str.replace(',', '')
    df['total_charges'].str.replace(' ', '0')
    pd.to_numeric(df['total_charges'], errors='coerce')
    return df_cleaned

