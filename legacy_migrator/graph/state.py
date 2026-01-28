from typing import TypedDict, List, Dict, Any


class MigratorState(TypedDict, total=False):
    java_project_path: str

    domains: list
    java_ir: list
    system_docs: dict

    python_ir: list
    python_system_docs: dict
