from fastapi import FastAPI, HTTPException
from loguru import logger

app = FastAPI()

@app.get("/personalize")
async def personalize(user_id: int):
    try:
        # Placeholder for personalization logic
        logger.info(f"Personalizing content for user {user_id}")
        return {"message": "Personalization successful"}
    except Exception as e:
        logger.error(f"Error personalizing content: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")