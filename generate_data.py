import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

def generate_and_train():
    print("Step 1: Generating Synthetic FinTech Data...")
    data = []
    for _ in range(2000):
        # Normal Traffic
        freq = np.random.randint(1, 15)
        payload = np.random.randint(100, 500)
        hour = np.random.randint(9, 17) 
        label = 0 
        
        # Inject Attacks (10% of data)
        if np.random.random() > 0.90:
            freq = np.random.randint(80, 200)   
            payload = np.random.randint(2000, 5000) 
            hour = np.random.randint(0, 5)      
            label = 1 
            
        data.append([freq, payload, hour, label])
    
    df = pd.DataFrame(data, columns=['req_freq', 'payload_size', 'hour', 'is_anomaly'])
    df.to_csv('training_data.csv', index=False)
    print("✅ training_data.csv created.")

    # Step 2: Training
    print("Step 2: Training AI Model...")
    X = df[['req_freq', 'payload_size', 'hour']]
    y = df['is_anomaly']
    
    model = RandomForestClassifier(n_estimators=100)
    model.fit(X, y)
    
    # Step 3: Save Model
    # Create gateway folder if it doesn't exist
    if not os.path.exists('gateway'):
        os.makedirs('gateway')
        
    joblib.dump(model, 'gateway/model.pkl')
    print("✅ gateway/model.pkl created successfully!")

if __name__ == "__main__":
    # This MUST match the function name defined above
    generate_and_train()