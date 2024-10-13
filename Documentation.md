# Dependencies
- [Llama-Index](https://docs.llamaindex.ai/en/stable/DOCS_README/)
- [Gemini](https://docs.llamaindex.ai/en/stable/examples/llm/gemini/)
- [List of Models](https://ai.google.dev/gemini-api/docs/models/gemini)
- [Streamlit](https://docs.streamlit.io)
- [Streamlit UI](https://docs.streamlit.io/develop/api-reference)

# Utility functions

## Rag
rag.py contains the helper functions to update the vector store of the contents of the contract, template

## Utils
utils.py contains helper functions to extract text from PDFs and helper functions to extract *Key Points*, *Clauses*, *Deviations*

# Pages

## Home Page

- New_contract.py contains home page with file uploaders to upload contract, template and utilises the helper functions to extract text from PDF and updating vector stores
- It also uses **query_output** function to answer queries about the contracts


## pages

*All additional pages must be present in the Pages folder only*

### Clauses

- It contains the UI components and uses **extract_clauses** function to extract clauses

### Key Points

- It contains the UI components and uses **extract_keypoints** function to extract clauses

### Deviations

- It contains the UI components and uses **find_deviations** function to extract clauses


