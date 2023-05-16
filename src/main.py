import poe
import os

client = poe.Client(os.environ['POE_TOKEN'])

message = "Explain to me 10 differnt methods steel can be used in a desk tidy, bold important text"

for chunk in client.send_message("chinchilla", message):
    print(chunk["text_new"], end="")