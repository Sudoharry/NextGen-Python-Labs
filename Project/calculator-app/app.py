from flask import Flask, render_template, request, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from simpleeval import simple_eval, InvalidExpression 

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

# Initialize limiter after creating app
limiter = Limiter(
    app=app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)
def safe_eval(expression):
    """Safely evaluate mathematical expressions using simpleeval"""
    try:
        # Convert UI symbols to Python operators
        expr = expression.replace('×', '*').replace('÷', '/')
        # Allow only basic math operations
        return str(simple_eval(expr, functions={}, names={}))
    except (InvalidExpression, SyntaxError, ZeroDivisionError):
        return None

@app.route('/')
def home():
    """Serve calculator interface"""
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    expression = data.get('expression', '')
    
    if not expression or len(expression) > 100:
        return jsonify({'result': 'Error', 'error': 'Invalid input'}), 400
    
    # Remove any whitespace
    expression = expression.strip()
    
    # Validate characters
    allowed_chars = set('0123456789+-×÷%.()')
    if not all(c in allowed_chars for c in expression):
        return jsonify({'result': 'Error', 'error': 'Invalid characters'}), 400
    
    result = safe_eval(expression)
    
    if result is None:
        return jsonify({'result': 'Error', 'error': 'Invalid expression'}), 400
    
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)