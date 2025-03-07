from flask import Flask , render_template, jsonify, request
from limiter import Limiter
from limiter.util import get_remote_address
from simpleeval import simple_eval, InvalidExpression

# Define a name to flask 
app = Flask(__name__)
app.config('JSON_SORT_KEY') = False

limiter=Limiter (
   app=app, 
   default_limit=['200 per day','50 per hour'],
   key_func = get_remote_address
   
)

def safe_eval(expression):
    try:

        # Convert UI symbol to Python
        expr = expression.replace('x','*').replace('÷','/')

        # Allow only basic math operations
        return str(simple_eval(expr,function={}, name={}))

    except ( InvalidExpression ,SyntaxError, ZeroDivisionError):
        return None    
    

@app.route('/')

def home():
    """Serve calculator interface"""
    return render_template('index.html')    

@app.route('/calculate', methods=['POST'])

def calculate():
    # Get used data as input
    data = request.get_json()

    #Pulls out the expresssion
    expression= data.get('expression','')

    # Check for empty or too long
    if not expression or len(expression) > 100:
        return jsonify({'error': 'error', 'result': 'Invalid Input'}), 400


    # Remove any white space
    expression = expression.strip()


    # Validate characters
    allowed_char = set('0123456789+/*-.()')
    if not all(c in allowed_char for c in expression):
        return jsonify({'error': 'error', 'result': 'Invalid User Input'}), 400

    #Evaluate the expression
    result = safe_eval(expression)

    #If the result failed return an error
    if result is None:
        return jsonify({'error': 'error', 'result': 'Invalid User Input'}), 400

    # Sends the result back in json format
    return jsonify({'result': result})

if __name__== '__main__':
 app.run (host='0.0.0.0', port=5000, debug=True)
