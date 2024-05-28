import webbrowser as web
import speech_recognition as sr
def main():
     path="C:/Program Files/Google/Chrome/Application/chrome.exe %s"           #forward slash

     r=sr.Recognizer()
     with sr.Microphone() as source:
          r.adjust_for_ambient_noise(source)
          print('Speak anything : ')
          audio=r.listen(source)             #records from mic
     
          try:
               query=r.recognize_google(audio)         #recognize voice
               print('You said :{}'.format(query))
          
               search_url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
               web.open(search_url)
               web.get(path).open(query)
          except:
               print('Sorry could not recognize your voice')
if __name__=="__main__":
     main()