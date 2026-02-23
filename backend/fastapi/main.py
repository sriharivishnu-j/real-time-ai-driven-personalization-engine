from fastapi import FastAPI
import logging

app = FastAPI()

logging.basicConfig(level=logging.INFO)

@app.get("/health")
async def health_check():
    logging.info("Health check endpoint called")
    return {"status": "healthy"}