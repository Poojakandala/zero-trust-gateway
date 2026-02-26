import requests
import time
import random

# Make sure your Gateway is running on Port 8000!
GATEWAY_URL = "http://localhost:8000/process-transaction"

def send_request(mode="safe"):
    headers = {"Authorization": "Bearer MOCK_TOKEN_XYZ"}
    
    if mode == "safe":
        payload = {"amount": random.randint(10, 100), "user_id": "user_123", "hour": 14}
        delay = 1 
    else:
        payload = {"amount": 9999, "user_id": "attacker_666", "hour": 2}
        delay = 0.2 

    try:
        # This sends the data to your FastAPI Gateway
        response = requests.post(GATEWAY_URL, json=payload, headers=headers)
        print(f"[{mode.upper()}] Status: {response.status_code} | Risk: {response.json().get('risk_score', 'N/A')}")
    except Exception as e:
        print(f"❌ Connection Failed: Is your Gateway (Terminal 1) running?")

    time.sleep(delay)

if __name__ == "__main__":
    print("🚀 Starting Demo Traffic... Watch your Dashboard!")
    
    print("\n--- Sending Normal Traffic ---")
    for _ in range(5):
        send_request("safe")
    
    print("\n🚨 INITIATING ATTACK...")
    for _ in range(15):
        send_request("attack")