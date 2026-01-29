import json
from utils.llm import call_llm


PYTHON_SYSTEM_DOC_PROMPT = """
You are generating developer documentation for a Python FastAPI backend.

Using this Python IR:

{python_ir}

Generate COMPLETE and CONCRETE documentation.

Do NOT use placeholders like step1, python_version, dependencies.

Infer realistic values.

Return ONLY JSON:

{{
 "introduction": "2-3 paragraph system overview",
 "architecture": "High level architecture explanation",
 "requirements": [
   "Python 3.10+",
   "fastapi",
   "uvicorn",
   "pydantic"
 ],
 "installation": [
   "python -m venv venv",
   "source venv/bin/activate",
   "pip install -r requirements.txt"
 ],
 "run_instructions": [
   "uvicorn main:app --reload",
   "Open http://127.0.0.1:8000/docs"
 ],
 "usage_examples": [
   "POST /tickets",
   "GET /tickets",
   "POST /comments"
 ]
}}
"""


def python_system_doc_node(state: dict):

    prompt = PYTHON_SYSTEM_DOC_PROMPT.format(
        python_ir=json.dumps(state["python_ir"], indent=2)
    )

    raw = call_llm(prompt)

    start = raw.find("{")
    end = raw.rfind("}") + 1
    clean = raw[start:end]

    docs = json.loads(clean)

    state["python_system_docs"] = docs
    return state
