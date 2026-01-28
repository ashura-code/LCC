from pathlib import Path
from utils.fs import collect_java_files, read_file

def java_scanner_node(state: dict):
    root = Path(state["java_project_path"]) / "src/main/java"
    files = collect_java_files(root)
    controllers = [f for f in files if f.name.endswith("Controller.java")]
    domains = []
    for c in controllers:
        name = c.stem.replace("Controller","")
        def find(x): return next((f for f in files if f.name==x),None)
        service = find(f"{name}Service.java")
        repo = find(f"{name}Repository.java")
        models = [f for f in files if f.parent.name=="model" and f.stem.startswith(name)]
        dtos = [f for f in files if f.parent.name=="dto" and f.stem.startswith(name)]
        domains.append({
            "name":name,
            "source":{
                "controller":read_file(c),
                "service":read_file(service) if service else "",
                "repository":read_file(repo) if repo else "",
                "models":[read_file(m) for m in models],
                "dtos":[read_file(d) for d in dtos],
            }
        })
    state["domains"]=domains
    return state
