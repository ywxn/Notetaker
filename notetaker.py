from flask import Flask, request, jsonify, render_template
from openai import OpenAI
from flask_cors import CORS
import PyPDF2
from docx import Document
import os

# Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Loads the OpenAI API key from a file
with open("OPENAI_API_KEY", "r") as file:
    api_key = file.read().strip()

# Set the OpenAI API key
client = OpenAI(api_key=api_key)


# Helper functions
def parse_text(file_path):
    # check if plain text file
    with open(file_path, "r") as file:
        text = file.read()
    return text


def parse_docx(file_path):
    doc = Document(file_path)
    text = " ".join([paragraph.text for paragraph in doc.paragraphs])
    return text


def parse_pdf(file_path):
    pdf_file_obj = open(file_path, "rb")
    pdf_reader = PyPDF2.PdfReader(pdf_file_obj)
    text = ""
    for page_num in range(len(pdf_reader.pages)):
        page_obj = pdf_reader.pages[page_num]
        text += page_obj.extract_text()
    pdf_file_obj.close()
    return text


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/generate_notes", methods=["POST"])
def generate_notes():
    input_type = request.form.get("inputType")

    if input_type == "fileInput":
        file = request.files.get("file")
        os.mkdir("uploads")
        file_path = os.path.join("uploads", file.filename)
        file.save(file_path)

        if file_path.endswith(".txt"):
            input_data = parse_text(file_path)
        elif file_path.endswith(".pdf"):
            input_data = parse_pdf(file_path)
        elif file_path.endswith(".docx"):
            input_data = parse_docx(file_path)

        os.remove(file_path)
        os.removedirs("uploads")
    else:
        input_data = request.form.get("noteInput")

    if not input_type or not input_data:
        return jsonify({"error": "Invalid input"}), 400

    try:
        # Prompt to extract important information and generate notes
        prompt = "Extract important information from the provided input enclosed in triple backticks and present it in a bulleted list of notes:\n\n"
        prompt += f"```{input_data}```\n"
        prompt += "Notes:\n- "

        # Process the input data and generate notes using the OpenAI API
        completion = client.completions.create(
            model="gpt-3.5-turbo-instruct", prompt=prompt, max_tokens=200
        )

        notes = completion.choices[0].text.strip().split("\n")

        # Return the generated notes as a JSON response
        return jsonify({"notes": notes})

    except Exception as e:
        app.logger.error("An error occurred: %s", str(e))

    return jsonify({"error": "Internal Server Error"}), 500


if __name__ == "__main__":
    app.run(debug=True)
