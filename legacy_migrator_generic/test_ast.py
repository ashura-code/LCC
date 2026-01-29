from agents.java_scanner_ast.node import java_ast_scanner_node

state = {
    "java_project_path": "../LegacyTicketTracker"
}

state = java_ast_scanner_node(state)

print(state["structural_ir"][:3])
