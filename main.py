import streamlit as st
from _speechElevenLabs import generate_speech
from _langchain import get_all_prompts

col1, col2 = st.columns(2)

def submit(paragraphs, style, voice_actor):
    generated_img_prompts = get_all_prompts(paragraphs, style)
    generated_speech = generate_speech(paragraphs, voice_actor)
    return [generated_img_prompts, generated_speech]

with col1: 
    st.header("Text")
    with st.form("Text input", clear_on_submit=False):
        paragraphs = st.text_area("Enter your text here")
        style = st.selectbox(
            'Art style',
            ('Dreamy','Water Color'))
        voice_actor = st.selectbox(
            'Voice actors',
            ('Adam','Bella'))
        submit_button = st.form_submit_button(label="Generate")

with col2: 
    st.header("Audiobook")
    if submit_button:
        generation = submit(paragraphs, style, voice_actor)
        image_prompts = generation[0]
        audio = generation[1]
    if submit_button:
        st.info(image_prompts)
        st.audio(audio)
    # if submit_button:
    #     video = submit(paragraphs)
    # if submit_button:
    #     st.video(video)