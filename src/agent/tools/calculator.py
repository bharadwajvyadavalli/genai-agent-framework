import ast
import operator as op

# supported operators
_OPERATORS = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.Pow: op.pow,
    ast.Mod: op.mod,
    ast.USub: op.neg
}

def _safe_eval(node):
    if isinstance(node, ast.Num):
        return node.n
    if isinstance(node, ast.BinOp):
        return _OPERATORS[type(node.op)](_safe_eval(node.left), _safe_eval(node.right))
    if isinstance(node, ast.UnaryOp):
        return _OPERATORS[type(node.op)](_safe_eval(node.operand))
    raise ValueError(f"Unsupported expression: {node}")

class CalculatorTool:
    def run(self, expression: str) -> str:
        try:
            tree = ast.parse(expression, mode='eval')
            result = _safe_eval(tree.body)
            return str(result)
        except Exception as e:
            return f"Error evaluating expression: {e}"
