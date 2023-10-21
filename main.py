import speech_recognition as speech_recog
import random
#### V1 - function
def speach():
    mic = speech_recog.Microphone()
    recog = speech_recog.Recognizer()

    with mic as audio_file:
        recog.adjust_for_ambient_noise(audio_file)
        audio = recog.listen(audio_file)
        return recog.recognize_google(audio, language="en-EN")

#### V2 - script
levels = {

    "easy": ["Dairy", "Mouse", "Computer"],

    "medium": ["Programming", "Algorithm", "Developer"],

    "hard": ["Neural network", "Machine learning", "Artificial intelligence"]

}
while True:
    print("="*50)
    difficulty = input('Choose the level easy/medium/hard or type stop to stop the game:')
    if difficulty == 'easy':
        word = random.choice(levels["easy"])
    elif difficulty == 'medium':
        word = random.choice(levels["medium"])
    elif difficulty == 'hard':
        word = random.choice(levels["hard"])
    elif difficulty == 'stop':
        break
    else:
        print('Please, type the give variants')
        break
    print(f'say the word: {word}')

    lword = word.lower()
    uword = word[0].upper() + word[1:]

    mic = speech_recog.Microphone()
    recog = speech_recog.Recognizer()

    with mic as audio_file:
        print("Speak Please")

        recog.adjust_for_ambient_noise(audio_file)
        audio = recog.listen(audio_file)

        if lword == recog.recognize_google(audio, language="en_EN") or uword == recog.recognize_google(audio, language="en_EN"):
            print('Correct Congrats!')
        else:
            print('Incorrect, you lost, deleting Windows...')
        print(f'you said: {recog.recognize_google(audio, language="en_EN")}')
    print("="*50)