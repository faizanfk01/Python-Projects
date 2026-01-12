import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")
speaker.rate = 2

speaker.Speak("Welcome Faizan")
print("Welcome Faizan")

completion = input("Have you completed 100 Days?: ").lower()

if completion == "yes":
    speaker.Speak("Congrats, you have completed 100 days")
    print("Congrats, you have completed 100 days")

elif completion == "no":
    speaker.Speak("Complete the hundred day first")
    print("Complete the hundred days first")

else:
    print("invalid input")