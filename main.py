from src.data_preprocessing import load_data
from src.feature_engineering import create_features
from src.model_training import train_model

def main():
    print("Project started")


    customers = load_data()
    print("Data loaded")

    df = create_features(customers)
    print("Feature engineering done")

    model = train_model(df)
    print("Model training done")

    print("Project completed successfully")

if __name__ == "__main__":   
    main()


    