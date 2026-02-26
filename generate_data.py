import pandas as pd
import numpy as np

def generate_fintech_logs(n=1000):
    data = []
    for _ in range(n):
        freq = np.random.randint(1, 15)
        payload = np.random.randint(100, 500)
        hour = np.random.randint(9, 17) 
        label = 0 
        if np.random.random() > 0.90:
            freq = np.random.randint(80, 200)   
            payload = np.random.randint(2000, 5000) 
            hour = np.random.randint(0, 5)      
            label = 1 
        data.append([freq, payload, hour, label])
    
    df = pd.DataFrame(data, columns=['req_freq', 'payload_size', 'hour', 'is_anomaly'])
    df.to_csv('training_data.csv', index=False)
    print("✅ training_data.csv created.")

generate_fintech_logs()
