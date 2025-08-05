import speech_recognition as sr

def get_voice_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak your command (e.g., 'Spin chapter 1')...")
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio)
        print("Heard:", command)
        return command.lower()
    except sr.UnknownValueError:
        print("Could not understand audio")
        return ""
