import streamlit as st
from utils import extract_clauses
from rag import query_output


def main():
    st.title("Clauses App")

    if 'contract_text' in st.session_state and st.session_state['contract_text'] != '':
        if 'clauses' not in st.session_state:
            with st.spinner('Extracting Clauses...'):
                st.session_state['clauses'] = extract_clauses(st.session_state['contract_text'])
            st.success("Done!")
            st.toast('Clauses extracted!')


        st.markdown(st.session_state['clauses'].text)
    else:
        st.markdown("# Go back and upload the contract!!")

    if 'contract_text' in st.session_state and st.session_state['contract_text'] != '':
        prompt = st.chat_input("If you have any doubts, let us know!")
        if prompt:
            with st.chat_message("user"):
                st.write(prompt)
            with st.spinner("Answering Your Query"):
                response = query_output(prompt)
                with st.chat_message("bot"):
                    st.write(response.text)
    


if __name__ == "__main__":
    main()