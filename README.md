# 📄 AI Chatbot on Your Documents

This project is a simple Flask-based API that allows you to **upload a document** (PDF, DOCX, or TXT) and **ask questions** about its content. The app extracts the text from your uploaded file and uses OpenAI’s GPT model to generate relevant answers based on the content.

---

## 🚀 Features

- Upload `.pdf`, `.docx`, or `.txt` documents
- Automatically extract and read file content
- Use OpenAI GPT (via `gpt-4o-mini`) to answer custom user questions
- Simple REST API endpoint: `POST /chat_with_doc`
- CORS enabled for frontend integration

---

## 🛠️ Technologies Used

- Python 3
- Flask
- flask-cors
- OpenAI SDK
- pdfplumber (PDF parsing)
- python-docx (DOCX parsing)

---

## 📁 Project Structure
custom_chatbot-/
│
├── app.py              # Flask backend code


---

## 📦 Installation

1. **Clone the repo**
```bash
git clone https://github.com/talluriprudhvi/custom_chatbot-.git
cd custom_chatbot-


📬 API Usage

Endpoint: /chat_with_doc

Method: POST
Content-Type: multipart/form-data

Form Fields:
	•	file: Your uploaded .pdf, .docx, or .txt file
	•	question: A question related to the document

Example cURL Command:
curl -X POST http://127.0.0.1:5000/chat_with_doc \
  -H "Content-Type: multipart/form-data" \
  -F "file=@/path/to/document.pdf" \
  -F "question=What is this document about?"