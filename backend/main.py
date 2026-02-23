from fastapi import FastAPI, HTTPException
import logging

app = FastAPI()

logging.basicConfig(level=logging.INFO)

@app.get("/api/personalization")
async def get_personalization():
    try:
        # Simulate interaction processing
        logging.info("Processing personalization request")
        return {"message": "Personalization data"}
    except Exception as e:
        logging.error(f"Error processing request: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")