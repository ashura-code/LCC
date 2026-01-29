import json
from agents.java_analyzer.prompts import JAVA_ANALYSIS_PROMPT
from schemas.java_ir import JavaDomainIR
from utils.llm import call_llm

def java_analyzer_node(state:dict):
    out=[]
    for d in state["domains"]:
        prompt=JAVA_ANALYSIS_PROMPT.format(
            controller=d["source"]["controller"],
            service=d["source"]["service"],
            models="".join(d["source"]["models"])
        )
        raw=call_llm(prompt)
        clean=raw[raw.find("{"):raw.rfind("}")+1]
        data=json.loads(clean)
        data["domain"]=d["name"]
        out.append(JavaDomainIR(**data).model_dump())
    state["java_ir"]=out
    return state
