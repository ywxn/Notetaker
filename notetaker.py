from flask import Flask, request, jsonify, render_template
from openai import OpenAI
from flask_cors import CORS
import webbrowser

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Read the OpenAI API key from a file
with open('OPENAI_API_KEY', 'r') as file:
    api_key = file.read().strip()

# Set the OpenAI API key
client = OpenAI(api_key=api_key)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_notes', methods=['POST'])
def generate_notes():
    data = request.get_json()

    input_type = data.get('inputType')
    input_data = data.get('inputData')

    # Validate the input
    if not input_type or not input_data:
        return jsonify({'error': 'Invalid input'}), 400

    try:
        # Process the input data and generate notes using the OpenAI API
        completion = client.completions.create(model='gpt-3.5-turbo-instruct', prompt=input_data, max_tokens=50)

        notes = completion.choices[0].text

        # Return the generated notes as a JSON response
        return jsonify({'notes': notes})

    except Exception as e:
    # Log the exception details
        app.logger.error("An error occurred: %s", str(e))

    # Return a JSON response with a generic error message
    return jsonify({'error': 'Internal Server Error'}), 500


if __name__ == '__main__':
    app.run(debug=True)
    # open the flask app in the default browse