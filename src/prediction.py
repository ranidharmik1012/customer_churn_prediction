def generate_predictions(model, df):

    # Use the trained model to predict churn probability
    # predict_proba gives probability for each class (0 and 1)
    # [:, 1] selects the probability of churn (class = 1)

    df["churn_probability"] = model.predict_proba(
        df[["state_code"]]
    )[:, 1]

# Save the final results to a CSV file
    df.to_csv("outputs/predictions.csv", index=False)
