# gpt3 linkedin post generator by Belghini - version July 2023


import os
import openai
import streamlit as st


# Connect to OpenAI GPT-3, fetch API key from Streamlit secrets
openai.api_key = os.getenv("OPENAI_API_KEY")

#or enter the api key here
openai.api_key =#"........"

Model= "text-davinci-003"


def gen_post(nb_words, subject):

    response = openai.Completion.create(
        engine=Model,
        prompt=f"write a linkedin creator post relative to the subject {subject}. Your content should be engaging, informative, and relevant LinkedIn posts for various professionals across different industries. Add emojis to the content when appropriate and write from a personal experience. The content should be up to {nb_words} words long and spaced out so that it's easy for readers to scan through. Please add relevant hashtags to the post and encourage the readers to comment..",
        temperature=0.8,
        max_tokens=4000,
        top_p=0.8,
        best_of=2,
        frequency_penalty=0.0,
        presence_penalty=0.0)

    return response.get("choices")[0]['text']


def main_gpt_post_generator():

    st.markdown('Generate LinkedIn posts related to a topic - powered by OpenAI using text-davinci-003 Model:sun_with_face:')
    st.write('\n')  # add spacing

    st.subheader('\n What is your Linkedpost is about?\n')

    post_text = ""  # initialize columns variables
    col1, space, col2, space, col3 = st.columns([10, 0.5, 5, 0.5, 10])
    with col1:
        input_topic = st.text_input('Tape a topic')
    with col2:
        input_words = st.text_input('number of words')
    with col3:
        st.write("\n")
        st.write("\n")
        if st.button('Generate Linkedin post'):
            with st.spinner():
                post_text = gen_post(input_words, input_topic)
    if post_text != "":
        st.write('\n')  # add spacing
        with st.expander("SECTION - Linkedin Post", expanded=True):
            st.markdown(post_text)  #output the results


if __name__ == '__main__':
    main_gpt_post_generator()
