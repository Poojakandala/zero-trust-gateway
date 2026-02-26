from fastapi import FastAPI, Request, Depends, HTTPException
from .auth import verify_token
from .risk_engine import RiskEngine
from .database import log_transaction
import time
import redis

app = FastAPI(title="Zero Trust Risk Gateway")

# Redis connection
r = redis.Redis(host='redis', port=6379, decode_responses=True)

engine = RiskEngine()


@app.middleware("http")
async def zero_trust_guard(request: Request, call_next):

    # 1. Rate Limiting
    client_ip = request.client.host
    count = r.incr(client_ip)
    if count == 1:
        r.expire(client_ip, 60)

    if count > 100:
        return HTTPException(status_code=429, detail="Rate limit exceeded")

    # 2. Feature Extraction
    features = {
        "freq": count,
        "path_depth": len(request.url.path.split("/")),
        "hour": time.localtime().tm_hour
    }

    # 3. AI Risk Score
    risk_score = engine.calculate_score(features)

    if risk_score > 0.8:
        log_transaction(client_ip, risk_score, "BLOCKED")
        return HTTPException(
            status_code=403,
            detail={"error": "Security Risk Too High", "score": risk_score}
        )

    # 4. Allow Request
    response = await call_next(request)
    response.headers["X-Risk-Score"] = str(risk_score)
    log_transaction(client_ip, risk_score, "ALLOWED")
    return response


# Protected API Endpoint
@app.get("/secure-data")
async def secure_api(token: str = Depends(verify_token)):
    return {"status": "Access Granted", "message": "Secure Data Accessed"}
