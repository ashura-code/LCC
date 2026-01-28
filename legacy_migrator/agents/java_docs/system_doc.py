import json
from utils.llm import call_llm


SYSTEM_DOC_PROMPT = """
You are documenting a backend system.

Using this structured Java IR:

{java_ir}

Generate system documentation.

Return ONLY JSON:

{{
 "introduction": string,
 "requirements": [string],
 "installation": [string],
 "run_instructions": [string],
 "architecture": string,
 "usage_examples": [string]
}}
"""


def system_doc_node(state: dict):

    prompt = SYSTEM_DOC_PROMPT.format(
        java_ir=json.dumps(state["java_ir"], indent=2)
    )

    raw = call_llm(prompt)

    start = raw.find("{")
    end = raw.rfind("}") + 1
    clean = raw[start:end]

    state["system_docs"] = json.loads(clean)

    return state
