from fastapi import FastAPI
from pydantic import BaseModel, Field
from starlette.concurrency import run_in_threadpool

from llm_port import get_llm

app = FastAPI()


class AskRequest(BaseModel):
    user_message: str = Field(min_length=1)

class ModelResponse(BaseModel):
    response: str = Field(description="LLM Response for user message")


@app.post("/ask", response_model=ModelResponse)
async def ask_model(ask: AskRequest) -> ModelResponse:
    response = await run_in_threadpool(lambda: get_llm().generate(ask.user_message))
    return ModelResponse(response=response)
