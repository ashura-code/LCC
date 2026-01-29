from utils.mkdocs import write_python_mkdocs,build_mkdocs
def python_docs_node(state):
    write_python_mkdocs(state,"output/python_docs"); build_mkdocs("output/python_docs"); return state
