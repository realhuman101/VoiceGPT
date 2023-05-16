import poe
import os

from . import textSpeech

client = poe.Client(os.environ['POE_TOKEN'])

message = """
please write sentence in simplified chinese level (foreign language, heavily simplified) with each of the words: （with pinyin and translation)
实验室
操场
寒假
暑假
学费
习惯
担心
明白
教学楼
没想到
虽然。。。但是。。。
"""

for chunk in client.send_message("chinchilla", message):
    print(chunk["text_new"], end="")

# textSpeech.listen()