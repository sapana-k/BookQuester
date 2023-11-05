import streamlit as st

st.set_page_config(page_title="BookQuester", page_icon="📖", layout="wide")
st.header("📖BookQuester")

topics = st.text_input('Enter topic :')

uploaded_file = st.file_uploader(
    "Upload a pdf, docx, or txt file",
    type=["pdf", "docx", "txt"],
    help="Scanned documents are not supported yet!",
)

st.write(uploaded_file)