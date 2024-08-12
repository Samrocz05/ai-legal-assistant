# AI Legal Documentation Assistant

## Overview

The AI Legal Documentation Assistant is a web application designed to help users analyze legal documents by either uploading them or scanning them using a camera. It leverages OpenAI's language model to summarize and respond to queries based on the content of the documents.

## Features

- **Document Upload**: Users can upload PDF files or images of documents for analysis.
- **Document Scanning**: Users can capture images of documents using their camera.
- **Document Analysis**: The application extracts text from the uploaded or scanned documents and provides a summary.
- **Query Handling**: Users can ask questions about the document, and the AI provides responses based on the document summary.
- **Directories**: Provides links to various legal resources.

## Requirements

- Python 3.12 or higher
- Flask
- OpenAI Python client
- pdfminer.six
- Pillow
- pytesseract
- Tesseract OCR (for image-to-text conversion)

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/ai-legal-assistant.git
   cd ai-legal-assistant
Create a Virtual Environment

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install Dependencies

bash
Copy code
pip install -r requirements.txt
Set Up Tesseract OCR

Download and install Tesseract OCR from here.
Add Tesseract to your system PATH.
Configure Environment Variables

Add your OpenAI API key in the app.py file:

python
Copy code
openai.api_key = 'YOUR_OPENAI_API_KEY'
Usage
Run the Flask Application

bash
Copy code
python app.py
Access the Application

Open your web browser and navigate to http://127.0.0.1:5000/.

Upload or Scan Documents

Use the Upload Document section to select and upload a file.
Use the Scan Document (using Camera) section to capture a document image using your camera.
Analyze and Query

After uploading or scanning, the document summary will be displayed.
Ask questions about the document and receive responses based on the summary.
Project Structure
php
Copy code
ai-legal-assistant/
│
├── app.py                    # Main Flask application
├── static/
│   ├── css/
│   │   └── styles.css        # Stylesheet for the web application
│   └── images/
│       └── logo.png          # Logo image for the web application
└── templates/
    └── index.html            # HTML template for the web application
Troubleshooting
Error 127.0.0.1 - - [21/Jun/2024 19:21:02] "POST /upload HTTP/1.1" 500 -

This error often indicates a problem with the document processing or API call. Check the error details and ensure that the OpenAI model being used is valid and that the document format is supported.
PDF Syntax Error

This may occur if the uploaded file is not a valid PDF. Ensure that the file being uploaded is a valid PDF or image.
License
This project is licensed under the MIT License. See the LICENSE file for details.

Contact
For questions or further information, please contact:

Sam D
Email: dsam5238@gmail.com
LinkedIn: Sam D
arduino
Copy code

Replace `https://github.com/your-username/ai-legal-assistant.git` with the actual URL of your repository. Adjust any details as needed to fit your project's specifics.
above thi paste in Readme.md right
ChatGPT
Yes, the provided content is meant to be placed in your README.md file. It includes a comprehensive overview of your AI Legal Documentation Assistant project, detailing features, installation instructions, usage, and troubleshooting tips.

Here's how you can use it:

Create a README.md File: If you don’t have one already, create a new file named README.md in the root directory of your project.

Paste the Content: Copy the provided content and paste it into the README.md file.

Save the File: Save the README.md file to ensure all the information is stored properly.