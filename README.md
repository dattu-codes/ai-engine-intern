# Mini Workflow Engine — AI Engineering Internship Assignment

This repository contains a minimal workflow/graph engine implemented using Python and FastAPI, created as part of the AI Engineering Internship assignment.

The project demonstrates:

- Clean and modular API design
- Asynchronous workflow execution
- Graph-based execution model (nodes, edges, state transitions)
- Branching and looping via `state["next"]`
- A complete example workflow: Code Review Mini-Agent


## Features

### Workflow Engine
- Nodes: Python functions that operate on shared state
- Edges: Define execution flow between nodes
- State: Dictionary passed and updated throughout execution
- Branching: Nodes may override the next step using `state["next"]`
- Looping: Nodes can trigger re-execution until a condition is satisfied
- Asynchronous Execution: Workflows run using `asyncio.create_task`

### Code Review Workflow (Rule-Based)
A simple rule-based agent that performs the following steps:

1. Extract functions from code  
2. Compute basic complexity  
3. Detect issues such as debug prints or TODO comments  
4. Suggest improvements  
5. Loop until `quality_score >= threshold`

This workflow does not use machine learning and is entirely rule-based.


## Project Structure

- **ai-engine-intern/**
  - **app/**
    - **engine/**
      - `graph.py` — Graph and Node classes
      - `runner.py` — Async workflow runner
      - `registry.py` — Optional registry for node functions
    - **workflows/**
      - `code_review.py` — Code review workflow implementation
    - **models/**
      - `schemas.py` — Pydantic request/response models
    - `db.py` — In-memory GraphStore and RunStore
    - `main.py` — FastAPI routes and application
- `requirements.txt`
- `.gitignore`
- `README.md`
