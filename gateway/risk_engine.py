import joblib
import pandas as pd

class RiskEngine:
    def __init__(self, model_path="model.pkl"):
        # Load your pre-trained Isolation Forest or Random Forest
        try:
            self.model = joblib.load(model_path)
        except:
            self.model = None

    def calculate_score(self, features: dict):
        """
        Features: {'req_freq': 10, 'payload_size': 1024, 'hour': 14}
        Returns: Float (0.0 to 1.0)
        """
        if not self.model:
            return 0.5 # Default neutral risk if model is missing
            
        df = pd.DataFrame([features])
        # Model returns -1 for anomaly, 1 for normal
        prediction = self.model.predict(df)[0]
        confidence = self.model.decision_function(df)[0]
        
        # Convert to 0-1 scale where 1 is high risk
        risk_score = 1 - ((confidence + 0.5) / 1.0) 
        return max(0, min(1, risk_score))