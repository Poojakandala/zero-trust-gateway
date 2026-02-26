import requests
import time
import random

GATEWAY_URL = "http://localhost:8000/secure-data"
HEADERS = {"Authorization": "Bearer MOCK_TOKEN_XYZ"}

def send_request(mode="safe"):
    
    if mode == "safe":
        delay = random.uniform(1, 2)
    else:
        delay = 0.1  # attack traffic = high frequency

    try:
        response = requests.get(GATEWAY_URL, headers=HEADERS)

        print(f"[{mode.upper()}] Status: {response.status_code} | "
              f"Risk Score: {response.headers.get('X-Risk-Score', 'N/A')}")

    except Exception as e:
        print(f"Connection Failed: {e}")

    time.sleep(delay)


if __name__ == "__main__":
    print("Sending SAFE traffic...\n")
    for _ in range(5):
        send_request("safe")

    print("\nSending ATTACK traffic...\n")
    for _ in range(50):
        send_request("attack")
