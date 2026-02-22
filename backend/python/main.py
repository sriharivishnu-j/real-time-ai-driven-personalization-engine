from fastapi import FastAPI, HTTPException
import logging

app = FastAPI()

logging.basicConfig(level=logging.INFO)

@app.get("/personalize/{user_id}")
async def personalize(user_id: str):
    try:
        # Placeholder for personalization logic
        logging.info(f"Fetching personalization for user: {user_id}")
        return {"message": f"Personalization result for {user_id}"}
    except Exception as e:
        logging.error(f"Error in personalization: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")