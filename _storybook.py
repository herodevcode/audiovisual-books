from moviepy.editor import ImageClip, TextClip, CompositeVideoClip, AudioFileClip
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.VideoClip import ImageClip, TextClip
from PIL import ImageFont

video_width = 1280
video_height = 720
fps = 30
background_color = 'white'

def create_slide(text, illustration_path, audio_path):
    # Load the illustration
    illustration = ImageClip(illustration_path).set_duration(10)  # Set duration in seconds

    # Load the audio
    audio = AudioFileClip(audio_path)

    # Create a text clip with the provided text
    font_size = 30
    font = ImageFont.truetype("illustrations/1.png", font_size)  # Replace with the path to your desired font
    text_clip = TextClip(text, font=font, size=(video_width, video_height), color='black').set_duration(audio.duration)

    # Combine the text clip and illustration
    slide = CompositeVideoClip([illustration, text_clip])

    # Add the audio to the slide
    slide = slide.set_audio(audio)

    return slide

# Assuming you have lists of text paragraphs, illustration paths, and audio paths
texts = [...]  # List of text paragraphs
illustration_paths = [...]  # List of paths to illustration images
audio_paths = [...]  # List of paths to audio files

# Create a list to hold all the slides
slides = []

for i, text in enumerate(texts):
    illustration_path = illustration_paths[i]
    audio_path = audio_paths[i]

    slide = create_slide(text, illustration_path, audio_path)
    slides.append(slide)

final_video = CompositeVideoClip(slides, size=(video_width, video_height)).set_fps(fps)
final_video.write_videofile("output/storybook.mp4", codec='libx264')