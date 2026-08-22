# pip install gTTS

from gtts import gTTS
import os

text = "Привет! Это Python читает текст вслух. Привет от Диджитализируй!"
tts  = gTTS(text, lang="ru")
tts.save("voice.mp3")
print("Сохранено в voice.mp3")
os.startfile("voice.mp3")  # Windows; на Linux: os.system("xdg-open voice.mp3")
