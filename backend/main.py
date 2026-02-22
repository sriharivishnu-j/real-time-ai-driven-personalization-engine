from fastapi import FastAPI, HTTPException
import logging
from langchain import LangChain
from openai import OpenAI

app = FastAPI()
lang_chain = LangChain()
openai = OpenAI()

logging.basicConfig(level=logging.INFO)

@app.get("/personalize")
async def personalize(user_id: str):
    try:
        # Example integration with LangChain and OpenAI
        decision = lang_chain.make_decision(user_id)
        personalized_response = openai.generate_response(decision)
        return {"response": personalized_response}
    except Exception as e:
        logging.error(f"Error during personalization: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
