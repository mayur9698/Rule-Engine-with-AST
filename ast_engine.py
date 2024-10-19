import ast

class Node:
    def __init__(self, node_type, value=None, left=None, right=None):
        self.type = node_type
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"Node(type='{self.type}', value='{self.value}')"

def create_rule(rule_string):
    """Create an AST from a rule string."""
    try:
        parsed_ast = ast.parse(rule_string, mode='eval').body
        return parsed_ast
    except SyntaxError as e:
        raise ValueError(f"Invalid rule: {rule_string}. Error: {e}")

def evaluate_rule(node, data):
    """Evaluate the rule represented by the AST against provided data."""
    if isinstance(node, ast.Compare):
        # Get the left and right values
        left_value = eval(ast.unparse(node.left), {}, data)
        right_value = eval(ast.unparse(node.comparators[0]), {}, data)

        # Get the comparison operator as a string
        operator = type(node.ops[0]).__name__

        # Map the operator name to actual Python operators
        operators_map = {
            'Eq': '==',
            'NotEq': '!=',
            'Lt': '<',
            'LtE': '<=',
            'Gt': '>',
            'GtE': '>='
        }

        # Ensure the operator exists in the map
        if operator not in operators_map:
            raise ValueError(f"Unsupported operator: {operator}")

        # Construct and evaluate the expression
        expression = f"{left_value} {operators_map[operator]} {right_value}"
        return eval(expression)

    elif isinstance(node, ast.BoolOp):
        # Evaluate each child node based on the boolean operator
        results = [evaluate_rule(value, data) for value in node.values]

        if isinstance(node.op, ast.And):
            return all(results)
        elif isinstance(node.op, ast.Or):
            return any(results)

    return False


def combine_rules(rules):
    """Combine multiple rules into a single AST using AND at the root."""
    if not rules:
        return None
    if len(rules) == 1:
        return rules[0]

    # Combine rules using an AND operator at the root
    combined_ast = ast.BoolOp(op=ast.And(), values=rules)
    return combined_ast
