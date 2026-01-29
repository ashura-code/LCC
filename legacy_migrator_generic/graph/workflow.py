from langgraph.graph import StateGraph, END

from graph.state import MigratorState

from agents.java_scanner.node import java_scanner_node
from agents.java_analyzer.node import java_analyzer_node
from agents.java_docs.system_doc import system_doc_node
from agents.java_docs.node import java_docs_node

from agents.python_designer.node import python_designer_node
from agents.python_docs.system_doc import python_system_doc_node
from agents.python_docs.node import python_docs_node
from agents.python_codegen.node import python_codegen_node


def build_graph():

    graph = StateGraph(MigratorState)

    graph.add_node("java_scanner", java_scanner_node)
    graph.add_node("java_analyzer", java_analyzer_node)
    graph.add_node("java_system_docs", system_doc_node)
    graph.add_node("java_docs", java_docs_node)

    graph.add_node("python_designer", python_designer_node)
    graph.add_node("python_system_docs", python_system_doc_node)
    graph.add_node("python_docs", python_docs_node)
    graph.add_node("python_codegen", python_codegen_node)

    graph.set_entry_point("java_scanner")

    graph.add_edge("java_scanner", "java_analyzer")
    graph.add_edge("java_analyzer", "java_system_docs")
    graph.add_edge("java_system_docs", "java_docs")

    graph.add_edge("java_docs", "python_designer")
    graph.add_edge("python_designer", "python_system_docs")
    graph.add_edge("python_system_docs", "python_docs")
    graph.add_edge("python_docs", "python_codegen")

    graph.add_edge("python_codegen", END)

    return graph.compile()
