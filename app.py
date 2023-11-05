import streamlit as st
import PyPDF2

def pdf_to_text(uploaded_pdf):
    text = ''
    pdf_reader = PyPDF2.PdfReader(uploaded_pdf)
    for page in range( len(pdf_reader.pages)):
        text += pdf_reader.pages[page].extract_text()
    return text


st.set_page_config(page_title="BookQuester", page_icon="📖", layout="wide")
st.header("📖BookQuester")

topics = st.text_input('Enter topic :',)

uploaded_file = st.file_uploader(
    "Upload a pdf, docx, or txt file",
    type=["pdf", "docx", "txt"],
    help="Scanned documents are not supported yet!",
)
if uploaded_file:
    text = pdf_to_text(uploaded_file)
    with open("extracted_text.txt", "w", encoding="utf-8") as file:
        file.write(text)
    
st.write(uploaded_file)