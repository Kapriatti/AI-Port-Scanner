import os
import joblib
from sklearn.ensemble import RandomForestClassifier
from utils.feature_extractor import extract_features_for_port

# Example training data (replace with real dataset)
# Ports and their known risk levels
train_ports = [21, 22, 23, 25, 53, 80, 110, 139, 443, 3389]
train_labels = [3, 1, 3, 2, 1, 2, 2, 3, 2, 3]  # Risk levels

def prepare_training_data(ports):
    X = [extract_features_for_port(port) for port in ports]
    return X

def train_and_save_model():
    X = prepare_training_data(train_ports)
    y = train_labels

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)

    # Save the model in the ai_model folder
    model_path = os.path.join(os.path.dirname(__file__), 'model.pkl')
    joblib.dump(model, model_path)
    print(f"Model trained and saved to {model_path}")

if __name__ == "__main__":
    train_and_save_model()
