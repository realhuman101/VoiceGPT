import whisper
import speech_recognition as sr

model = whisper.load_model("base.en")

r = sr.Recognizer()

def listen() -> str:
	while True: # Understandable text loop
		with sr.Microphone() as source:
			print("Say command")
			audio = r.listen(source)

		print("Recieved command...")

		with open("audio.wav", "wb") as f:
			f.write(audio.get_wav_data())
		
		print('Processing command...')
		text = model.transcribe("audio.wav")["text"]

		try:
			# txt = r.recognize_sphinx(audio)
			print("Interpreted Message: " + text + "\n\n\n")
			return text
		except sr.UnknownValueError:
			print("Sphinx could not understand audio, please try again")
		except sr.RequestError as e:
			Exception("Could not request results from Sphinx, Error: \n", e)