
# 🛡️ AI-Driven Zero Trust Risk Gateway
**📌 Project Overview**
In modern FinTech ecosystems, traditional perimeter security is no longer enough. Once a single internal service is compromised, attackers can move laterally to drain wallets or steal data.

Our solution implements a Zero Trust Architecture using an AI-Driven Security Gateway. Every single request—even from "trusted" internal sources—is evaluated in real-time by a Machine Learning model that detects anomalies in request frequency, payload size, and transaction timing.

Core Innovation:
Context-Aware AI: Uses a Random Forest Classifier to identify "Safe" vs. "Attack" traffic patterns.

Real-Time Intervention: Automatically blocks high-risk requests before they reach the backend.

Zero Trust Logic: "Never Trust, Always Verify" applied to every API call.

**🏗️ Technical Architecture**
The system is built using a microservices approach:

Security Gateway (FastAPI): The entry point that intercepts all traffic.

Risk Engine (Scikit-Learn): A pre-trained ML model that scores every request from 0.0 (Safe) to 1.0 (Critical).

Stateful Rate Limiter (Redis): Tracks request bursts to prevent Brute Force and DDoS.

Audit Ledger (SQLite): A permanent, immutable record of all security decisions.

Live Threat Dashboard (Streamlit): Real-time visualization of network health and attack status.

**🛠️ Tech Stack**
- Language: Python 3.13

- Frameworks: FastAPI, Streamlit

- AI/ML: Scikit-Learn (Random Forest), Pandas, NumPy

- Database: Redis (Cache/Rate-Limiting), SQLite (Audit Logs)

- DevOps: Docker, Docker-Compose

**🚀 Installation & Setup**
1. Clone the Project & Install Dependencies
2. Train the AI Model
Before starting the gateway, you must generate the synthetic training data and train the brain:

This creates training_data.csv and gateway/model.pkl.

3. Run via Docker (Recommended)
4. Manual Execution (Without Docker)
Run these in 3 separate terminals:

- Gateway: python -m uvicorn gateway.main:app --port 8000

- Dashboard: streamlit run dashboard/dashboard.py

- Simulator: python simulate_traffic.py

📊 Evaluation Criteria for Judges
🔮 Future Scope
JWT Deep Inspection: Validating user identity claims within the gateway.

Biometric Integration: Triggering MFA (Multi-Factor Authentication) automatically when the AI detects a high risk score.

Graph Analysis: Using Graph Neural Networks to detect complex money-laundering paths.
