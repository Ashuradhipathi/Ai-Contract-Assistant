import streamlit as st
from utils import extract_keypoints
from rag import query_output


def main():
    st.title("Insights App")

    if 'contract_text' in st.session_state and st.session_state['contract_text'] != '':
        if 'keypoints' not in st.session_state:
            with st.spinner('Extracting Contract...'):
                st.session_state['keypoints'] = extract_keypoints(st.session_state['contract_text'])
            st.success("Done!")
            st.toast('Key Points extracted!')


        st.markdown(st.session_state['keypoints'].text)
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