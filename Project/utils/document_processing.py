import docx
from PyPDF2 import PdfReader
from fastapi import UploadFile

async def extract_text(file: UploadFile):
    content = await file.read()
    if file.filename.endswith(".pdf"):
        pdf = PdfReader(file.file)
        return " ".join([page.extract_text() for page in pdf.pages])
    elif file.filename.endswith(".docx"):
        doc = docx.Document(file.file)
        return " ".join([para.text for para in doc.paragraphs])
    elif file.filename.endswith(".txt"):
        return content.decode("utf-8")
    else:
        raise ValueError("Unsupported file type")
