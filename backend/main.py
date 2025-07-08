
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from agent import run_agent

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/search")
def search(from_city: str = Query(...), to_city: str = Query(...), date: str = Query(...)):
    query = f"Busca opciones de transporte desde {from_city} a {to_city} el {date}."
    return {"result": run_agent(query)}
