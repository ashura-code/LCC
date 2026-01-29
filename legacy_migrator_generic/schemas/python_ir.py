from pydantic import BaseModel
from typing import List

class PythonRoute(BaseModel):
    method: str
    path: str
    function: str

class PythonModel(BaseModel):
    name: str
    fields: List[str]

class PythonDomainIR(BaseModel):
    domain: str
    description: str
    routes: List[PythonRoute]
    models: List[PythonModel]
    enums: List[str]
    services: List[str]
