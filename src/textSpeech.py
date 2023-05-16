import whisper
import speech_recognition as sr

# model = whisper.load_model("base.en")

def listen() -> None:
	while True: # Understandable text loop
		r = sr.Recognizer()
		with sr.Microphone() as source:
			print("Say command")
			audio = r.listen(source)

		try:
			return r.recognize_whisper(audio, language="english")
		except sr.UnknownValueError:
			print("Whisper could not understand audio, please try again")
		except sr.RequestError as e:
			Exception("Could not request results from Whisper, Error: \n", e)