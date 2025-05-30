AI-Powered Port Scanner

A smart and enhanced network port scanner that combines traditional port scanning techniques with machine learning-based risk scoring. This tool scans specified IP addresses and port ranges, identifies open ports and services, extracts multiple features per port, and predicts a risk level with brief descriptions — helping you prioritize security efforts efficiently.


Features

Customizable IP address and port range scanning

Multi-feature extraction per port (10+ features for detailed analysis)

Machine learning-based risk scoring trained on known vulnerabilities and common port risks

Human-readable output with open port info and risk levels

Modular, easy-to-extend Python codebase


Why This Scanner is Unique

Traditional port scanners simply report whether ports are open or closed. This project adds an AI-powered layer that assesses potential security risks for each detected open port using a trained machine learning model. This helps you:

Quickly identify ports that may require urgent attention

Understand potential risk levels with concise explanations

Enhance your network security auditing beyond basic port detection


Installation

Clone the repository:

git clone https://github.com/Kapriatti/AI-Port-Scanner.git
cd AI-Port-Scanner

(Optional) Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate       # On Windows: venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt


Usage

Run the port scanner module:
 
python -m scanner.port_scanner

You will be prompted to enter:

The IP address or hostname to scan

The port range (e.g., 20-100)

Example output:

[OPEN] Port 53 (domain) → Risk Level: 2 - Medium risk: Moderately sensitive port, sometimes exploited.
[OPEN] Port 80 (http) → Risk Level: 2 - Medium risk: Moderately sensitive port, sometimes exploited.

Project Structure

AI-Port-Scanner/
├── ai_model/
│   └── train_model.py          # Script to train the machine learning model
├── scanner/
│   └── port_scanner.py         # Main port scanner script
├── utils/
│   ├── feature_extractor.py    # Feature extraction logic
│   └── risk_levels.json        # Risk level descriptions and explanations
├── requirements.txt            # Python dependencies
├── README.md
└── .gitignore


