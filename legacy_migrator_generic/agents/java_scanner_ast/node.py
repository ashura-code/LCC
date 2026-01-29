from pathlib import Path
from tree_sitter import Parser, Language
import tree_sitter_java


def java_ast_scanner_node(state: dict):

    project = Path(state["java_project_path"])

    # Convert capsule → Language object
    JAVA_LANGUAGE = Language(tree_sitter_java.language())

    parser = Parser()
    parser.language = JAVA_LANGUAGE

    classes = []

    for file in project.rglob("*.java"):
        if "target" in str(file):
            continue

        src = file.read_text(encoding="utf-8")
        tree = parser.parse(bytes(src, "utf8"))
        root = tree.root_node

        for node in root.children:
            if node.type == "class_declaration":

                class_name = None
                methods = []

                for child in node.children:

                    if child.type == "identifier":
                        class_name = src[child.start_byte:child.end_byte]

                    if child.type == "method_declaration":
                        for m in child.children:
                            if m.type == "identifier":
                                methods.append(
                                    src[m.start_byte:m.end_byte]
                                )

                classes.append({
                    "class": class_name,
                    "methods": methods,
                    "file": str(file)
                })

    state["structural_ir"] = classes
    return state
