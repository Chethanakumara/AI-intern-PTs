import ast
import os
from rag_engine import generate_rag_feedback


def analyze_python_file(file_path):

    if not os.path.exists(file_path):
        print("❌ File not found!")
        return None

    with open(file_path, "r", encoding="utf-8") as file:
        source_code = file.read()

    total_lines = len(source_code.splitlines())
    tree = ast.parse(source_code)

    functions = 0
    classes = 0
    imports = []

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            functions += 1
        elif isinstance(node, ast.ClassDef):
            classes += 1
        elif isinstance(node, ast.Import):
            for item in node.names:
                imports.append(item.name)

    imports = list(set(imports))

    return {
        "file_name": os.path.basename(file_path),
        "total_lines": total_lines,
        "functions": functions,
        "classes": classes,
        "imports": imports
    }


def main():
    file_path = input("Enter Python file path: ")
    result = analyze_python_file(file_path)

    if result:
        print("\n📊 CODE ANALYSIS REPORT")
        print("----------------------")
        print(f"File      : {result['file_name']}")
        print(f"Lines     : {result['total_lines']}")
        print(f"Functions : {result['functions']}")
        print(f"Classes   : {result['classes']}")

        print("\n🤖 RAG-BASED AI FEEDBACK")
        print("------------------------")
        feedback = generate_rag_feedback(result)
        for tip in feedback:
            print("-", tip)


if __name__ == "__main__":
    main()
