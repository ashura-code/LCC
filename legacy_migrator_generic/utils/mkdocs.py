from pathlib import Path
import subprocess
import json


def safe(v):
    if isinstance(v, (dict, list)):
        return json.dumps(v, indent=2)
    return str(v)


# -------------------------------------------------------------------
# Java MkDocs
# -------------------------------------------------------------------

def write_java_mkdocs(state: dict, output_dir: str):

    java_ir = state["java_ir"]
    system_docs = state.get("system_docs", {})

    output = Path(output_dir)
    docs = output / "docs"
    docs.mkdir(parents=True, exist_ok=True)

    index = docs / "index.md"

    with index.open("w", encoding="utf-8") as f:
        f.write("# Legacy Java System Documentation\n\n")

        f.write("## Introduction\n")
        f.write(safe(system_docs.get("introduction", "")) + "\n\n")

        f.write("## Architecture\n")
        f.write(safe(system_docs.get("architecture", "")) + "\n\n")

        f.write("## Requirements\n")
        for r in system_docs.get("requirements", []):
            f.write(f"- {safe(r)}\n")

        f.write("\n## Installation\n")
        for i in system_docs.get("installation", []):
            f.write(f"- {safe(i)}\n")

        f.write("\n## How To Run\n")
        for r in system_docs.get("run_instructions", []):
            f.write(f"- {safe(r)}\n")

        f.write("\n## Usage Examples\n")
        for u in system_docs.get("usage_examples", []):
            f.write(f"- {safe(u)}\n")

        f.write("\n## Domains\n")
        for d in java_ir:
            f.write(f"- [{d['domain']}]({d['domain']}.md)\n")

    for d in java_ir:
        page = docs / f"{d['domain']}.md"

        with page.open("w", encoding="utf-8") as f:
            f.write(f"# {d['domain']}\n\n")

            f.write("## Overview\n")
            f.write(safe(d.get("domain_summary", "")) + "\n\n")

            f.write("## API Endpoints\n")
            for e in d.get("endpoints", []):
                f.write(
                    f"- **{e['method']}** `{e['path']}` — {safe(e['description'])}\n")

            f.write("\n## Entities\n")
            for ent in d.get("entities", []):
                fields = ", ".join(ent.get("fields", [])) if ent.get(
                    "fields") else "relationship only"
                f.write(f"- **{ent['name']}**: {fields}\n")

            if d.get("enums"):
                f.write("\n## Enums\n")
                for e in d["enums"]:
                    f.write(f"- {safe(e)}\n")

            if d.get("business_logic"):
                f.write("\n## Business Logic\n")
                for b in d["business_logic"]:
                    f.write(f"- {safe(b)}\n")

            if d.get("usage_examples"):
                f.write("\n## Usage Examples\n")
                for u in d["usage_examples"]:
                    f.write(f"- {safe(u)}\n")

    mkdocs_yml = output / "mkdocs.yml"

    with mkdocs_yml.open("w", encoding="utf-8") as f:
        f.write("""site_name: Legacy Java Documentation

theme:
  name: material

nav:
  - Home: index.md
""")
        for d in java_ir:
            f.write(f"  - {d['domain']}: {d['domain']}.md\n")


# -------------------------------------------------------------------
# Python MkDocs
# -------------------------------------------------------------------

def write_python_mkdocs(state: dict, output_dir: str):

    python_ir = state["python_ir"]
    system_docs = state.get("python_system_docs", {})

    output = Path(output_dir)
    docs = output / "docs"
    docs.mkdir(parents=True, exist_ok=True)

    index = docs / "index.md"

    with index.open("w", encoding="utf-8") as f:
        f.write("# Python FastAPI System Documentation\n\n")

        f.write("## Introduction\n")
        f.write(safe(system_docs.get("introduction", "")) + "\n\n")

        f.write("## Architecture\n")
        f.write(safe(system_docs.get("architecture", "")) + "\n\n")

        f.write("## Requirements\n")
        for r in system_docs.get("requirements", []):
            f.write(f"- {safe(r)}\n")

        f.write("\n## Installation\n")
        for i in system_docs.get("installation", []):
            f.write(f"- {safe(i)}\n")

        f.write("\n## How To Run\n")
        for r in system_docs.get("run_instructions", []):
            f.write(f"- {safe(r)}\n")

        f.write("\n## Usage Examples\n")
        for u in system_docs.get("usage_examples", []):
            f.write(f"- {safe(u)}\n")

        f.write("\n## Domains\n")
        for d in python_ir:
            f.write(f"- [{d['domain']}]({d['domain']}.md)\n")

    for d in python_ir:
        page = docs / f"{d['domain']}.md"

        with page.open("w", encoding="utf-8") as f:
            f.write(f"# {d['domain']}\n\n")

            f.write("## Overview\n")
            f.write(safe(d.get("description", "")) + "\n\n")

            f.write("## API Routes\n")
            for r in d.get("routes", []):
                f.write(
                    f"- **{r['method']}** `{r['path']}` → `{r['function']}`\n")

            f.write("\n## Models\n")
            for m in d.get("models", []):
                f.write(f"- **{m['name']}**: {', '.join(m['fields'])}\n")

            if d.get("enums"):
                f.write("\n## Enums\n")
                for e in d["enums"]:
                    f.write(f"- {safe(e)}\n")

            if d.get("services"):
                f.write("\n## Services\n")
                for s in d["services"]:
                    f.write(f"- {safe(s)}\n")

    mkdocs_yml = output / "mkdocs.yml"

    with mkdocs_yml.open("w", encoding="utf-8") as f:
        f.write("""site_name: Python FastAPI Documentation

theme:
  name: material

nav:
  - Home: index.md
""")
        for d in python_ir:
            f.write(f"  - {d['domain']}: {d['domain']}.md\n")


# -------------------------------------------------------------------
# Build helper
# -------------------------------------------------------------------

def build_mkdocs(path: str):
    subprocess.run(["mkdocs", "build"], cwd=path, check=True)
