import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")

while True:
    s = input("Enter the word you want to say: ")
    if(s == "q"):
        break
    speaker.Speak(s)