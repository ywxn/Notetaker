from flask import Flask, request, jsonify, render_template
from openai import OpenAI
from flask_cors import CORS
import PyPDF2
from docx import Document

# Loads the OpenAI API key from a file
with open("OPENAI_API_KEY", "r") as file:
    api_key = file.read().strip()

# Set the OpenAI API key
client = OpenAI(api_key=api_key)


# Helper functions
def parse_docx(file_path):
    doc = Document(file_path)
    text = " ".join([paragraph.text for paragraph in doc.paragraphs])
    return text


def parse_pdf(file_path):
    pdf_file_obj = open(file_path, "rb")
    pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)
    text = ""
    for page_num in range(pdf_reader.numPages):
        page_obj = pdf_reader.getPage(page_num)
        text += page_obj.extractText()
    pdf_file_obj.close()
    return text


# Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/generate_notes", methods=["POST"])
def generate_notes():
    input_type = request.form.get("inputType")

    if input_type == "pdf":
        file = request.files.get("file")
        file.save("temp.pdf")
        input_data = parse_pdf("temp.pdf")
        file.rm("temp.pdf")
    elif input_type == "docx":
        file = request.files.get("file")
        file.save("temp.docx")
        input_data = parse_docx("temp.docx")
        file.rm("temp.docx")
    else:
        input_data = request.form.get("inputData")

    # Validate the input
    if not input_type or not input_data:
        return jsonify({"error": "Invalid input"}), 400

    try:
        # Prompt to extract important information and generate notes
        prompt = "Extract important information from the provided input enclosed in triple backticks and present it in a bulleted list of notes:\n\n"
        prompt += f"```{input_data}```\n"
        prompt += "Notes:\n- "

        # Process the input data and generate notes using the OpenAI API
        completion = client.completions.create(
            model="text-davinci-003", prompt=prompt, max_tokens=200
        )

        notes = completion.choices[0].text.strip()

        # Return the generated notes as a JSON response
        return jsonify({"notes": notes})

    except Exception as e:
        # Log the exception details
        app.logger.error("An error occurred: %s", str(e))

    # Return a JSON response with a generic error message
    return jsonify({"error": "Internal Server Error"}), 500
