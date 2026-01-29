from utils.mkdocs import write_java_mkdocs,build_mkdocs
def java_docs_node(state):
    write_java_mkdocs(state,"output/java_docs"); build_mkdocs("output/java_docs"); return state
