from flask import Flask, request, jsonify
from openai import OpenAI

app = Flask(__name__)

# Read the OpenAI API key from a file
with open('OPENAI_API_KEY', 'r') as file:
    api_key = file.read().strip()
# Set the OpenAI API key
client = OpenAI(api_key=api_key)

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
        # Adjust the OpenAI API call based on your specific needs
        response = client.completions.create(engine="text-davinci-003",
        prompt=input_data,
        max_tokens=150)

        notes = response.choices[0].text.strip()

        # Return the generated notes as a JSON response
        return jsonify({'notes': notes})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(port=8888)
