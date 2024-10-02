import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from langserve import add_routes

from src.base.llm_model import get_hf_llm
from src.rag.main import build_rag_chain, Input_QA, Output_QA

os.environ["TOKENIZERS_PARALLELISM"] = "false"

llm = get_hf_llm(temperature=0.8)
genai_docs = "./data_source/generative_ai"

genai_chain = build_rag_chain(llm, data_dir=genai_docs, data_type="pdf")


app = FastAPI(
    title="LangChain Server",
    version=1.0,
    description="A simple API server using Langchain's Runnable interfaces"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_headers=["*"],
    allow_methods=["*"],
    expose_headers=["*"],
)


@app.get("/check")
async def check():
    return {"status": "ok"}

@app.post("/generative_ai", response_model=Output_QA)
async def generative_ai(inputs: Input_QA):
    answer = genai_chain.invoke(inputs.question)
    return {"answer": answer}


add_routes(app,
           genai_chain,
           playground_type="default",
           path="/generative_ai")