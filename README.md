# 🔐 AI-Driven Zero Trust Risk Gateway

---

## 📌 Project Overview

In modern **FinTech ecosystems**, traditional perimeter security is no longer enough.  
If one internal service is compromised, attackers can move laterally and drain wallets or steal sensitive data.

This project implements a **Zero Trust Architecture** using an **AI-Driven Security Gateway**.

Every API request — even from *trusted internal services* — is evaluated in real-time using Machine Learning.

---

## 🚀 Core Innovation

### 🧠 Context-Aware AI
- Uses **Machine Learning models (Scikit-learn)**
- Detects anomalies in:
  - Request frequency  
  - Payload behavior  
  - Transaction timing  
- Classifies traffic as:
  - ✅ Safe  
  - ❌ Suspicious  

### ⚡ Real-Time Intervention
- High-risk API calls are **blocked before reaching backend services**
- Prevents lateral movement attacks

### 🔐 Zero Trust Logic
> **"Never Trust, Always Verify"**

Applied to **every single API request**

---

## 🏗 Technical Architecture

The system follows a **microservices-based architecture**:

### 1️⃣ Security Gateway (FastAPI)
- Entry point for all internal API traffic
- Intercepts every request

### 2️⃣ Identity Verification (PyJWT)
- Validates JWT tokens
- Checks expiration
- Ensures trusted issuer

### 3️⃣ AI Risk Engine (Scikit-learn)
- Pre-trained anomaly detection model
- Generates risk score between:
  - `0.0 → Safe`
  - `1.0 → Critical`

### 4️⃣ Rate Limiting (Redis)
- Monitors request frequency
- Prevents brute-force or flooding attacks

### 5️⃣ Audit Logging (SQLite)
- Stores:
  - Service name
  - Risk score
  - Decision (ALLOW / BLOCK)
  - Timestamp

### 6️⃣ Monitoring Dashboard (Streamlit)
- Real-time analytics
- Risk trend visualization
- Blocked vs Allowed statistics
- Service-level risk insights

---

## 🔄 How It Works (Flow)

1. Service sends API request  
2. Gateway intercepts request  
3. JWT token is verified  
4. Rate limiting check is applied  
5. AI model calculates risk score  
6. Policy engine decides:
   - ✅ Allow
   - ❌ Block  
7. Event is logged in database  
8. Dashboard updates in real-time  

---

## 🛡 Security Features

- Zero Trust enforcement
- AI-based anomaly detection
- Dynamic risk scoring
- Real-time blocking
- Service-level monitoring
- Containerized deployment (Docker)

---

## 🐳 Deployment

The system is containerized using **Docker**, enabling:

- Service isolation
- Easy scaling
- Real-world FinTech simulation

---

## 🎯 Impact

This solution enhances internal API security in FinTech systems by:

- Preventing lateral attacks
- Detecting abnormal service behavior
- Reducing insider threat risks
- Enforcing adaptive, intelligent access control

---

## 💡 Future Enhancements

- Behavioral profiling per service
- Advanced ML ensemble models
- SIEM integration
- Blockchain-based audit integrity

---
