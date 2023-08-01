import time
import streamlit as st
from _speechElevenLabs import generate_and_save_all_speech
from _promptOpenAI import get_all_prompts
from _stablediffusion import gen_all_images
from _storybook import generate_video

st.set_page_config(page_title="Audiovisual-books")
st.title('📚🗺️ Audiovisual-books ')

XI_API_KEY = st.sidebar.text_input('Eleven labs API Key')
OPENAI_API_KEY = st.sidebar.text_input('OpenAI API Key')
DREAMSTUDIO_API_KEY = st.sidebar.text_input('Dream Studio API Key')

col1, col2 = st.columns(2)

def submit(paragraphs, style, voice_actor):
    texts = paragraphs.split('\n')
    generated_img_prompts = get_all_prompts(texts, style, OPENAI_API_KEY)
    image_list, warning_messages = gen_all_images(generated_img_prompts, DREAMSTUDIO_API_KEY)
    audio_list = generate_and_save_all_speech([(idx, text) for idx, text in enumerate(texts)], voice_actor, XI_API_KEY)
    video_path = generate_video(image_list, audio_list)
    return [video_path, warning_messages]

with col1: 
    st.header("Text")
    with st.form("Text input", clear_on_submit=False):
        paragraphs = st.text_area(label = "Enter your text here", value= "A man walking along the river. \nA woman walking along the ocean.")
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
        with st.spinner('Wait for it...'):
            time.sleep(5)
            generation = submit(paragraphs, style, voice_actor)
            video_path = generation[0]
            warning_messages = generation[1]
            for warning_message in warning_messages:
                st.warning(warning_message)
        st.success('Done!')
    if submit_button:
        st.video(video_path)