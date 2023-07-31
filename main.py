import streamlit as st
from _speechElevenLabs import generate_speech

col1, col2 = st.columns(2)

def submit(input_text, voice_actor):
    generated_speech = generate_speech(input_text, voice_actor)
    return generated_speech

with col1: 
    st.header("Text")
    with st.form("Text input", clear_on_submit=False):
        input_text = st.text_area("Enter your text here")
        voice_actor = st.selectbox(
            'Voice actors',
            ('Adam','Bella'))
        submit_button = st.form_submit_button(label="Generate")

with col2: 
    st.header("Audiobook")
    if submit_button:
        audio = submit(input_text, voice_actor)
    if submit_button:
        st.audio(audio)
    # if submit_button:
    #     video = submit(input_text)
    # if submit_button:
    #     st.video(video)pip