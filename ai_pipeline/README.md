# AI Pipeline

This module handles the AI-driven decision-making using LangChain and OpenAI.

## Setup

Ensure you have set your OpenAI API key in the environment.

## Usage

```python
from langchain_agent import DecisionAgent

agent = DecisionAgent(api_key="your-openai-api-key")
result = agent.make_decision("Provide input data here")
```
