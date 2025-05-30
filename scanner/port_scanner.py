import socket
import joblib
import os
import json
from utils.feature_extractor import extract_features_for_port

# Path to the trained model
MODEL_PATH = os.path.join(os.path.dirname(__file__), "..", "ai_model", "model.pkl")

# Path to risk_levels.json
RISK_LEVELS_PATH = os.path.join(os.path.dirname(__file__), "..", "utils", "risk_levels.json")

def load_model(path):
    return joblib.load(path)

def load_risk_levels():
    with open(RISK_LEVELS_PATH, "r") as f:
        return json.load(f)

def scan_target(target, ports, model, risk_descriptions):
    print(f"\nScanning {target}...\n")
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target, port))
            if result == 0:
                service = socket.getservbyport(port, "tcp") if port in range(1, 65536) else "unknown"
                features = extract_features_for_port(port, service)
                risk = int(model.predict([features])[0])
                description = risk_descriptions.get(str(risk), "No description available.")
                print(f"[OPEN] Port {port} ({service}) → Risk Level: {risk} - {description}")
            sock.close()
        except Exception as e:
            print(f"Error scanning port {port}: {e}")

def main():
    target = input("Enter the IP address or hostname to scan: ")
    port_range = input("Enter port range (e.g., 20-100): ")

    try:
        start_port, end_port = map(int, port_range.split("-"))
        ports = range(start_port, end_port + 1)
    except:
        print("Invalid port range. Use format like 20-100.")
        return

    model = load_model(MODEL_PATH)
    risk_descriptions = load_risk_levels()
    scan_target(target, ports, model, risk_descriptions)

if __name__ == "__main__":
    main()
