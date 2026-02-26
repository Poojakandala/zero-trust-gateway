from fastapi import HTTPException, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

security = HTTPBearer()

# Temporary test token
TEST_TOKEN = "MOCK_TOKEN_XYZ"

def verify_token(auth: HTTPAuthorizationCredentials = Security(security)):
    token = auth.credentials

    # Allow test token for simulator
    if token == TEST_TOKEN:
        return {"user": "test_client", "scope": "full_access"}

    # Otherwise block
    raise HTTPException(status_code=401, detail="Invalid or missing token")
