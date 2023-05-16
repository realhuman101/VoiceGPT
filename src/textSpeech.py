import whisper
import speech_recognition as sr

model = whisper.load_model("base.en")

r = sr.Recognizer()

def listen() -> str:
	with sr.Microphone() as source:
		print("Say command")
		audio = r.listen(source)

	print("Recieved command...")

	with open("audio.wav", "wb") as f:
		f.write(audio.get_wav_data())
	
	print('Processing command...')
	text = model.transcribe("audio.wav")["text"]

	print("Interpreted Message: " + text + "\n\n\n")
	return text