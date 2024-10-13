import os
import streamlit as st
from utils import extract_contract
from rag import query_output, update_vector_store






def main():
    st.title("Upload New Contracts and Templates")

    st.write("Upload a Contract")
    contract_pdf = st.file_uploader("Upload Contract PDF", type=["pdf"])
    if contract_pdf:
        with st.spinner('Extracting Contract...'):
            st.session_state['contract_text'] =  extract_contract(contract_pdf)
            update_vector_store(st.session_state['contract_text'])
            if 'clauses' in st.session_state:
                st.session_state.popitem('clauses')
            if 'keypoints' in st.session_state :
                st.session_state.popitem('keypoints')
        st.success("Done!")
        st.toast('Contract extracted!')




    st.write("Upload The Template")
    template_pdf = st.file_uploader("Upload Template PDF", type=["pdf"])
    if template_pdf:
        with st.spinner('Extracting Template...'):
            st.session_state['contract_template_text'] =  extract_contract(template_pdf)
            update_vector_store(st.session_state['contract_template_text'])

            if 'deviations' in st.session_state:
                st.session_state.popitem('deviations')
        st.success("Done!")
        st.toast('Template extracted!')

    if 'contract_text' in st.session_state and st.session_state['contract_text'] != '':
        prompt = st.chat_input("If you have any doubts about clauses, let us know!")
        if prompt:
            with st.chat_message("user"):
                st.write(prompt)
            with st.spinner("Answering Your Query"):
                response = query_output(prompt)
                with st.chat_message("bot"):
                    st.write(response.text)





if __name__ == "__main__":
    main()

