import os

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI()

with open("recording.mp3", "rb") as audio_file:
  translation = client.audio.translations.create(
    model="whisper-1",
    file=audio_file,
  )

print(translation.text)
