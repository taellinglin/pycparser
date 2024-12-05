import shutil
import ast
import astor

def backup_and_modify_c_parser(filepath):
    # Backup the original file
    backup_path = filepath.replace(".py", "_original.py")
    shutil.copy(filepath, backup_path)
    print(f"Backup created: {backup_path}")

    # Parse the original file
    with open(filepath, "r", encoding="utf-8") as file:
        tree = ast.parse(file.read())

    # Add default docstrings to functions without them
    class DocstringAdder(ast.NodeTransformer):
        def visit_FunctionDef(self, node):
            if not ast.get_docstring(node):
                node.body.insert(0, ast.Expr(value=ast.Str("Auto-added docstring")))
            return node

    modified_tree = DocstringAdder().visit(tree)

    # Save the modified file
    modified_code = astor.to_source(modified_tree)
    with open(filepath, "w", encoding="utf-8") as file:
        file.write(modified_code)
    print(f"Modified file saved: {filepath}")

# Run the script
original_file_path = "c_parser.py"  # Replace with your file path if different
backup_and_modify_c_parser(original_file_path)
