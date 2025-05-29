from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from retriever_agent import query_index
from language_agent import summarize_chunks

app = FastAPI(title="Finance Assistant Orchestrator")

class QueryRequest(BaseModel):
    query: str

class QueryResponse(BaseModel):
    summary: str

@app.post("/brief", response_model=QueryResponse)
def get_market_brief(request: QueryRequest):
    try:
        chunks = query_index(request.query)
        summary = summarize_chunks(chunks)
        return QueryResponse(summary=summary)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
