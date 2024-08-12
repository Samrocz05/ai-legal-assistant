from flask import Flask, request, jsonify, render_template
from werkzeug.utils import secure_filename
from pdfminer.high_level import extract_text
from PIL import Image
import pytesseract
import openai
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

# Ensure the upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# OpenAI API key
openai.api_key = 'YOUR_OPENAI_API_KEY'

def analyze_document(file_path):
    try:
        if file_path.endswith('.pdf'):
            text = extract_text(file_path)
        else:
            # Use Tesseract OCR for images
            image = Image.open(file_path)
            text = pytesseract.image_to_string(image)
        return text
    except Exception as e:
        print(f"Error processing document: {e}")
        return None

def summarize_text(text):
    response = openai.Completion.create(
        engine="gpt-3.5-turbo",
        prompt=f"Summarize the following document:\n\n{text}",
        max_tokens=150
    )
    return response.choices[0].text.strip()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"})
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"})

    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)

    text = analyze_document(file_path)
    if not text:
        return jsonify({"error": "Failed to process document"})

    summary = summarize_text(text)
    return jsonify({"summary": summary})

@app.route('/query', methods=['POST'])
def query():
    data = request.json
    user_query = data.get("query")
    document_summary = data.get("summary")
    
    response = openai.Completion.create(
        engine="gpt-3.5-turbo",
        prompt=f"Based on the following document summary, answer the user's question:\n\nSummary: {document_summary}\n\nQuestion: {user_query}",
        max_tokens=150
    )
    return jsonify({"response": response.choices[0].text.strip()})

@app.route('/directories', methods=['GET'])
def directories():
    directories_info = {
        "Legal Advice": "https://www.legaladvice.com",
        "Court Forms": "https://www.courtforms.com",
        "Law Libraries": "https://www.lawlibraries.com",
        "Legal News": "https://www.legalnews.com",
        "Legal Research": "https://www.legalresearch.com"
    }
    return jsonify(directories_info)

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, request, jsonify, render_template
from werkzeug.utils import secure_filename
import pytesseract
from pdfminer.high_level import extract_text
import openai
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

# Ensure the upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# OpenAI API key
openai.api_key = 'sk-proj-W7sAuxMK1zxmk50o4yxNT3BlbkFJ2lpiuFPtnteNqW4WgcFh'

def analyze_document(file_path):
    try:
        if file_path.endswith('.pdf'):
            text = extract_text(file_path)
        else:
            text = pytesseract.image_to_string(file_path)
        return text
    except Exception as e:
        print(f"Error processing document: {e}")
        return None

def summarize_text(text):
    try:
        response = openai.Completion.create(
            engine="gpt-3.5-turbo",
            prompt=f"Summarize the following document:\n\n{text}",
            max_tokens=150
        )
        return response.choices[0].text.strip()
    except openai.error.InvalidRequestError as e:
        print(f"Error summarizing text: {e}")
        return "Error summarizing text: API request was invalid or exceeded quota."
    except openai.error.OpenAIError as e:
        print(f"OpenAI API error: {e}")
        return "OpenAI API error: Please check your plan and billing details."
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return "An unexpected error occurred while summarizing text."

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"})
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"})
    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)
    text = analyze_document(file_path)
    if not text:
        return jsonify({"error": "Failed to process document"})
    summary = summarize_text(text)
    return jsonify({"summary": summary})

@app.route('/query', methods=['POST'])
def query():
    data = request.json
    user_query = data.get("query")
    document_summary = data.get("summary")
    
    try:
        response = openai.Completion.create(
            engine="gpt-3.5-turbo",
            prompt=f"Based on the following document summary, answer the user's question:\n\nSummary: {document_summary}\n\nQuestion: {user_query}",
            max_tokens=150
        )
        return jsonify({"response": response.choices[0].text.strip()})
    except openai.error.OpenAIError as e:
        print(f"OpenAI API error: {e}")
        return jsonify({"error": "OpenAI API error: Please check your plan and billing details."})
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return jsonify({"error": "An unexpected error occurred while querying the document."})

@app.route('/directories', methods=['GET'])
def directories():
    directories_info = {
        "Legal Advice": "https://www.legaladvice.com",
        "Court Forms": "https://www.courtforms.com",
        "Law Libraries": "https://www.lawlibraries.com",
        "Legal News": "https://www.legalnews.com",
        "Legal Research": "https://www.legalresearch.com"
    }
    return jsonify(directories_info)

if __name__ == '__main__':
    app.run(debug=True)
