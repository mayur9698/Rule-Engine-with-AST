from flask import Flask, request, jsonify
from ast_engine import create_rule, combine_rules, evaluate_rule
import sqlite3

app = Flask(__name__)

# Database connection function
def get_db_connection():
    conn = sqlite3.connect('rules.sql')
    conn.row_factory = sqlite3.Row
    return conn

# API to create a new rule
@app.route('/create_rule', methods=['POST'])
def create_rule_api():
    data = request.json
    rule_string = data.get('rule_string')
    if not rule_string:
        return jsonify({'error': 'Rule string is required'}), 400
    
    try:
        ast = create_rule(rule_string)
        conn = get_db_connection()
        conn.execute("INSERT INTO rules (rule_string, ast_json) VALUES (?, ?)", 
                     (rule_string, str(ast)))
        conn.commit()
        conn.close()
        return jsonify({'message': 'Rule created successfully', 'ast': str(ast)})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# API to evaluate a rule
@app.route('/evaluate_rule', methods=['POST'])
def evaluate_rule_api():
    data = request.json
    rule_ast = data.get('rule_ast')
    attributes = data.get('data')

    try:
        result = evaluate_rule(rule_ast, attributes)
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
