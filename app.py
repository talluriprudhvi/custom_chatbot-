from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI
import os
import tempfile
import docx
import pdfplumber

app = Flask(__name__)
CORS(app)

# Replace with your actual OpenAI API key
api_key = " "  # keep this in an env var for production
client = OpenAI(api_key=api_key)

def extract_text(file_path, file_type):
    text = ""
    if file_type.endswith('.pdf'):
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""
    elif file_type.endswith('.docx'):
        doc = docx.Document(file_path)
        for para in doc.paragraphs:
            text += para.text + "\n"
    elif file_type.endswith('.txt'):
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()
    return text.strip()

@app.route('/chat_with_doc', methods=['POST'])
def chat_with_doc():
    if 'file' not in request.files or 'question' not in request.form:
        return jsonify({'error': 'File and question are required'}), 400

    file = request.files['file']
    question = request.form['question']

    with tempfile.NamedTemporaryFile(delete=False) as temp:
        file.save(temp.name)
        file_path = temp.name
        file_type = file.filename.lower()

        try:
            document_text = extract_text(file_path, file_type)
            if not document_text:
                return jsonify({'answer': "Could not extract content from the document."})

            prompt = f"""Use the following document content to answer the question.\n\nDocument:\n{document_text[:3000]}\n\nQuestion: {question}\nAnswer:"""

            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are a helpful AI assistant."},
                    {"role": "user", "content": prompt}
                ]
            )
            answer = response.choices[0].message.content.strip()
            return jsonify({'answer': answer})

        finally:
            os.remove(file_path)

if __name__ == '__main__':
    app.run(debug=True)