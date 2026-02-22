from fastapi import FastAPI, HTTPException
import logging

app = FastAPI()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.get("/personalize")
async def personalize(user_id: int):
    try:
        logger.info(f"Received personalization request for user {user_id}")
        # Placeholder for personalization logic
        return {"message": "Personalization successful", "user_id": user_id}
    except Exception as e:
        logger.error(f"Error in personalization: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
