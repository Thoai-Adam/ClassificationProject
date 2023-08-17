import os
import pandas as pd

def drop_columns(df):
    columns_to_drop = ['Unnamed: 0', 'payment_type_id', 'internet_service_type_id', 'contract_type_id', 'customer_id']
    df = df.drop(columns=columns_to_drop)
    return df






def change_dtype(df):
    df.total_charges = df.total_charges.replace(' ', 0)
    df.total_charges = df.total_charges.astype(float)
    return df

def impute_mode(train, validate, test):
    imputer = SimpleImputer(fill_value= 'unknown', strategy='constant')
    train[['churn']] = imputer.fit_transform(train[['churn']])
    validate[['churn']] = imputer.transform(validate[['churn']])
    test[['churn']] = imputer.transform(test[['churn']])
    return train, validate, test