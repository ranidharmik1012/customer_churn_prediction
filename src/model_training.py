# Used to split data into training and testing sets
from sklearn.model_selection import train_test_split

# Random Forest model for classification

from sklearn.ensemble import RandomForestClassifier

# Used to evaluate model performance (accuracy, precision, recall, F1-score)

from sklearn.metrics import classification_report

def train_model(df):

# Select input feature (X) and target label (y)
    X = df[["state_code"]]
    y = df["churn"]

# Split data into training (80%) and testing (20%)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

# Create Random Forest model with 100 trees
    model = RandomForestClassifier(n_estimators=100)
    
    # Train the model using training data
    model.fit(X_train, y_train)

# Predict churn on test data
    preds = model.predict(X_test)

# Print model performance metrics
    print("Model Performance:")
    print(classification_report(y_test, preds))

# Return trained model
    return model
    return model
