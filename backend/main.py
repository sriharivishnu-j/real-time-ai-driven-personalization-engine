from fastapi import FastAPI, HTTPException
import logging

app = FastAPI()

logger = logging.getLogger("uvicorn")

@app.get("/personalize")
async def personalize(user_id: int):
    try:
        # Simulate AI-driven personalization logic
        logger.info(f"Fetching personalization for user {user_id}")
        personalized_data = {"user_id": user_id, "recommendations": ["item1", "item2"]}
        return personalized_data
    except Exception as e:
        logger.error(f"Error in personalization: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")