import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

from pydub import AudioSegment

r = sr.Recognizer()

playsound('test.mp3')
sound = AudioSegment.from_mp3('test.mp3')
sound.export("test.wav", format="wav")

harvard = sr.AudioFile('test.wav')
with harvard as source :
    audio = r.record(source)
    test = r.recognize_google(audio)

if test == 'it was a cold':
    playsound('result.wav')

#with sr.Microphone() as source : 
#    audio = r.listen(source)
#    test = r.recognize_google(audio)
#test = 'It was a cold day. Kipper was at school getting ready to go home. Good job, everyone!'
#gt = gTTS(test)

#gt.save('test.wav')


#playsound('test.wav')