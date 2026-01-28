<<<<<<< Updated upstream
=======
from dotenv import load_dotenv
load_dotenv()

# if __name__ == "__main__":
#     result = java_scanner_node({
#         "java_project_path": "../LegacyTicketTracker"
#     })

#     for d in result["domains"]:
#         print("\nDOMAIN:", d["name"])
#         print("Controller:", d["controller"])
#         print("Service:", d["service"])
#         print("Repository:", d["repository"])
#         print("Models:", d["models"])
#         print("DTOs:", d["dtos"])


# from agents.java_scanner.node import java_scanner_node
# from agents.java_analyzer.node import java_analyzer_node
# from agents.java_docs.node import java_docs_node

# if __name__ == "__main__":

#     state = java_scanner_node({
#         "java_project_path": "../LegacyTicketTracker"
#     })

#     state = java_analyzer_node(state)

#     # 👇 THIS MUST EXIST
#     state = java_docs_node(state)

#     print("Java MkDocs generated.")


# from agents.java_scanner.node import java_scanner_node
# from agents.java_analyzer.node import java_analyzer_node
# from agents.java_docs.node import java_docs_node
# from agents.python_designer.node import python_designer_node

# if __name__ == "__main__":

#     state = java_scanner_node({
#         "java_project_path": "../LegacyTicketTracker"
#     })

#     state = java_analyzer_node(state)
#     state = java_docs_node(state)

#     state = python_designer_node(state)

#     print(state["python_ir"])

from agents.java_scanner.node import java_scanner_node
from agents.java_analyzer.node import java_analyzer_node
from agents.java_docs.node import java_docs_node
from agents.java_docs.system_doc import system_doc_node
from agents.python_docs.system_doc import python_system_doc_node
from agents.python_designer.node import python_designer_node
from agents.python_docs.node import python_docs_node


def main():

    # -------------------------
    # Step 1: Scan Java project
    # -------------------------
    state = java_scanner_node({
        "java_project_path": "../LegacyTicketTracker"
    })

    # -------------------------
    # Step 2: Java -> Java IR
    # -------------------------
    state = java_analyzer_node(state)

    # -------------------------
    # Step 2.5: System Docs (LLM once)
    # -------------------------
    state = system_doc_node(state)

    # -------------------------
    # Step 3: Java MkDocs
    # -------------------------
    state = java_docs_node(state)

    # -------------------------
    # Step 4: Java IR -> Python IR
    # -------------------------
    state = python_designer_node(state)


    state = python_system_doc_node(state)


    # -------------------------
    # Step 5: Python MkDocs
    # -------------------------
    state = python_docs_node(state)

    print("\n✅ Pipeline completed successfully.\n")
    print("Java docs:    legacy_migrator/output/java_docs")
    print("Python docs:  legacy_migrator/output/python_docs\n")


if __name__ == "__main__":
    main()

>>>>>>> Stashed changes
