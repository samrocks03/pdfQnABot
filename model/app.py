import os
import streamlit as st
from PIL import Image
from pdf_processor import process_pdf
from qa_processor import answer_question

# Streamlit interface
st.title("PDF Question Answering Bot")
uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file:
    # Ensure the uploads directory exists
    uploads_dir = "uploads"
    os.makedirs(uploads_dir, exist_ok=True)
    
    # Save uploaded PDF
    pdf_path = os.path.join(uploads_dir, uploaded_file.name)
    with open(pdf_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Process PDF to images
    image_paths = process_pdf(pdf_path)
    st.write("PDF processed into images:")

    # Display images
    for image_path in image_paths:
        image = Image.open(image_path)
        st.image(image, caption=os.path.basename(image_path))

    question = st.text_input("Ask a question about the PDF:")
    if question:
        st.write("Processing your question...")
        # Answer the question for each image
        for image_path in image_paths:
            accuracy, answer = answer_question(image_path, question)
            st.markdown(f"<p style='color:{'green' if accuracy >= 95 else 'red'};font-size:30px'><b>Accuracy of the model:</b> {accuracy:.3f}%</p>", unsafe_allow_html=True)
            st.markdown(f"<p style='font-size:30px'><b>Output of the model:</b> <u>{answer}</u></p>", unsafe_allow_html=True)

        # st.write("Question processing complete.")
