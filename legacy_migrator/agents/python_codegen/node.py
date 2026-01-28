from pathlib import Path
import re


def sanitize(name: str) -> str:
    """
    Convert human descriptions into valid python identifiers.
    """
    name = name.lower()
    name = re.sub(r"[^a-z0-9]+", "_", name)
    return name.strip("_")


def python_codegen_node(state: dict):

    python_ir = state["python_ir"]

    base = Path("output/python_app")

    routers = base / "routers"
    models = base / "models"
    services = base / "services"

    routers.mkdir(parents=True, exist_ok=True)
    models.mkdir(parents=True, exist_ok=True)
    services.mkdir(parents=True, exist_ok=True)

    # -------------------------
    # requirements.txt
    # -------------------------
    (base / "requirements.txt").write_text(
        "fastapi\nuvicorn\npydantic\n"
    )

    # -------------------------
    # main.py
    # -------------------------
    imports = []
    includes = []

    for d in python_ir:
        lname = d["domain"].lower()
        imports.append(f"from routers import {lname}")
        includes.append(f"app.include_router({lname}.router)")

    main_py = f"""
from fastapi import FastAPI

{chr(10).join(imports)}

app = FastAPI()

{chr(10).join(includes)}
"""

    (base / "main.py").write_text(main_py.strip() + "\n")

    # -------------------------
    # Per domain generation
    # -------------------------
    for d in python_ir:
        domain = d["domain"]
        lname = domain.lower()

        # -------- Models --------
        model_file = models / f"{lname}.py"

        model_lines = [
            "from pydantic import BaseModel",
            ""
        ]

        for m in d["models"]:
            model_lines.append(f"class {m['name']}(BaseModel):")
            if m["fields"]:
                for f in m["fields"]:
                    model_lines.append(f"    {f}: str")
            else:
                model_lines.append("    pass")
            model_lines.append("")

        model_file.write_text("\n".join(model_lines))

        # -------- Services --------
        service_file = services / f"{lname}_service.py"

        service_lines = [
            f"class {domain}Service:",
            "    pass",
            ""
        ]

        service_file.write_text("\n".join(service_lines))

        # -------- Routers --------
        router_file = routers / f"{lname}.py"

        router_lines = [
            "from fastapi import APIRouter",
            f"from models.{lname} import *",
            f"from services.{lname}_service import {domain}Service",
            "",
            "router = APIRouter()",
            "",
            f"service = {domain}Service()",
            ""
        ]

        for r in d["routes"]:
            fname = sanitize(r["function"])
            router_lines.append(
                f"@router.{r['method'].lower()}('{r['path']}')")
            router_lines.append(f"def {fname}():")
            router_lines.append("    return {'status': 'ok'}")
            router_lines.append("")

        router_file.write_text("\n".join(router_lines))

    return state
