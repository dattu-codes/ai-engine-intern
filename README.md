AI Engine Intern – Workflow Execution API

A lightweight workflow engine built using FastAPI that executes AI-driven tasks through a modular and extensible pipeline. This project demonstrates how to build, register, and run workflows programmatically using a clean API structure.

Tech Stack

Python 3.10+

FastAPI

Pydantic

Uvicorn

Custom Workflow Engine Core

Project Structure

ai_engine_intern/
app/
main.py – FastAPI app entrypoint
router.py – API routes
workflow_registry.py – Registers workflows
tasks_manager.py – Task execution manager
workflows/
example_workflow.py – Sample workflow
steps/ – Individual workflow steps
requirements.txt
README.md

Running the Application

Create virtual environment
python -m venv venv
source venv/bin/activate (Linux/Mac)
venv\Scripts\activate (Windows)

Install dependencies
pip install -r requirements.txt

Start server
uvicorn ai_engine_intern.app.main:app --reload

Open API docs
http://127.0.0.1:8000/docs

Example: Running a Workflow

Send a POST request:

POST /run-workflow
{
"workflow_name": "example_workflow",
"input": {
"text": "Hello AI Engine"
}
}

Features

Easy workflow registration

Modular step-based design

FastAPI-powered clean API

Extensible for ML/AI task orchestration

License

MIT License

Author

Dattatreya Teella
