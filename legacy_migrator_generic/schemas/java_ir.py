from pydantic import BaseModel
from typing import List

class Endpoint(BaseModel):
    method: str
    path: str
    description: str

class Entity(BaseModel):
    name: str
    fields: List[str]

class JavaDomainIR(BaseModel):
    domain: str
    domain_summary: str
    endpoints: List[Endpoint]
    entities: List[Entity]
    enums: List[str]
    business_logic: List[str]
    usage_examples: List[str]
