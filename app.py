from flask import Flask, render_template, request

app = Flask(__name__)

# Route to display the HTML page
@app.route('/')
def home():
    return render_template('index.html')

# Route triggered by the HTML form submit button
@app.route('/run-script', methods=['POST'])
def run_script():
    # Execute custom Python code
    print("Success! The HTML button triggered this Python text.")
    
    # Perform calculations or processing
    result = 10 + 20
    
    return f"Python code executed successfully! Result: {result}"

if __name__ == '__main__':
    app.run(debug=True)
