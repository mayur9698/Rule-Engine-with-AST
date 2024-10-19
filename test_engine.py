import unittest
from ast_engine import create_rule, evaluate_rule, combine_rules
import ast  # Import Python's AST module to check node types

class TestRuleEngine(unittest.TestCase):

    def test_create_rule(self):
        """Test Case 1: Create Rule"""
        rule_string = "((age > 30 and department == 'Sales') or (age < 25 and department == 'Marketing'))"
        rule_ast = create_rule(rule_string)
        # Validate that the returned object is an AST node
        self.assertIsInstance(rule_ast, ast.AST)
        print(f"AST for Rule 1: {ast.unparse(rule_ast)}")

    def test_combine_rules(self):
        """Test Case 2: Combine Rules"""
        rule1 = create_rule("age > 30 and department == 'Sales'")
        rule2 = create_rule("salary > 50000 or experience > 5")

        combined_ast = combine_rules([rule1, rule2])
        self.assertIsInstance(combined_ast, ast.BoolOp)
        print(f"Combined AST: {ast.unparse(combined_ast)}")

    def test_evaluate_rule(self):
        """Test Case 3: Evaluate Rule"""
        rule_string = "age > 30 and salary > 50000"
        rule_ast = create_rule(rule_string)

        data = {"age": 35, "department": "Sales", "salary": 60000, "experience": 3}
        result = evaluate_rule(rule_ast, data)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
