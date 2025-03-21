import os
import PyPDF2
import cohere
from dotenv import load_dotenv 

# Load environment variables
load_dotenv()

# Initialize Cohere API
COHERE_API_KEY = os.getenv("COHERE_API_KEY")
if not COHERE_API_KEY:
    raise ValueError("Error: COHERE_API_KEY is not set. Please configure your API key.")
co = cohere.Client(api_key=COHERE_API_KEY)

# Function to extract text from PDF
def extract_text_from_pdf(pdf_path):
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"Error: PDF file '{pdf_path}' not found.")

    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        extracted_text = [page.extract_text() for page in reader.pages if page.extract_text()]
        return "\n".join(extracted_text) if extracted_text else "No readable text found in the document."

# Function to generate AI response using Cohere
def generate_response(user_query, pdf_text):
    prompt = f"""
    Use the provided document text to answer the user's question.
    If the document does not contain the answer, use logical reasoning.

    Question: {user_query}
    Document Context: {pdf_text}
    Answer:
    """
    
    response = co.generate(prompt=prompt, model='command-r-plus')
    return response.generations[0].text.strip() if response.generations else "No response generated."

# Example usage
pdf_path = "herbal_medicine.pdf"  # Change this to your PDF file
try:
    pdf_text = extract_text_from_pdf(pdf_path)
    user_query = "What are the medicinal benefits of Aloe Vera?"
    response = generate_response(user_query, pdf_text)
    print("Response:", response)
except Exception as e:
    print("Error:", str(e))
