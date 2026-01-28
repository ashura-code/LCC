# from agents.java_scanner.node import java_scanner_node
# from agents.java_analyzer.node import java_analyzer_node
# from agents.java_docs.system_doc import system_doc_node
# from agents.java_docs.node import java_docs_node
# from agents.python_designer.node import python_designer_node
# from agents.python_docs.system_doc import python_system_doc_node
# from agents.python_docs.node import python_docs_node
# from agents.python_codegen.node import python_codegen_node

# state={"java_project_path":"../LegacyTicketTracker"}
# state=java_scanner_node(state)
# state=java_analyzer_node(state)
# state=system_doc_node(state)
# state=java_docs_node(state)
# state=python_designer_node(state)
# state=python_system_doc_node(state)
# state=python_docs_node(state)
# state=python_codegen_node(state)
# print("DONE")


from graph.workflow import build_graph


if __name__ == "__main__":

    app = build_graph()

    initial_state = {
        "java_project_path": "../LegacyTicketTracker"
    }

    result = app.invoke(initial_state)

    print("\n✅ Migration pipeline completed.\n")
