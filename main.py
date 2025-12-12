import asyncio
from fastapi import FastAPI, HTTPException
from app.models.schemas import CreateGraphRequest, RunGraphRequest
from app.db import GraphStore, RunStore
from app.workflows.code_review import build_code_review_graph
from app.engine.graph import Graph
from app.engine.runner import Runner

# FastAPI app
app = FastAPI(title="Mini Workflow Engine")

# In-memory stores
graph_store = GraphStore()
run_store = RunStore()
runner = Runner(graph_store, run_store)


@app.post("/graph/create")
async def create_graph(req: CreateGraphRequest):
    """
    Create a graph from a preset or a provided definition.
    """
    if req.preset == "code_review":
        graph = build_code_review_graph()
    elif req.graph_def:
        graph = Graph.from_dict(req.graph_def)
    else:
        raise HTTPException(status_code=400, detail="provide preset or graph_def")

    graph_id = graph_store.save_graph(graph)
    return {"graph_id": graph_id}


@app.post("/graph/run")
async def run_graph(req: RunGraphRequest):
    """
    Start a run and schedule it asynchronously.
    """
    graph = graph_store.get_graph(req.graph_id)
    if graph is None:
        raise HTTPException(status_code=404, detail="graph not found")

    run_id = run_store.create_run(req.graph_id, req.initial_state)

    # Schedule async execution
    asyncio.create_task(runner.run(run_id))

    return {"run_id": run_id}


@app.get("/graph/state/{run_id}")
async def get_state(run_id: str):
    """
    Get the state of a workflow run.
    """
    run = run_store.get_run(run_id)
    if run is None:
        raise HTTPException(status_code=404, detail="run not found")

    return {
        "run_id": run_id,
        "state": run["state"],
        "logs": run["logs"],
        "status": run["status"]
    }
