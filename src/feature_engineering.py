
import pandas as pd
import numpy as np

def create_features(customers):
    
    # Encode states as numbers
    customers["state_code"] = customers["customer_state"].astype("category").cat.codes

    # Fake churn logic (for learning purpose)
    # Assume some states have higher churn
    customers["churn"] = np.where(customers["state_code"] % 2 == 0, 1, 0)

    # Keep useful columns
    df = customers[[
        "customer_unique_id",
        "state_code",
        "churn"
    ]]

    return df

