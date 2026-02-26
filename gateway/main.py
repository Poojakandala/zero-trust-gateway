from fastapi import FastAPI, Request, Depends
from .auth import verify_token
from .risk_engine import RiskEngine
from .database import log_transaction
import time
import redis

app = FastAPI(title="Zero Trust Risk Gateway")
r = redis.Redis(host='redis', port=6379, decode_responses=True)
engine = RiskEngine()

@app.middleware("http")
async def zero_trust_guard(request: Request, call_next):
    # 1. Rate Limiting (Redis)
    client_ip = request.client.host
    count = r.incr(client_ip)
    if count == 1: r.expire(client_ip, 60)
    
    if count > 100: # Threshold
        return {"error": "Rate limit exceeded"}, 429

    # 2. Extract Behavioral Features for AI
    features = {
        "freq": count,
        "path_depth": len(request.url.path.split("/")),
        "hour": time.localtime().tm_hour
    }

    # 3. AI Risk Scoring
    risk_score = engine.calculate_score(features)
    
    if risk_score > 0.8: # Strict Policy
        log_transaction(client_ip, risk_score, "BLOCKED")
        return {"error": "Security Risk Too High", "score": risk_score}, 403

    # 4. Success - Proceed and Log
    response = await call_next(request)
    log_transaction(client_ip, risk_score, "ALLOWED")
    return response