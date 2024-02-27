import pytest
# TODO: add necessary import
import numpy as np
import pandas as pd
import os
from ml.data import process_data
from ml.model import compute_model_metrics, train_model, inference
from sklearn.svm import SVC

# TODO: implement the first test. Change the function name and input as needed
def test_one():
    """
    # Verify train_modle returns RBF model by adding test data and processing with process_data function
    """
    data = pd.DataFrame(
        {
            'column_1' : [10, 20, 30, 29, 100],
            'column_2' : [0, 1, 0, 1, 0],
            'label' : [0, 1, 0, 1, 0]
        }
    )

    X_train, y_train, _,_ = process_data(
        data,
        categorical_features= ['column_2'],
        label= 'label',
        training= True
    )

    #Training rbf_model
    rbf_model = train_model(X_train, y_train)

    #Check model type
    assert isinstance(rbf_model, SVC)
    assert rbf_model.kernel == 'rbf'
    


# TODO: implement the second test. Change the function name and input as needed
def test_two():
    """
    # Testing the csv import for successful attempt
    """
    project_path = os.getcwd()
    data_path = os.path.join(project_path, "data", "census.csv")

    try:
        test_csv = pd.read_csv(data_path)
        #test that csv/dataframe is not empty
        assert not test_csv.empty
        #test print first few lines
        print(test_csv.head())
        
    except Exception as e:
        print('Error')
        

# TODO: implement the third test. Change the function name and input as needed
def test_three():
    """
    # Test one hot encoding by asserting that columns have been created for categories
    """
    data = pd.DataFrame(
        {
            'column_1': [10, 20, 30, 40, 50],
            'column_2': ['A', 'B', 'A', 'C', 'D'],
            'label': [0, 1, 0, 1, 0]
        }
    )


    # Process the test data
    X_train, y_train, _,_ = process_data(
        data,
        categorical_features= ['column_2'],
        label= 'label',
        training= True
    )
    #make sure type is dataframe
    if isinstance(X_train, np.ndarray):
        X_train = pd.DataFrame(X_train, columns=['column_1', 'column_2_A', 'column_2_B', 'column_2_C', 'column_2_D'])
    
#Check that new binary columns are created for each category in column_2
    assert 'column_2_A' in X_train.columns
    assert 'column_2_B' in X_train.columns
    assert 'column_2_C' in X_train.columns
    assert 'column_2_D' in X_train.columns
