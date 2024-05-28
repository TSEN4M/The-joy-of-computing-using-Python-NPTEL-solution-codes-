import speech_recognition as sr
from playsound import playsound 

AUDIO_FILE=("sample_1.wav")  #place the file name in the braces
#use the audion file as the source

playsound('sample_1.wav')#playing the audiofile sample_1.wav

r=sr.Recognizer()       #r is an object of class speech_recognition.Recognizer
print(type(r))

with sr.AudioFile(AUDIO_FILE) as source:
        audio=r.record(source)
        print(type(audio))              #audio is an object of class speech_recognition.AudioData
#reads the audio file

try:
        print('audio file contains :' + r.recognize_google(audio))
except sr.UnknownValueError:
        print('Google Speech Recognition could not understand audio')
except sr.RequestError:
        print("couldn't get the results from Google Speech Recognition")
