# PDF Question Answering Bot

![PDF Question Answering Bot](https://media.licdn.com/dms/image/C4E12AQEQv1eyCBZUTQ/article-cover_image-shrink_720_1280/0/1592238018499?e=2147483647&v=beta&t=TQ4vCHx8dyyrHlzsp5mt6ez3CLUWj0lFUMngJl0icG0)

This Streamlit application allows users to upload a PDF file and ask questions about its content. The application uses LayoutLM, a transformer-based model for document understanding, to extract information and provide answers to user queries.

## Folder Structure

```
F:.
│   .gitignore
│   LICENSE
│   readme.md
│
├───model
│   │   app.py
│   │   pdf_processor.py
│   │   qa_processor.py
│   │   requirements.txt
│   │
│   └───__pycache__
│           pdf_processor.cpython-311.pyc
│           qa_processor.cpython-311.pyc
│
├───uploads
│   │   invoice.pdf
│   │
│   └───images
│           invoice_1.png
│
└───__pycache__
        pdf_processor.cpython-311.pyc
        qa_processor.cpython-311.pyc

```



## Setup

1. Clone the repository:

   ```
   git clone https://github.com/samrocks03/pdfQnABot.git
   ```
2. Navigate to the project directory:

    ```
    cd pdfQnABot/model
    ```

3. Install the required dependencies:
    ```
        pip install -r -q requirements.txt
    ```

4. Run the Streamlit application:
    ```
        streamlit run app.py
    ```

