# /usr/python3

import sys
import pyttsx3
import speech_recognition as spr
import wikipedia


class VoiceCommander(object):

    def __init__(self):
        self.recognize = spr.Recognizer()
        self.microphone = spr.Microphone()
        self.engine = pyttsx3.init('nsss')
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[32].id)

    def voice(self, audio):
        print('Lyra: ' + audio)
        self.engine.say(audio)
        self.engine.runAndWait()

    def run(self):
        with self.microphone as input:
            print("Listening...")
            self.recognize.pause_threshold = 1
            audio = self.recognize.listen(input)
        try:
            query = self.recognize.recognize_google(audio, language='en-in')
            print('You: ' + query + '\n')
        except spr.UnknownValueError:
            self.voice("Sorry sir! I don't understand that yet. Try typing the command!")
            query = str(input('Command: '))
        return query


if __name__ == '__main__':
    vc = VoiceCommander()
    vc.voice('Hello Sir, I am your assistant the lady Lyra!')
    vc.voice('How may I assist you?')

    while True:
        q = vc.run().lower()
        try:
            if 'who are you' in q:
                vc.voice('I am your assistant the lady Lyra! Sir!')
            elif 'what is your name' in q:
                vc.voice('My name is Lyra! Sir!')
            elif 'hello' in q:
                vc.voice('Hello Sir')
            elif 'bye' in q:
                vc.voice('Bye, Have a good day Sir!.')
                sys.exit()
            else:
                vc.voice('Searching...')
                results = wikipedia.summary(q)
                vc.voice('Lyra Find it.')
                vc.voice('According to Wikipedia - ')
                vc.voice(results)
        except Exception as e:
            print("Exception is: ", e)

