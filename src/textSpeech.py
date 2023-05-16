import whisper
import speech_recognition as sr

# model = whisper.load_model("base.en")

def listen() -> None:
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("Say something!")
		audio = r.listen(source)

	try:
		return recognize_whisper(audio, language="english")
	except sr.UnknownValueError:
		Exception("Whisper could not understand audio")
	except sr.RequestError as e:
		Exception("Could not request results from Whisper, Error: \n", e)