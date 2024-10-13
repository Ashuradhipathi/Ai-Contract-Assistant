import os
import streamlit as st
#from llama_index.readers.file import PDFReader

from llama_index.embeddings.gemini import GeminiEmbedding
from llama_index.core import VectorStoreIndex, Document
from llama_index.core.node_parser.text import TokenTextSplitter
from utils import GOOGLE_API_KEY, llm

text_splitter = TokenTextSplitter(chunk_size=512)  
embedding_model = GeminiEmbedding(api_key=GOOGLE_API_KEY)

def update_vector_store(text):
    chunks = text_splitter.split_text(text)
    documents = []
    for chunk in chunks:
        documents.append(Document(text=chunk))
    st.session_state['vector_store'] = VectorStoreIndex.from_documents(documents,embed_model=embedding_model)
    

def query_output(query):
    if 'vector_store' in st.session_state:
        query_engine = st.session_state['vector_store'].as_query_engine(response_mode="tree_summarize",llm=llm)
        results = query_engine.query(query)
        response = llm.complete(f"Answer the question: {query} in reference with {results}")
    else:
        update_vector_store(st.session_state['contract_text'])
    return response