import os
import pandas as pd

def drop_columns(df):
    columns_to_drop = ['Unnamed: 0', 'payment_type_id', 'internet_service_type_id', 'contract_type_id', 'customer_id']
    df = df.drop(columns=columns_to_drop)
    return df