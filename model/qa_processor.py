from transformers import pipeline

def answer_question(image_path, question):
    # Define the NLP pipeline
    nlp = pipeline(
        "document-question-answering",
        model="impira/layoutlm-document-qa",
    )

    # Answer the question for the image
    result = nlp(image_path, question)
    score = result[0]['score'] * 100
    answer = result[0]['answer']

    return score, answer
