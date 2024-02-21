from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

OPENAI_API_KEY = ""

# Replace 'your-api-key' with your OpenAI API key
openai.api_key = OPENAI_API_KEY

@app.route('/generate_notes', methods=['POST'])
def generate_notes():
    data = request.get_json()

    input_type = data.get('inputType')
    input_data = data.get('inputData')

    # Process the input data and generate notes using the OpenAI API
    # Adjust the OpenAI API call based on your specific needs
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=input_data,
        max_tokens=150
    )

    notes = response.choices[0].text.strip()

    return jsonify({'notes': notes})

if __name__ == '__main__':
    app.run(port=8000)
