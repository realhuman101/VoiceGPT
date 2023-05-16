import speech_recognition as sr

# model = whisper.load_model("base.en")

r = sr.Recognizer()

def listen() -> str:
	while True: # Understandable text loop
		with sr.Microphone() as source:
			print("Say command")
			audio = r.listen(source)

		print('audio finished recording')

		try:
			thi = r.recognize_sphinx(audio)
			print("THING:", thi)
			print(type(thi))
			return thi
		except sr.UnknownValueError:
			print("Sphinx could not understand audio, please try again")
		except sr.RequestError as e:
			Exception("Could not request results from Sphinx, Error: \n", e)