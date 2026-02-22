from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import logging

app = FastAPI()

logging.basicConfig(level=logging.INFO)

class PersonalizationRequest(BaseModel):
    user_id: str

@app.post("/personalization")
async def get_personalization(request: PersonalizationRequest):
    try:
        # Assume some AI processing logic here
        personalized_content = f"Hello, {request.user_id}! This is your personalized content."
        return {"content": personalized_content}
    except Exception as e:
        logging.error(f"Error processing personalization: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")