import streamlit as st
from utils import find_deviations
from rag import query_output


def main():
    st.title("Deviations App")

    if ('contract_text' in st.session_state and st.session_state['contract_text'] != '') and ('contract_template_text' in st.session_state and st.session_state['contract_template_text'] != ''):
        if 'deviations' not in st.session_state:
            with st.spinner('Extracting Deviations...'):
                st.session_state['deviations'] = find_deviations(st.session_state['contract_text'],st.session_state['contract_template_text'])
                st.success("Done!")
                st.toast('Deviations extracted!')


        st.markdown(st.session_state['deviations'].text)
    else:
        st.markdown("# Go back and upload the contract and Template!!")

    if st.session_state['contract_text'] != '':
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



