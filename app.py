# Import the necessary libraries
import streamlit as st
import fitz # PyMuPDF library for working with PDF files
import random

# Define a function to chat with a PDF file
def chat_with_pdf(pdf_file):
    # Open the PDF file and get the number of pages
    pdf = fitz.open(stream=pdf_file.read(), filetype="pdf")
    num_pages = pdf.pageCount

    # Choose a random page and extract its text
    page_num = random.randint(0, num_pages - 1)
    page = pdf.loadPage(page_num)
    page_text = page.getText()

    # Display the page number and the text
    st.write(f"Page {page_num + 1} of {num_pages}:")
    st.write(page_text)

    # Ask the user to enter a question or a comment about the text
    user_input = st.text_input("Enter a question or a comment about the text:")

    # Generate a response based on the user input and the text
    # This is a very simple and naive way of generating a response
    # You can use more advanced natural language processing techniques to improve it
    if user_input:
        if "?" in user_input:
            # If the user input is a question, try to answer it using the text
            response = "I don't know the answer to that question. Maybe you can find it in the text."
        else:
            # If the user input is a comment, try to acknowledge it or give feedback
            response = "That's an interesting comment. I agree with you." 
        st.write(response)

# Create a title and a sidebar for the web app
st.title("Chat with any PDF")
st.sidebar.header("Upload a PDF file")

# Allow the user to upload a PDF file from their device
uploaded_file = st.sidebar.file_uploader("Choose a PDF file", type="pdf")

# If a PDF file is uploaded, call the chat_with_pdf function
if uploaded_file is not None:
    chat_with_pdf(uploaded_file)
