import os
import streamlit as st
#from llama_index.readers.file import PDFReader
from llama_index.llms.gemini import Gemini
from llama_index.embeddings.gemini import GeminiEmbedding
import streamlit.components.v1 as components
from pypdf import PdfReader

from llama_index.core import VectorStoreIndex, Document
from llama_index.core.node_parser.text import TokenTextSplitter



# Set Google API key
GOOGLE_API_KEY = os.getenv("api")

llm = Gemini(model="models/gemini-1.5-flash-8b", temperature=0, embedding=GeminiEmbedding,api_key=GOOGLE_API_KEY)

    
def extract_contract(contract_pdf):
    pdf_text = ""
    pdf_reader = PdfReader(contract_pdf)
    number_of_pages = len(pdf_reader.pages)
    for index in range(number_of_pages):
        pdf_text = pdf_text + pdf_reader.pages[index].extract_text()
    return pdf_text







def extract_keypoints(contract_text):
    try:
        key_points = llm.complete(f"You are a contract evaluator, You will be provided a contract, {contract_text}. return the key points that should be known to both the parties")
        return key_points
    except:
        return extract_keypoints(contract_text)

def extract_clauses(contract_text):
    try:
        clauses = llm.complete(f"You are a contract evaluator, You will be provided a contract, {contract_text}.Mention the key clauses and sub clauses of the contract and categorise the contents of contract under the clauses")
        return clauses
    except:
        return extract_clauses(contract_text)

def find_deviations(contract_text, contract_template_text):    
    prompt = f"""
    You are a contract analysis expert.  
    You are given a contract and a template:

    Contract:
    ```
    {contract_text}
    ```

    Template:
    ```
    {contract_template_text}
    ```

    Analyze the contract and the template and identify any deviations.  
    Respond in the following format in markdown:

    - Deviation 1: [Explain the deviation]
    - Deviation 2: [Explain the deviation]
    ...

    Focus on structural differences, missing information, or inconsistencies.
    """
    try:
        response = llm.complete(prompt)
        return response
    except:
        find_deviations(contract_text, contract_template_text)                                                                      
    

if 'contract_text' not in st.session_state:
    st.session_state['contract_text'] = ''

if 'contract_template_text' not in st.session_state:
    st.session_state['contract_template_text'] = ''
















