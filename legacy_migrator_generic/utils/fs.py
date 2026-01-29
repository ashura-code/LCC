from pathlib import Path

def read_file(path: Path) -> str:
    return path.read_text(encoding="utf-8")

def collect_java_files(root: Path):
    return [p for p in root.rglob("*.java") if "target" not in str(p)]
