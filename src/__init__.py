import poe
import os

from . import textSpeech

client = poe.Client(os.environ['POE_TOKEN'])

message = ""

for chunk in client.send_message("chinchilla", message):
    print(chunk["text_new"], end="")

# textSpeech.listen()