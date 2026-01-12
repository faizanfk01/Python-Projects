import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")

names = ["John", "Harry", "Faizan"]

for name in names:
    speaker.Speak(f"Shoutout to {name}")
    print(f"Shoutout to {name}")