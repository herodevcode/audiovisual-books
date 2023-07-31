import os
from elevenlabs import generate, set_api_key

#Define function for generating speech
def generate_speech(text_input, voice_actor):

    #Set API key for ElevenLabs
    set_api_key(os.getenv("XI_API_KEY"))

    generated_speech = generate(
        text = text_input,
        voice = voice_actor,
        model = 'eleven_monolingual_v1')
    
    return generated_speech

# generate_speech("Hello, my name is Bella. I am a voice from Eleven Labs. I am a text to speech model. ", "Bella")