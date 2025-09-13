# Copyright Sierra

from tau_bench.envs.tool import Tool


class Calculate(Tool):
    @staticmethod
    def invoke(data, expression: str) -> str:
        try:
            import ast
            import operator
            
            # Safe evaluation using ast.literal_eval for simple expressions
            allowed_chars = set('0123456789+-*/.() ')
            if not all(c in allowed_chars for c in expression):
                return "Error: Invalid characters in expression"
            
            # Define safe operations
            ops = {
                ast.Add: operator.add,
                ast.Sub: operator.sub,
                ast.Mult: operator.mul,
                ast.Div: operator.truediv,
                ast.Pow: operator.pow,
                ast.USub: operator.neg,
                ast.UAdd: operator.pos,
            }
            
            def safe_eval(node):
                if isinstance(node, ast.Constant):  # Python 3.8+
                    return node.value
                elif isinstance(node, ast.Num):  # Python < 3.8
                    return node.n
                elif isinstance(node, ast.BinOp):
                    return ops[type(node.op)](safe_eval(node.left), safe_eval(node.right))
                elif isinstance(node, ast.UnaryOp):
                    return ops[type(node.op)](safe_eval(node.operand))
                else:
                    raise ValueError(f"Unsupported operation: {type(node)}")
            
            tree = ast.parse(expression, mode='eval')
            result = safe_eval(tree.body)
            return str(round(result, 2))
            
        except Exception as e:
            return f"Error: {str(e)}"

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "calculate",
                "description": "Perform mathematical calculations",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "expression": {
                            "type": "string",
                            "description": "Mathematical expression to calculate (e.g., '2 + 3 * 4')"
                        }
                    },
                    "required": ["expression"]
                }
            }
        }