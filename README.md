# AI-Powered Port Scanner

An intelligent port scanning tool that not only scans for open ports but also analyzes them using machine learning to assign risk scores. Built for aspiring cybersecurity professionals and ethical hackers, this project demonstrates practical skills in network scanning, threat analysis, and AI-driven risk assessment.

---

## 🔍 Features

- **Multi-threaded Port Scanning:** Quickly scans target IPs for open ports.
- **Service Detection:** Identifies services running on open ports.
- **Feature Extraction:** Gathers 10+ characteristics per port (e.g., banner data, known vulnerabilities, common usage).
- **ML-Based Risk Scoring:** Trained machine learning model predicts risk level (Low, Medium, High) for each open port.
- **JSON Output:** Clean output with port number, service name, and risk score.

---

## 📁 Project Structure

```
AI-Port-Scanner/
├── ai_model/
│   └── train_model.py            # Script to train ML model on labeled port data
├── scanner/
│   └── port_scanner.py           # Main scanning script with risk scoring
├── utils/
│   ├── feature_extractor.py      # Extracts features per port for ML input
│   └── risk_levels.json          # Maps port ranges or services to baseline risk levels
├── README.md                     # Project documentation (this file)
├── requirements.txt              # Dependencies list
└── .gitignore                    # Git ignore rules
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Kapriatti/AI-Port-Scanner.git
cd AI-Port-Scanner
```

### 2. (Optional) Create and Activate a Virtual Environment

```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On Mac/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Train the Machine Learning Model

```bash
python ai_model/train_model.py
```

### 5. Run the Port Scanner

```bash
python scanner/port_scanner.py
```

---

## 📌 Example Output

```json
[
  {
    "ip": "192.168.1.10",
    "port": 22,
    "service": "ssh",
    "features": {...},
    "risk_score": "High"
  },
  {
    "ip": "192.168.1.10",
    "port": 80,
    "service": "http",
    "features": {...},
    "risk_score": "Low"
  }
]
```

---

## 🧠 ML Model Details

- **Model Type:** RandomForestClassifier (or similar)
- **Training Data:** Simulated ports with labeled risk levels
- **Input Features:** Port number, service name, known CVEs, encryption usage, popularity, etc.
- **Output:** Predicted risk score (Low, Medium, High)

---

## 🛡️ Use Cases

- Educational project to demonstrate ML + cybersecurity
- Internal network vulnerability scanning
- SOC analyst training

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 👤 Author

**Kapriatti**  
Cybersecurity Student | Developer | Builder  
GitHub: [Kapriatti](https://github.com/Kapriatti)
