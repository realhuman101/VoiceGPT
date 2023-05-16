import poe
import os

from . import textSpeech

client = poe.Client(os.environ['POE_TOKEN'])

while True:
	message = textSpeech.listen()

	for chunk in client.send_message("chinchilla", message): # 'chinchilla' == ChatGPT
		print(chunk["text_new"], end="")
	
	print("\n" + "="*10)
