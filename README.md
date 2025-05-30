# 🔍 AI-Powered Port Scanner

An AI-enhanced port scanner that scans common ports on a given IP address, identifies open ports and their services, and uses a machine learning model to assign risk levels based on service type and port number.

---

## 📌 Features

- 🔎 Scans common TCP ports and detects open ones
- 🧠 Uses a trained ML model (Random Forest) to assign a **risk level** (Low/Medium/High)
- 🗂️ Outputs readable scan reports
- 💡 Teaches fundamentals of port scanning and basic threat modeling
- 📁 Beginner-friendly folder and file structure

---

## 🧠 How It Works

1. The scanner runs a basic TCP port scan on predefined common ports (e.g., 22, 80, 443).
2. It uses a machine learning model trained on synthetic data (`train_model.py`) to assign risk ratings.
3. Outputs scan results with human-readable risk levels.

---

## ⚙️ Tech Stack

- Python 3
- `socket` for port scanning
- `scikit-learn` + `joblib` for machine learning
- `nmap` (optional) for advanced scanning
- JSON for storing and using risk rules

---

## 📁 Project Structure
<pre> AI-Port-Scanner/ │ ├── README.md ← Project overview ├── requirements.txt ← Python dependencies │ ├── ai_model/ │ ├── train_model.py ← ML training script │ └── model.pkl ← Trained ML model (auto-generated) │ ├── scanner/ │ └── port_scanner.py ← Main port scanning script │ ├── utils/ │ └── risk_levels.json ← Risk level definitions │ ├── reports/ │ └── sample_scan_report.txt← Sample scan result </pre>

