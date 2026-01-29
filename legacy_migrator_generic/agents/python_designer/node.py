import json
from agents.python_designer.prompts import PYTHON_DESIGN_PROMPT
from schemas.python_ir import PythonDomainIR
from utils.llm import call_llm

def python_designer_node(state):
    out=[]
    for d in state["java_ir"]:
        raw=call_llm(PYTHON_DESIGN_PROMPT.format(java=json.dumps(d)))
        clean=raw[raw.find("{"):raw.rfind("}")+1]
        data=json.loads(clean)
        data["domain"]=d["domain"]
        out.append(PythonDomainIR(**data).model_dump())
    state["python_ir"]=out
    return state
