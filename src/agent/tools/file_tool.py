class FileTool:
    def run(self, operation: str, path: str, content: str = None) -> str:
        try:
            if operation == 'read':
                with open(path, 'r', encoding='utf-8') as f:
                    return f.read()
            elif operation == 'write':
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(content or '')
                return f"Written to {path}."
            else:
                return "Invalid operation. Use 'read' or 'write'."
        except Exception as e:
            return f"FileTool error: {e}"
