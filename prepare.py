import pandas as pd
from sklearn.model_selection import train_test_split

def prepare_telco_data(df):
    numeric_columns = []

    for col in df.columns:
        if pd.api.types.is_numeric_dtype(df[col]):
            numeric_columns.append(col)

    print(numeric_columns)

    # Select features and target variable
    # Use .describe with object columns with the normalized value count 
    # i did this to see the distribution of unique values
    # and to understand the frequency and proportion of different values in the categorical columns

    obj_cols = df.columns[[df[col].dtype == 'O' for col in df.columns]]  #'O' is for object
    for col in obj_cols:
        print(df[col].value_counts())
        print(df[col].value_counts(normalize=True, dropna=False))
        print('----------------------')
        
    #i want 20% test, 80% train-validate
    #of the 80% train_validate, i have 30% validate, and 70% train
    seed = 42 #this is a random state (number generator) so anyone can take my code and produce the same result 
    train, test = train_test_split(df, test_size=.2, random_state=seed, stratify=df.churn) 
    #stratifying the churn will maintain the same class distribution in both training and test dataset
    #after i run this code, i will have two separate datasets: train and test, subset of df. 


    train, validate = train_test_split(train, test_size=.3, random_state=seed, stratify=train.churn)
    #this code will further split the train subset into train and validate with 30% validate and 70% train
    
    # after the split i want to validate my train so that my model perform well to unseen data
    # validate will prevent overfitting, be able to experience different hyperparameter, 
    print(f'train -> {train.shape}')
    print(f'validate -> {validate.shape}')
    print(f'test -> {test.shape}')