"""Calculate utility tool for DoorDash domain."""

import re
from typing import Dict, Any


def calculate(expression: str) -> Dict[str, Any]:
    """
    Calculate mathematical expressions safely.
    
    Args:
        expression: Mathematical expression to calculate
    
    Returns:
        Dict containing calculation result
    """
    try:
        # Remove any potentially dangerous characters
        safe_expression = re.sub(r'[^0-9+\-*/().\s]', '', expression)
        
        # Evaluate the expression safely
        result = eval(safe_expression)
        
        return {
            "success": True,
            "expression": expression,
            "result": result
        }
        
    except ZeroDivisionError:
        return {
            "success": False,
            "error": "Division by zero is not allowed"
        }
    except Exception as e:
        return {
            "success": False,
            "error": f"Cannot calculate expression: {str(e)}"
        } 